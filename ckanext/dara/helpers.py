# Hendrik Bunke
# ZBW - Leibniz Information Centre for Economics

import ckan.plugins.toolkit as tk
from ckan.common import c, request
from ckanext.dara import schema as dara_schema
from ckanext.dara.schema import author_fields, fields
from ckanext.dara.ftools import list_dicter, dicter
from pylons import config
import json
from ckan.new_authz import users_role_for_group_or_org
from ckan import model
import requests
from hurry.filesize import size, si
from toolz.itertoolz import last
import json



def dara_pkg():
    """
    get package for several helper functions
    XXX DO WE REALLY NEED THIS?
    """

    pkg_id = tk.c.id
    try:
        pkg = tk.get_action('package_show')(None, {'id': pkg_id})
    except:
        pkg = model.Package.by_name(pkg_id)

    # params = request.params
    return pkg


def dara_debug(obj):
    pkg_dict = dara_pkg()
    import ipdb; ipdb.set_trace()


def dara_auto_fields():
    pkg = dara_pkg()
    site_url = config.get('ckan.site_url')

    # fallback for development
    if 'localhost' in site_url:
        site_url = "http://edawax.de"

    pkg_url = tk.url_for(controller='package', action='read', id=pkg['name'])
    dara_url = site_url + pkg_url

    return {'URL': dara_url}


def dara_author_fields():
    return dara_schema.author_fields()


def dara_resource():
    """
    somehow hack. c.resource doesnt return a resource when calling .../dara_xml
    """
    # TODO improve this. We should somehow be able to get the type of the
    # context (resource or package)
    try:
        if 'resource' in request.path:
            return tk.get_action('resource_show')(None, {'id': c.resource_id})
        else:
            return c.resource
    except:
        return False


# def get_request_params():
#    return tk.request.params


def dara_resource_url(url):
    """
    for development. dara does not accept localhost urls
    """
    if 'localhost' in url:
        url = url.replace('localhost', 'edawax.de')
    return url


def dara_md():
    """
    returns dara keys with dara names (this is a relict)
    """
    named_levels = {}
    all_levels = dara_schema.fields()

    for i in all_levels:
        d = 'dara_' + i.id
        named_levels[d] = {'name': i.widget.name}

    return named_levels


# XXX why is there a param 'data_type'?
def dara_authors(dara_type, data):
    """
    return authors as dict
    """
    pack = data or dara_pkg()
    v = pack.get('dara_authors') # None if key does not exist
    if isinstance(v, unicode):
        import ast
        new_v = ast.literal_eval(v)
        return list_dicter(new_v[:], [i.id for i in author_fields()])
    if isinstance(v, list):
        return list_dicter(v[:], [i.id for i in author_fields()])
    if isinstance(v, basestring):
        return json.loads(v)
    return None

def check_journal_role(pkg, role):
    user = tk.c.user
    if not user:
        return False
    group = pkg.get('owner_org', pkg.get('group_id', False))
    if group:
        return users_role_for_group_or_org(group, user) == role
    return False


def resource_is_internal(res):
    url = res['url']
    site_url = config.get('ckan.site_url')
    return url.startswith(site_url)


def fileinfo(res):
    """
    return dictionary with filename and filesize of res
    """
    url = res['url']
    req = requests.head(url, headers={'Accept-Encoding': 'identity'})
    filename = last(filter(lambda i: i, url.split('/')))
    cr = last(req.headers.get('content-range', '0').split('/'))
    cl = req.headers.get('content-length', cr)
    
    # for now we just take the original content-length
    # filesize = size(int(cl), system=si)
    
    return {'filesize': cl,
            'filename': filename}



def av_transform(num):
    """ necessary for backward compatibilty in v4_0 """
    options = {'1': 'Download', '2': 'Delivery', '3': 'OnSite', '4':
            'NotAvailable', '5': 'Unknown'}
    return options.get(num, 'Unknown')


def unit_type_transform(num):
    numstrings = map(str, range(1, 14))
    values = ['Individual', 'Organization', 'Family', 'Family.HouseholdFamily',
            'Household', 'HousingUnit', 'EventOrProcess', 'GeographicUnit', 'TimeUnit',
            'TextUnit', 'Group', 'Object', 'Other']
    d = dict(zip(numstrings, values))
    return d.get(num)


def org_extra_info(pkg):
    """ Get extra values for an organization (ISBN/ISSN) """
    journal = pkg['organization']['name']
    data = tk.get_action('organization_show')(None, {'id': journal})
    if data:
        return (data['publicationID'], data['publicationID_Type'])
    return (0, 0)

def resource_type(data):
    if data == 'data':
        return 'Dataset'

    if data == "text":
        return "Text"

    if data == "code":
        return "Software"

    if data == "other":
        return "Other"

def _parse_authors(data):
    authors = []
    data = json.loads(data)
    for author in data:
        first = author['firstname'][0]
        last = author['lastname']
        authors.append('{}, {}.'.format(last, first))
    return ', '.join(authors)

def build_citation(data):
    """ Build a citation using APA style for use in freetext 'publications' """
    citation = '{authors} ({year}). {journal}{vol}, {pages}.'
    volume_issue = ''

    authors = data.get('dara_authors', '')
    journal_title = data['organization']['title']
    vol = data.get('dara_Publication_Volume', '')
    iss = data.get('dara_Publication_Issue', '')
    date = data.get('dara_PublicationDate', '')
    start_page = data.get('dara_Publication_StartPage', '')
    end_page = data.get('dara_Publication_EndPage', '')
    pages = '{}-{}'.format(start_page, end_page)

    authors = _parse_authors(authors)

    if vol:
        volume_issue += ", {}".format(vol)
    if iss:
        volume_issue += "({})".format(iss)

    return citation.format(authors=authors, year=date, journal=journal_title, vol=volume_issue, pages=pages)

def query_crossref(doi):
    """
        Plan to only run this if there's a DOI but the publication 
        metadata is incomplete.
    """
    base_url = "https://api.crossref.org/works/{doi}"
    
    response = requests.get(base_url.format(doi=doi))
    if response.status_code == 200:
        data = response.json()
        return data
    return False
