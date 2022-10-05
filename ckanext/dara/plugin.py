# Hendrik Bunke
# ZBW - Leibniz Information Centre for Economics

"""CKAN plugin for da|ra schema based metadata"""

# import logging
import ckan.plugins as plugins
import ckan.plugins.toolkit as tk
import ckan.lib.helpers as h
# from ckan.lib.navl.dictization_functions import missing, StopOnError, Invalid
from ckanext.dara import schema as ds
from itertools import chain
from ckanext.dara import helpers
from ckanext.dara import validators, converters
from copy import deepcopy
from ckan.common import config
import ckanext.dara.doi as doi
import mimetypes
import ckanext.dara.api as api
from ckan.logic.action.create import resource_create as ckan_resource_create
from ckan.logic.action.create import package_create as ckan_package_create
from ckan.logic.action.update import package_update as ckan_package_update
from ckanext.edawax.helpers import is_author

from flask import Blueprint

PREFIX = 'dara_'


def feedback_resource_create(context, data_dict):
    """
    Provide the user feedback when they are adding resources
    """
    resource = ckan_resource_create(context, data_dict)
    h.flash_success(f"The file \"{resource['name']}\" was added to the dataset.")
    return resource


def feedback_package_update(context, data_dict):
    """
    Provide the user feedback when creating the package
    """
    package = ckan_package_update(context, data_dict)
    # t
    if context.get('allow_state_change', False) \
        and package['state'] == 'active' \
            and package['dara_edawax_review'] == 'false':
        helpers.flash_html('Dataset Created. Uploaded files can be seen under \
                            "Data and Resources." <br> To send your data to the \
                            "editorial office, please press the “Send to Journal” button')

    return package

def dara_fields(dara_type):
    return filter(lambda field: dara_type in field.adapt, ds.fields())


def vc(action, field):
    # vals = map(lambda v: tk.get_validator(v), field.validators)
    # c_show = map(lambda c: tk.get_converter(c), field.converters_show)
    # c_update = map(lambda c: tk.get_converter(c), field.converters_update)
    # m = {'show': c_show + vals,
    # 'update': vals + c_update}
    vals = list(map(lambda v: tk.get_validator(v), field.validators))
    m = {'show': [tk.get_converter('convert_from_extras')] + vals,
         'update': vals + [tk.get_converter('convert_to_extras')]}
    return m[action]


def schema_update(schema, action):
    fields = chain(dara_fields('dataset'),
                dara_fields('publication'),
                ds.hidden_fields(),
                ds.single_fields())

    #map(lambda f: schema.update({PREFIX + f.id: vc(action, f)}), fields)
    for f in fields:
        schema.update({PREFIX + f.id: vc(action, f)})

    resource_schema_update(schema, action)


def resource_schema_update(schema, action):
    v = [tk.get_validator('ignore_missing')]
    fields = chain(dara_fields('data'),
                dara_fields('text'),
                dara_fields('code'),
                dara_fields('other'),
                ds.hidden_fields())

    for f in fields:
        schema['resources'].update({PREFIX + f.id: v})


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
    plugins.implements(plugins.IBlueprint)


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
        tk.add_resource('assets', 'dara')
        mimetypes.add_type('STATA do', '.do')
        mimetypes.add_type('STATA data', '.dta')
        mimetypes.add_type('SRC', '.src')
        mimetypes.add_type('LOG', '.log')
        mimetypes.add_type('SPS', '.sps')
        mimetypes.add_type('R', '.r')

    def get_validators(self):
        return {'authors': validators.authors,
                'normalize_issue_string': validators.normalize_issue_string,
                'jel_convert': validators.jel_convert,
                'dates': validators.dates,
                'dara_doi_validator': validators.dara_doi_validator,
                }

    def get_actions(self):
        # Package_create - triggers when first page is completed
        return {
                    'get_by_doi': api.get_by_doi,
                    'xml_show': api.xml_show,
                    'resource_create': feedback_resource_create,
                    'package_update': feedback_package_update,
               }

    def get_helpers(self):
        return {
                'dara_md': helpers.dara_md,
                'dara_pkg': helpers.dara_pkg,
                'dara_resource': helpers.dara_resource,
                'dara_debug': helpers.dara_debug,
                'dara_authors': helpers.dara_authors,
                'dara_fields': dara_fields,
                'dara_auto_fields': helpers.dara_auto_fields,
                'dara_resource_url': helpers.dara_resource_url,
                'dara_author_fields': helpers.dara_author_fields,
                'resource_author_fields': helpers.resource_author_fields,
                'check_journal_role': helpers.check_journal_role,
                'resource_is_internal': helpers.resource_is_internal,
                'fileinfo': helpers.fileinfo,
                'res_doi': doi.res_doi,
                'pkg_doi': doi.pkg_doi,
                'dara_use_testserver': doi.use_testserver,
                'av_transform': helpers.av_transform,
                'unit_type_transform': helpers.unit_type_transform,
                'org_extra_info': helpers.org_extra_info,
                'resource_type': helpers.resource_type,
                'build_citation': helpers.build_citation,
                'get_journal_name': doi.get_journal_name,
                #'has_doi': helpers.has_doi,
                }

    def is_fallback(self):
        # Return True to register this plugin as the default handler for
        # package types not handled by any other IDatasetForm plugin.
        return True

    def package_types(self):
        # This plugin doesn't handle any special package types, it just
        # registers itself as the default (above).
        return []


    def get_blueprint(self):
        import ckanext.dara.views as views

        dara = Blueprint(u'dara', self.__module__, url_prefix=u"/dataset")

        dara.add_url_rule(u'/<id>/dara_xml',
                          view_func=views.xml,
                          methods=['GET', 'POST'])
        dara.add_url_rule(u'/<id>/resource/<resource_id>/dara_xml',
                           view_func=views.xml,
                           methods=[u'GET', u'POST'])
        dara.add_url_rule(u'/<id>/resource/<resource_id>/dara_xml',
                          view_func=views.xml,
                          methods=['GET', 'POST'])
        dara.add_url_rule(u'/<id>/dara_register',
                          view_func=views.register,
                          methods=['GET', 'POST'])
        dara.add_url_rule(u'/edit/<id>/dara_doi',
                          view_func=views.doi,
                          methods=['GET', 'POST'])
        dara.add_url_rule(u'/<id>/resource/<resource_id>/download/<filename>',
                          view_func=views.resource_download,
                          methods=['GET', 'POST'])
        dara.add_url_rule(u'/<pkg_id>/state',
                          view_func=views.cancel,
                          methods=['GET', 'POST'])

        return dara
