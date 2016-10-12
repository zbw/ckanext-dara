# Hendrik Bunke
# ZBW - Leibniz Information Centre for Economics

import ckan.plugins.toolkit as tk
from ckan.common import c, request
from ckanext.dara import schema as dara_schema
from ckanext.dara.schema import author_fields
from ckanext.dara.ftools import list_dicter
from pylons import config
import json
from ckan.new_authz import users_role_for_group_or_org
from ckan import model


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
