#Test 
#based on ckanext/example_idatasetform
#HB 2013-04-11

#import logging

import ckan.plugins as plugins
import ckan.plugins.toolkit as tk

class DaraMetadataPlugin(plugins.SingletonPlugin,
        tk.DefaultDatasetForm):
    '''
    A CKAN plugin for adding da|ra metadata schema
    '''
    
    plugins.implements(plugins.IConfigurer, inherit=False)
    plugins.implements(plugins.IDatasetForm, inherit=False)
    plugins.implements(plugins.ITemplateHelpers, inherit=False)

    
    def update_config(self, config):
        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        tk.add_template_directory(config, 'templates')

    def get_helpers(self):
        #return {'country_codes': country_codes}
        return {}

    def is_fallback(self):
        # Return True to register this plugin as the default handler for
        # package types not handled by any other IDatasetForm plugin.
        return True

    def package_types(self):
        # This plugin doesn't handle any special package types, it just
        # registers itself as the default (above).
        return []

    def _dara_package_schema(self, schema):
        # Add our custom metadata field to the schema.
       
        schema.update({
            'dara_year' : [
                tk.get_validator('ignore_missing'),
                tk.get_converter('convert_to_extras')
                ]
            })

        schema.update({
               'dara_resourceType': [
                   tk.get_validator('ignore_missing'),
                   tk.get_converter('convert_to_extras')
                   ]
               })

        schema.update({
            'DOI': [
                tk.get_validator('ignore_missing'),
                tk.get_converter('convert_to_extras')
                ]
            })

        schema.update({
            'dara_availability' : [
                tk.get_validator('ignore_missing'),
                tk.get_converter('convert_to_extras')
                ]
            })
               
        return  schema
               
    def create_package_schema(self):
        schema = super(DaraMetadataPlugin, self).create_package_schema()
        schema = self._dara_package_schema(schema)
        return schema

    
    def update_package_schema(self):
        schema = super(DaraMetadataPlugin, self).update_package_schema()
        schema = self._dara_package_schema(schema)
        return schema

    def show_package_schema(self):
        schema = super(DaraMetadataPlugin, self).show_package_schema()

        # Don't show vocab tags mixed in with normal 'free' tags
        # (e.g. on dataset pages, or on the search page)
        schema['tags']['__extras'].append(tk.get_converter('free_tags_only'))

        
        schema.update({
               'dara_resourceType': [
                   tk.get_validator('ignore_missing'),
                   tk.get_converter('convert_from_extras')
                   ]
               })

        schema.update({
            'dara_year': [
                tk.get_converter('convert_from_extras'),
                tk.get_validator('ignore_missing')
                ]
            })

        schema.update({
            'DOI': [
                tk.get_converter('convert_from_extras'),
                tk.get_validator('ignore_missing')
                ]
            })


        return schema



### example code ###

#def create_country_codes():
#   '''Create country_codes vocab and tags, if they don't exist already.

#   Note that you could also create the vocab and tags using CKAN's API,
#   and once they are created you can edit them (e.g. to add and remove
#   possible dataset country code values) using the API.

#   '''
#   user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
#   context = {'user': user['name']}
#   try:
#       data = {'id': 'country_codes'}
#       tk.get_action('vocabulary_show')(context, data)
#       logging.info("Example genre vocabulary already exists, skipping.")
#   except tk.ObjectNotFound:
#       logging.info("Creating vocab 'country_codes'")
#       data = {'name': 'country_codes'}
#       vocab = tk.get_action('vocabulary_create')(context, data)
#       for tag in (u'uk', u'ie', u'de', u'fr', u'es'):
#           logging.info(
#                   "Adding tag {0} to vocab 'country_codes'".format(tag))
#           data = {'name': tag, 'vocabulary_id': vocab['id']}
#           tk.get_action('tag_create')(context, data)


#def country_codes():
#   '''Return the list of country codes from the country codes vocabulary.'''
#   create_country_codes()
#   try:
#       country_codes = tk.get_action('tag_list')(
#               data_dict={'vocabulary_id': 'country_codes'})
#       return country_codes
#   except tk.ObjectNotFound:
#       return None


