import json
import requests
from toolz.dicttoolz import get_in
from toolz.functoolz import pipe
from itertools import count

# from toolz.itertoolz import first, partition
from copy import deepcopy
# from ckan.plugins.toolkit import missing
from ckanext.dara.schema import author_fields
from ckanext.dara.ftools import list_dicter
# from datetime import datetime
# from ckan.plugins.toolkit import Invalid
# from ckan.lib.navl.dictization_functions import unflatten

error_key = '_error'


def normalize_issue_string(value):
    """ Issues are sometimes Double ('4+5'). Users tend to use different separators for
    double numbers, which is a problem for journal listings. So here we replace common
    separators with '/'."""
    return value.replace('+', '/').replace('-', '/')


def authors(key, data, errors, context):
    """
    validate, and transform author fields to JSON string and store it
    """
    # XXX Shouldn't the converter part be in converters, not in validators...?!
    if errors[key] or not isinstance(data[key], list):
        return

    def validate(authors_orig):
        authors = deepcopy(authors_orig)

        def val(a):
            if a['lastname'] == a['authorID'] == '':
                msg = u'Authors must at least provide Last Name OR Personal ID'
                a.update({error_key: msg})

            if a['authorID'] and not a['authorID_Type']:
                msg = u'Please add type of Author_ID'
                a.update({error_key: msg})

            return a

        return map(val, authors)

    def error_check(author):
        """
        only this function appends errors
        """
        if error_key in author:
            errors[key].append(author[error_key])
        return author

    def url_check(author):
        """
        sets missing http prefix for author url
        """

        if author['url']:
            if not author['url'].startswith(('http://', 'https://')):
                author['url'] = 'http://' + author['url']
        return author

    def id_check(author):
        """
        checks ID type and calls appropriate function
        """
        id_type = author['authorID_Type']
        id_value = author['authorID']
        funcs = {'ORCID': _orcid, 'GND': _ytc, 'Scopus': _ytc, 'WoS': _ytc,
                'Repec': _ytc}
        if id_type and id_value:
            return pipe(author, funcs[id_type], url_check, error_check)
        if id_value and not id_type:
            author.update({error_key: u'Please provide type of author ID'})
        return error_check(author)

    dk = map(lambda a: a.strip(), data[key])

    authors = (list_dicter(dk, [field.id for field in author_fields()]))
    data[key] = json.dumps(map(id_check, validate(authors)))


def _ytc(author_orig):
    """ yet to come """
    return author_orig


def _orcid(author_orig):
    """
    """
    # Test IDs
    # 0000-0003-3030-3021' # Meister Edawax, sandbox
    # 0000-0002-2389-8429' #sandbox Bunke
    # 000-0002-1234-5678' #fail test
    # 0000-0003-1419-2405  # Martin Fenner, public
    # 0000-0002-1516-2382 # Hendrik Bunke, public

    mapping = dict(
        firstname=['orcid-bio', 'personal-details', 'given-names', 'value'],
        lastname=['orcid-bio', 'personal-details', 'family-name', 'value'],
        url=['orcid-bio', 'researcher-urls', 'researcher-url', 0, 'url', 'value'],
        )

    def orcid_call(author_id):
        # sandbox only for development
        # orcid_base = 'http://pub.sandbox.orcid.org/v1.2'
        orcid_base = 'http://pub.orcid.org'
        headers = {'Accept': 'application/orcid+json'}
        url = '{}/{}/orcid-profile'.format(orcid_base, author_id)
        return requests.get(url, headers=headers)

    def orcid_map(k):
        return (k, get_in(mapping[k], profile, default=author_orig[k]))

    author = deepcopy(author_orig)
    req = orcid_call(author['authorID'])
    if req.status_code == 200:
        profile = req.json()['orcid-profile']
        author.update(map(orcid_map, mapping.iterkeys()))
        return author

    # TODO: more detailed error reasons
    msg = 'Personal ID {} does not seem to be a valid ORCID ID'.format(author['authorID'])
    author[error_key] = msg
    return author


def jel_convert(value, context):
    """This is rather hacky and might seem to be
    illogical. In case of more than on JEL field entry a list is returned that must
    be transformed to a string. CKAN than does some other operations (flattened
    dict) and calls this function a second time, only that this time a list is
    expected as return value. The second condition deals with that as well as with
    the case that only one field value is returned, which is a simple unicode
    string.  CKAN then later adds curly brackets (e.g. u"{A12}") and calls this
    function a second time. I couldnt find out where (and why) CKAN adds the
    brackets, so here we remove them and then return a list with one string."""
        
    if isinstance(value, list):
        return ','.join(value)
    
    if isinstance(value, basestring):
        return value.replace('{', '').replace('}', '').split(',')

    return value


