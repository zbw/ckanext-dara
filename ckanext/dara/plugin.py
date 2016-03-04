# Hendrik Bunke
# ZBW - Leibniz Information Centre for Economics

"""CKAN plugin for da|ra schema based metadata"""

# import logging
import ckan.plugins as plugins
import ckan.plugins.toolkit as tk
# from ckan.lib.navl.dictization_functions import missing, StopOnError, Invalid
from ckanext.dara import schema as ds
from itertools import chain
from ckanext.dara import helpers
from ckanext.dara import validators
from copy import deepcopy
from datetime import datetime
from pylons import config


PREFIX = 'dara_'


def dara_fields(dara_type):
    return filter(lambda field: dara_type in field.adapt, ds.fields())


def vc(action, f_validators):
    vals = map(lambda v: tk.get_validator(v), f_validators)
    m = {'show': [tk.get_converter('convert_from_extras')] + vals,
         'update': vals + [tk.get_converter('convert_to_extras')]}
    return m[action]


def schema_update(schema, action):
    fields = chain(dara_fields('dataset'),
                dara_fields('publication'),
                ds.hidden_fields(),
                ds.single_fields())
    map(lambda f: schema.update({PREFIX + f.id: vc(action, f.validators)}), fields)
    resource_schema_update(schema)
    
    # XXX validating resource custom fields does not work in CKAN!?.
    # map(lambda f: schema['resources'].update({PREFIX + f.id: map(lambda v:
    #    tk.get_validator(v), f.validators)}), dara_fields('resource'))


def resource_schema_update(schema):
    v = [tk.get_validator('ignore_missing')]
    fields = chain(dara_fields('data'),
                dara_fields('text'),
                dara_fields('code'),
                dara_fields('other'),
                ds.hidden_fields())
    map(lambda f: schema['resources'].update({PREFIX + f.id: v}), fields)
    

def dara_package_schema(schema):
    schema_update(schema, 'update')
    return schema


def dara_doi(pkg):
    # DOI prefix must be set in CKAN config
    # TODO: catch missing config entry
    # TODO: build check if DOI already exists...? better take microseconds :-)
    prefix = config.get('ckanext.dara.doi_prefix')
    timestamp = "{:%y%j.%H%M%S}".format(datetime.utcnow())
    org_id = pkg.get('group_id', pkg.get('owner_org'))
    data_dict = {'id': org_id, 'include_datasets': False}
    org = tk.get_action('organization_show')(None, data_dict)
    journal = org['name']
    doi = u'{}/{}.{}'.format(prefix, journal, timestamp)
    return doi


class DaraMetadataPlugin(plugins.SingletonPlugin, tk.DefaultDatasetForm):
    '''
    A CKAN plugin for da|ra metadata schema. All additional functions are
    above, so this class just contains the original methods from the
    plugins interfaces
    '''
    plugins.implements(plugins.IConfigurer, inherit=False)
    # plugins.implements(plugins.IConfigurable, inherit=True)
    plugins.implements(plugins.IDatasetForm, inherit=True)
    plugins.implements(plugins.ITemplateHelpers, inherit=True)
    plugins.implements(plugins.IPackageController, inherit=True)
    plugins.implements(plugins.IRoutes, inherit=True)
    plugins.implements(plugins.IValidators)

    def show_package_schema(self):
        schema = deepcopy(super(DaraMetadataPlugin, self).show_package_schema())
        schema_update(schema, 'show')
        return schema

    def create_package_schema(self):
        schema = deepcopy(super(DaraMetadataPlugin, self).create_package_schema())
        return dara_package_schema(schema)

    def update_package_schema(self):
        schema = deepcopy(super(DaraMetadataPlugin, self).update_package_schema())
        return dara_package_schema(schema)

    def update_config(self, config):
        tk.add_template_directory(config, 'templates')
        tk.add_public_directory(config, 'public')
        tk.add_resource('resources', 'dara')

    def get_validators(self):
        return {'authors': validators.authors,
                # 'pubdate': validators.pubdate,
                # 'dara': validators.dara,
                }

   
    def get_helpers(self):
        return {
                'dara_md': helpers.dara_md,
                'dara_pkg': helpers.dara_pkg,
                'dara_resource': helpers.dara_resource,
                'dara_debug': helpers.dara_debug,
                'dara_c': tk.c,
                'dara_authors': helpers.dara_authors,
                'dara_fields': dara_fields,
                'dara_auto_fields': helpers.dara_auto_fields,
                'dara_doi': dara_doi,
                'dara_resource_url': helpers.dara_resource_url,
                'dara_author_fields': helpers.dara_author_fields,
                'check_journal_role': helpers.check_journal_role,
                'resource_is_internal': helpers.resource_is_internal
                }

    def is_fallback(self):
        # Return True to register this plugin as the default handler for
        # package types not handled by any other IDatasetForm plugin.
        return True

    def package_types(self):
        # This plugin doesn't handle any special package types, it just
        # registers itself as the default (above).
        return []

    
    def before_map(self, map):
        """
        """
        # map.connect() accepts arbitrary **kw and *args. That's why
        # we can add the template for the calls of the controller here
        
        map.connect('/dataset/{id}/dara_xml',
                controller="ckanext.dara.controller:DaraController",
                action='xml',
                template='package/collection.xml',)

        map.connect('/dataset/{id}/resource/{resource_id}/dara_xml',
                controller="ckanext.dara.controller:DaraController",
                action='xml',
                template='package/resource.xml')

        map.connect('/dataset/{id}/dara_register',
                controller="ckanext.dara.controller:DaraController",
                action="register",
                template="package/collection.xml",)

        map.connect('dara_doi', '/dataset/edit/{id}/dara_doi',
                controller="ckanext.dara.controller:DaraController",
                action="doi",
                template="package/doi.html",
                ckan_icon="exchange")

        return map


class DaraResourcesPlugin(plugins.SingletonPlugin):
    """
    Plugin for Resources Controller
    """
    # XXX we have to use this extra class for creation of DOI proposal. This is a
    # little inconsistent with the dataset generation of DOI, which is done via
    # helpers from the template. That's not possible for resources since we
    # don't get the pkg (or any other relevant data) there. On the other hand
    # there are some clashes and errors when using the after_create method with
    # the dataset also. However, both dataset and resource actually use the same
    # function for DOI generation (dara_doi()), only the calling point is
    # different

    plugins.implements(plugins.IResourceController, inherit=True)

    def after_create(self, context, resource):
        pkg_id = resource['package_id']
        pkg_dict = tk.get_action('package_show')(context, {'id': pkg_id})
        doi = dara_doi(pkg_dict)
        resource['dara_DOI_Proposal'] = doi
        tk.get_action('resource_update')(context, resource)
    
    #def before_show(self, resource_dict):
    #    import ipdb; ipdb.set_trace()



