# DOI generation and helper methods

import ckan.plugins.toolkit as tk
from datetime import datetime
from ckan.common import config


def dara_doi(org_name, created):
    prefix = config.get('ckanext.dara.doi_prefix')
    dt = datetime.strptime(created, "%Y-%m-%dT%H:%M:%S.%f")
    timestamp = "{:%Y%j.%H%M%S}".format(dt)
    doi = u'{}/{}.{}'.format(prefix, org_name, timestamp)
    return doi


def get_journal_name(pkg):
    org_id = pkg.get('group_id', pkg.get('owner_org'))
    data_dict = {'id': org_id, 'include_datasets': False}
    org = tk.get_action('organization_show')(None, data_dict)
    return org['name']


# helpers
def res_doi(res, pkg, journal_name):
    doi = res.get('dara_DOI', None)
    if doi:
        return doi

    #pkg = tk.get_action('package_show')(None, {'id': res['package_id']})
    doi_gen = dara_doi(journal_name, res['created'])

    # necessary to append 'R' here because of different creation timestamp
    # methods for packages and resources and possible clashes. # XXX CKAN!
    # pkg['metadata_created'] uses UTC, resources['created'] local time.
    # See https://github.com/ckan/ckan/issues/2903
    # Could be upgraded later (random char, random char/number combination)
    # which might be necessary for use with API
    return "{}R".format(doi_gen)


# helpers
def pkg_doi(pkg):
    try:
        doi = pkg.get('dara_DOI', None)
        if doi:
            return doi
    except AttributeError:
        pass
    return dara_doi(get_journal_name(pkg), pkg['metadata_created'])


# helpers
def use_testserver():
    return {'true': True, 'false': False}.get(config.get('ckanext.dara.use_testserver', 'false'))



