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

PREFIX = 'dara_'


def dara_fields(dara_type):
    return filter(lambda field: dara_type in field.adapt, ds.fields())


def vc(action, f_validators):
    vals = map(lambda v: tk.get_validator(v), f_validators)
    m = {'show': [tk.get_converter('convert_from_extras')] + vals,
         'update': vals + [tk.get_converter('convert_to_extras')]}
    return m[action]


def schema_update(schema, action):
    fields = chain(ds.fields(), ds.hidden_fields(), ds.single_fields())
    map(lambda f: schema.update({PREFIX + f.id: vc(action, f.validators)}), fields)
    
    # resource_schema_update(schema)
    
    # XXX validating resource fields throws errors. See https://github.com/ckan/ckan/issues/2816
    # and https://github.com/ckan/ckan/issues/2331
    # This is a long lasting CKAN Bug...
    map(lambda f: schema['resources'].update({PREFIX + f.id: map(lambda v:
        tk.get_validator(v), f.validators)}), dara_fields('resource'))


def resource_schema_update(schema):
    v = [tk.get_validator('ignore_missing')]
    map(lambda f: schema['resources'].update({PREFIX + f.id: v}), dara_fields('resource'))
    

def dara_package_schema(schema):
    schema_update(schema, 'update')
    return schema


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
    plugins.implements(plugins.IResourceController, inherit=True)
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
                'pubdate': validators.pubdate,
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
                'dara_doi': helpers.dara_doi,
                'dara_resource_doiid' : helpers.dara_resource_doiid,
                'dara_resource_url' : helpers.dara_resource_url,
                'dara_author_fields' : helpers.dara_author_fields,
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
