from toolz.dicttoolz import get_in
import ckan.plugins.toolkit as tk
from pylons import config


# XXX   I haven't found a way to make the CKAN API handle custom exceptions
# properly, so we use logic.NotFound

@tk.side_effect_free
def get_by_doi(context, q):
    """return package or resource with the given DOI"""
    
    def get_package(data_dict):
        solr = tk.get_action('package_search')(None, data_dict)
        return get_doi_obj(solr, 'package_show')

    def get_resource(data_dict):
        solr = tk.get_action('resource_search')(None, data_dict)
        return get_doi_obj(solr, 'resource_show')

    def get_doi_obj(solr, action):
        count = solr.get('count', 0)
        if count == 1:
            pkg_id = get_in(['results', 0, 'id'], solr, default=None)
            return tk.get_action(action)(None, {'id': pkg_id})
        elif count > 1:
            return tk.ObjectNotFound("Found more than one object with given\
                DOI. This should not happen.")
        return

    doi = q.get('doi', None)
    if not doi:
        raise tk.ObjectNotFound("DOI not given")
    
    ts = config.get('ckanext.dara.use_testserver', 'false')
    field = {'true': 'dara_DOI_Test', 'false': 'dara_DOI'}.get(ts)
    
    search_str = u'{}:{}'.format(field, doi)
    pkg_data_dict = {'fq': search_str}
    res_data_dict = {'query': search_str}
    
    data = get_package(pkg_data_dict) or get_resource(res_data_dict) or None
   
    if not data:
        raise tk.ObjectNotFound("Object with DOI {}".format(doi))
    
    return data
    
 
