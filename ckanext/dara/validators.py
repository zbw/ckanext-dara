import json
import requests
from copy import deepcopy
# from ckan.plugins.toolkit import missing, _
from ckanext.dara.schema import author_fields
from ckanext.dara.utils import list_dicter


error_key = '_error'


def authors(key, data, errors, context):
    """
    transform author fields to JSON string and store it
    """
    # TODO make sure there's at least one author given AND each Author has
    # at least lastname or Personal ID
    # XXX Shouldn't the converter part be in converters, not in validators...?!

    if errors[key] or not isinstance(data[key], list):
        return

    def error_check(d):
        """
        only this function appends errors
        """
        if error_key in d:
            errors[key].append(d[error_key])
        return

    def id_check(author):
        """ 
        checks ID type and calls appropriate function
        """
        id_type = author['authorID_Type']
        id_value = author['authorID']
        if id_type and id_value:
            func_d = {'ORCID': _orcid}
            func = func_d[id_type]
            call = func(author)
            error_check(call)
            return call
        return author
    
    authors = list_dicter(data[key][:], [field.id for field in author_fields()])
    data[key] = json.dumps(map(lambda author: id_check(author), authors))


def _orcid(author_orig):
    """
    """
    # Test IDs
    # 0000-0003-3030-3021' # Meister Edawax, sandbox
    # 0000-0002-2389-8429' #sandbox Bunke
    # 000-0002-1234-5678' #fail test
    # 0000-0003-1419-2405  # Martin Fenner, public
    # 0000-0002-1516-2382 # Hendrik Bunke, public

    def orcid_call(author_id):
        # sandbox only for development
        # orcid_base = 'http://pub.sandbox.orcid.org/v1.2'
        orcid_base = 'http://pub.orcid.org'
        headers = {'Accept': 'application/orcid+json'}
        url = '{}/{}/orcid-profile'.format(orcid_base, author_id)
        return requests.get(url, headers=headers)
    
    # we don't want to modify the original dict. This is a functional
    # principle, but might also become handy for comparisons
    author = deepcopy(author_orig)
    
    req = orcid_call(author['authorID'])
    if req.status_code == 200:
        content = req.json()
        author['authorID_URI'] = _getkey(content, 'orcid-identifier', 'uri')
        author['firstname'] = _getkey(content, 'given-names', 'value')
        author['lastname'] = _getkey(content, 'family-name', 'value')
        researcher_urls = _getkey(content, 'researcher-urls', 'researcher-url')
        if researcher_urls:
            author['url'] = researcher_urls[0]['url']['value']
        return author
    else:
        # TODO: more detailed error reasons
        msg = 'Personal ID {} does not seem to be a valid ORCID ID'.format(author['authorID'])
        author[error_key] = msg
        return author


def _getkey(dic, key, valkey):
    """ 
    iterates over a (nested) dict and returns value for given key. key has to
    be unique. Recursion, yeah! ;-)
    """
    if key in dic:
        if dic[key]:
            return dic[key][valkey]
        return u''
    for k,v in dic.iteritems():
        if isinstance(v, dict):
            return _getkey(v, key, valkey)
            
