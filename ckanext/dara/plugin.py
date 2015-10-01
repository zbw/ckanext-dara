#Hendrik Bunke
#ZBW - Leibniz Information Centre for Economics

"""CKAN plugin for da|ra schema based metadata"""

#import logging
import ckan.plugins as plugins
import ckan.plugins.toolkit as tk
#from ckan.lib.navl.dictization_functions import missing, StopOnError, Invalid
from ckanext.dara import schema as dara_schema
#from itertools import chain
#from collections import OrderedDict
from ckanext.dara import helpers
from ckanext.dara import validators


PREFIX = 'dara_'

def dara_fields(level, dara_type):
    fields = dara_schema.fields()
    #fields = dara_schema.testfields()
    return filter(lambda field: field.level == level and dara_type in field.adapt,
            fields)


class DaraMetadataPlugin(plugins.SingletonPlugin, tk.DefaultDatasetForm):
    '''
    A CKAN plugin for da|ra metadata schema
    '''

    plugins.implements(plugins.IConfigurer, inherit=False)
    #plugins.implements(plugins.IConfigurable, inherit=True)
    plugins.implements(plugins.IDatasetForm, inherit=True)
    plugins.implements(plugins.ITemplateHelpers, inherit=True)
    plugins.implements(plugins.IPackageController, inherit=True)
    plugins.implements(plugins.IResourceController, inherit=True)
    plugins.implements(plugins.IRoutes, inherit=True)
    plugins.implements(plugins.IValidators)

   #def after_update(self, context, id):
   #    pkg = helpers.dara_pkg()
   #    import pdb; pdb.set_trace()
   #
   #def before_view(self, pkg_dict):
   #    import ipdb; ipdb.set_trace()

    def _resource_schema_update(self, schema):
        for i in dara_fields(1, 'resource') + dara_fields(2, 'resource'):
            field = PREFIX + i.id
            schema['resources'].update({
                field: [ tk.get_validator('ignore_missing'),
                    ]
        })


    def _dara_package_schema(self, schema):
        # Add our custom metadata field to the schema.


        def schema_update(key):
            field = PREFIX + key
            schema.update({
                field: [
                        tk.get_validator('ignore_missing'),
                        tk.get_converter('convert_to_extras'),
                ]
            })

         #XXX this should be removed when we have dara metadata link to article
        schema.update({
            'edawax_article_url': [
                tk.get_validator('ignore_missing'),
                tk.get_converter('convert_to_extras')
            ]
        })


        #dataset schema, level1, level2, publications
        for i in dara_schema.fields():
            schema_update(i.id)

        #resources schema (new in CKAN 2.3)
        self._resource_schema_update(schema)

       # XXX resource authors do not work for now
       #schema['resources'].update({
       #    'dara_resource_authors': [tk.get_validator('ignore_missing'),
       #                    tk.get_validator('authors'),
       #                    tk.get_converter('convert_to_extras'),
       #                    ]
       #    })


        #XXX author list with validator
        field = PREFIX + 'authors'
        schema.update({
                field: [
                        #tk.get_validator('repeating_text'),
                        tk.get_validator('ignore_missing'),
                        tk.get_validator('authors'),
                        #tk.get_validator('repeating_text_output'),
                        tk.get_converter('convert_to_extras'),
                        ]
                })




        #hidden fields
        for i in dara_schema.hidden_fields():
            schema_update(i)


        return schema


    def show_package_schema(self):

        schema = super(DaraMetadataPlugin, self).show_package_schema()

        def schema_update(key):
            field = PREFIX + key
            schema.update({
                field: [
                    #tk.get_validator('keep_extras'),
                    tk.get_converter('convert_from_extras'),
                    tk.get_validator('ignore_missing')]
            })


        schema.update({
             'edawax_article_url' : [
                tk.get_converter('convert_from_extras'),
                tk.get_validator('ignore_missing'),
             ]
        })



        #dataset
        for i in dara_schema.fields():
            schema_update(i.id)

        #resources schema (NEW! in 2.3)
        self._resource_schema_update(schema)

        #XXX resource authors not functional at the moment. debug!
        #schema['resources'].update({
        #    'dara_resource_authors': [tk.get_converter('convert_from_extras'),
        #                    tk.get_validator('ignore_missing'),
        #            ]
        #})

        #hidden fields
        for i in dara_schema.hidden_fields():
            schema_update(i)

        #author list with validator
        field = PREFIX + 'authors'
        schema.update({
                field: [tk.get_converter('convert_from_extras'),
                    tk.get_validator('ignore_missing'),
                    #tk.get_validator('repeating_text_output'),
                    #tk.get_validator('authors'),
                    #tk.get_validator('repeating_text'),
                ]
                })





        return schema



    def update_config(self, config):
        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        tk.add_template_directory(config, 'templates')
        tk.add_public_directory(config, 'public')
        tk.add_resource('resources', 'dara')
        #tk.add_resource('fanstatic', 'dara')


    def get_validators(self):
        return {
            #'repeating_text': validators.repeating_text,
            #'repeating_text_output':
            #    validators.repeating_text_output,
            'authors': validators.authors,
            }


    def get_helpers(self):
        return {
                'dara_md': helpers.dara_md,
                'dara_pkg': helpers.dara_pkg,
                'dara_resource': helpers.dara_resource,
                'dara_debug': helpers.dara_debug,
                'dara_c': tk.c,
                'dara_authors': helpers.dara_authors,
                #'dara_publication_fields': dara_schema.publication_fields(),
                'dara_publications': helpers.dara_publications,
                'dara_fields': dara_fields,
                'dara_auto_fields': helpers.dara_auto_fields,
                #'dara_first_author': helpers.dara_first_author,
                #'dara_additional_authors': helpers.dara_additional_authors,
                'dara_doi': helpers.dara_doi,
                'dara_resource_doiid' : helpers.dara_resource_doiid,
                'dara_resource_url' : helpers.dara_resource_url,
                'dara_author_fields' : helpers.dara_author_fields,
                #'get_request_params': helpers.get_request_params,
                'check_journal_role': helpers.check_journal_role,
                'get_user_id': helpers.get_user_id,
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

    def create_package_schema(self):
        schema = super(DaraMetadataPlugin, self).create_package_schema()
        schema = self._dara_package_schema(schema)
        return schema

    def update_package_schema(self):
        schema = super(DaraMetadataPlugin, self).update_package_schema()
        schema = self._dara_package_schema(schema)
        return schema


    def before_map(self, map):
        """
        """
        #XXX Note: map.connect() accepts arbitrary **kw and *args. That's why
        #we can add the template for the calls of the controller here

        map.connect('/dataset/{id}/dara_xml',
                controller="ckanext.dara.controller:DaraController",
                action='xml',
                template='package/collection.xml',
                )

        map.connect('/dataset/{id}/resource/{resource_id}/dara_xml',
                controller="ckanext.dara.controller:DaraController",
                action='xml',
                template='package/resource.xml'
                )


        map.connect('/dataset/{id}/dara_register',
                controller="ckanext.dara.controller:DaraController",
                action="register",
                template="package/collection.xml",
                )

        map.connect('dara_doi', '/dataset/edit/{id}/dara_doi',
                controller="ckanext.dara.controller:DaraController",
                action="doi",
                ckan_icon="exchange"
                )

        #XXX obsolete
       #map.connect('/dataset/{id}/doi_proposal',
       #        controller="ckanext.dara.controller:DaraController",
       #        action="doi_proposal"
       #        )nse

        return map
