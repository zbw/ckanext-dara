import json
import requests
from toolz.dicttoolz import get_in
from toolz.functoolz import pipe
from copy import deepcopy
# from ckan.plugins.toolkit import missing, _
from ckanext.dara.schema import author_fields
from ckanext.dara.ftools import list_dicter


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

    def error_check(author):
        """
        only this function appends errors
        """
        if error_key in author:
            errors[key].append(author[error_key])
        return author

    def id_check(author):
        """
        checks ID type and calls appropriate function
        """
        id_type = author['authorID_Type']
        id_value = author['authorID']
        if id_type and id_value:
            funcs = {'ORCID': _orcid}
            return pipe(author, funcs[id_type], error_check)
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
        profile = content['orcid-profile']  # convenience
        
        author['authorID_URI'] = get_in(['orcid-identifier', 'uri'], profile)
        author['firstname'] = get_in(['orcid-bio', 'personal-details',
                                      'given-names', 'value'], profile,
                                     default=author_orig['firstname'])
        author['lastname'] = get_in(['orcid-bio', 'personal-details',
                                     'family-name', 'value'], profile,
                                    default=author_orig['lastname'])
        author['url'] = get_in(['orcid-bio', 'researcher-urls',
                                'researcher-url', 0, 'url', 'value'], profile,
                               default=author_orig['url'])
        
        return author
    else:
        # TODO: more detailed error reasons
        msg = 'Personal ID {} does not seem to be a valid ORCID ID'.format(author['authorID'])
        author[error_key] = msg
        return author



