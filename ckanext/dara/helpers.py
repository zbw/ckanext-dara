#Hendrik Bunke
#ZBW - Leibniz Information Centre for Economics

import ckan.plugins.toolkit as tk
from ckan.common import c
from ckanext.dara import schema as dara_schema
from ckanext.dara import utils
from datetime import datetime
from hashids import Hashids
import ckan.model as model
from pylons import config
import json
import ckan.plugins.toolkit as tk


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
    
    #params = request.params
    
    return pkg

def dara_debug():
    pkg_dict = dara_pkg()

    import pdb; pdb.set_trace()

def dara_auto_fields():
    pkg = dara_pkg()
    site_url = config.get('ckan.site_url')
    
    #fallback for development
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
    #XXX improve this. we should somehow be able to get the type of the context
    #(resource or package)
    try:
       #if 'resource_edit' in request.path:
       #    resource = tk.get_action('resource_show')(None, {'id': c.resource_id})
        #else:
        resource = c.resource
        return resource
    except:
        return False


#def get_request_params():
#    import ipdb; ipdb.set_trace()
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


def dara_authors(dara_type):
    """
    return all author fields
    """
    #import pdb; pdb.set_trace()
    

   #XXX we don't have resource authors at the moment
   #if dara_type == 'dataset':
   #    pkg = dara_pkg()
   #    key = 'dara_authors'
   #if dara_type == 'res':
   #    pkg = dara_resource()
   #    key = 'dara_resource_authors'
    
    pkg = dara_pkg()
    key = 'dara_authors'

    try:
        authors = json.loads(pkg[key])
        return authors
    except:
        return None

def dara_first_author():
    """
    workaround until we have a proper authors implementation
    """
    pkg = dara_pkg()
    return utils.author_name_split(pkg['author'])


def dara_additional_authors():
    """
    workaround
    """
    return map(lambda author: utils.author_name_split(author), dara_authors())


def dara_publications():
    """
    checks for publications
    """
    pkg = dara_pkg()
    for k in pkg.keys():
        if 'dara_Publication_' in k and pkg[k] is not u'':
            return True
    return False



def dara_doi(pkg):
    """
    used in snippets/package_metadata_fields.  For now we only take the pkg
    creation date and build a unique hash out of it. If there is more than one
    upload in one second and for the same journal/organization we'd have a
    collision. This case might be rare.
    """
    
    #check if we have a DOI already
    key = 'dara_DOI_Proposal'
    if key in pkg and pkg[key]:
        return pkg[key]
    
    # DOI prefix must be set in CKAN config
    prefix = config.get('ckanext.dara.doi_prefix')
        
    #make sure we ALWAYS get an org id
    try:
        group = pkg['group_id']
        data_dict = {'id': group, 'include_datasets': False}
        org = tk.get_action('organization_show')(None, data_dict)
        journal = org['name']
    except:
        journal = 'edawax'  #fallback
    
    #building a unique DOI id
    uid = __make_uid()
    doi = '{}/{}.{}'.format(prefix, journal, uid)
    return doi


def dara_resource_doiid():
    """
    Called when form for resource is edited first time
    """
    return __make_uid()


def __make_uid():
    salt = '{:%Y.%m.%d - %H:%M:%S:%f}'.format(datetime.now())
    now = '{:%y%j}'.format(datetime.now())
    hashids = Hashids(salt=salt)
    uid = hashids.encode(int(now))
    return uid


