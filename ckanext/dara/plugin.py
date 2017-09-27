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
from ckanext.dara import validators, converters
from copy import deepcopy
from pylons import config
import doi
import mimetypes
import api



PREFIX = 'dara_'


def dara_fields(dara_type):
    return filter(lambda field: dara_type in field.adapt, ds.fields())


def vc(action, field):
    # vals = map(lambda v: tk.get_validator(v), field.validators)
    # c_show = map(lambda c: tk.get_converter(c), field.converters_show)
    # c_update = map(lambda c: tk.get_converter(c), field.converters_update)
    # m = {'show': c_show + vals,
         # 'update': vals + c_update}

    vals = map(lambda v: tk.get_validator(v), field.validators)
    m = {'show': [tk.get_converter('convert_from_extras')] + vals,
         'update': vals + [tk.get_converter('convert_to_extras')]}
    return m[action]

def schema_update(schema, action):
    fields = chain(dara_fields('dataset'),
                dara_fields('publication'),
                ds.hidden_fields(),
                ds.single_fields())
    map(lambda f: schema.update({PREFIX + f.id: vc(action, f)}), fields)
    
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
    plugins.implements(plugins.IResourceController, inherit=True)
    plugins.implements(plugins.IActions)
    


   #def before_create(self, context, resource):
   #
   #    def get_pkg():
   #        return tk.get_action('package_show')(context, {'id': context['package'].id})
   #    import ipdb; ipdb.set_trace()

    # def after_update(self, context, pkg_dict):
        # import ipdb; ipdb.set_trace()

    # def before_view(self, pkg_dict):
        # import ipdb; ipdb.set_trace()


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
        mimetypes.add_type('STATA do', '.do')
        mimetypes.add_type('STATA data', '.dta')
        mimetypes.add_type('SRC', '.src')
        mimetypes.add_type('LOG', '.log')

    def get_validators(self):
        return {'authors': validators.authors,
                'normalize_issue_string': validators.normalize_issue_string,
                'jel_convert': validators.jel_convert,
                }

    def get_actions(self):
        return {'get_by_doi': api.get_by_doi}

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
                'dara_resource_url': helpers.dara_resource_url,
                'dara_author_fields': helpers.dara_author_fields,
                'check_journal_role': helpers.check_journal_role,
                'resource_is_internal': helpers.resource_is_internal,
                'fileinfo': helpers.fileinfo,
                'res_doi': doi.res_doi,
                'pkg_doi': doi.pkg_doi,
                'dara_use_testserver': doi.use_testserver
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
