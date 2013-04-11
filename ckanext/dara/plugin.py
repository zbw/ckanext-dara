#Test 
#based on ckanext/example_idatasetform
#HB 2013-04-11

import logging

import ckan.plugins as plugins
import ckan.plugins.toolkit as tk


def create_country_codes():
    '''Create country_codes vocab and tags, if they don't exist already.

    Note that you could also create the vocab and tags using CKAN's API,
    and once they are created you can edit them (e.g. to add and remove
    possible dataset country code values) using the API.

    '''
    user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
    context = {'user': user['name']}
    try:
        data = {'id': 'country_codes'}
        tk.get_action('vocabulary_show')(context, data)
        logging.info("Example genre vocabulary already exists, skipping.")
    except tk.ObjectNotFound:
        logging.info("Creating vocab 'country_codes'")
        data = {'name': 'country_codes'}
        vocab = tk.get_action('vocabulary_create')(context, data)
        for tag in (u'uk', u'ie', u'de', u'fr', u'es'):
            logging.info(
                    "Adding tag {0} to vocab 'country_codes'".format(tag))
            data = {'name': tag, 'vocabulary_id': vocab['id']}
            tk.get_action('tag_create')(context, data)


def country_codes():
    '''Return the list of country codes from the country codes vocabulary.'''
    create_country_codes()
    try:
        country_codes = tk.get_action('tag_list')(
                data_dict={'vocabulary_id': 'country_codes'})
        return country_codes
    except tk.ObjectNotFound:
        return None


class DaraMetadataPlugin(plugins.SingletonPlugin,
        tk.DefaultDatasetForm):
    '''An example IDatasetForm CKAN plugin.
    Uses a tag vocabulary to add a custom metadata field to datasets.
    '''
    plugins.implements(plugins.IConfigurer, inherit=False)
    plugins.implements(plugins.IDatasetForm, inherit=False)
    plugins.implements(plugins.ITemplateHelpers, inherit=False)


    def update_config(self, config):
        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        tk.add_template_directory(config, 'templates')

    def get_helpers(self):
        return {'country_codes': country_codes}

    def is_fallback(self):
        # Return True to register this plugin as the default handler for
        # package types not handled by any other IDatasetForm plugin.
        return True

    def package_types(self):
        # This plugin doesn't handle any special package types, it just
        # registers itself as the default (above).
        return []

    def _modify_package_schema(self, schema):
        # Add our custom country_code metadata field to the schema.
        schema.update({
                'country_code': [tk.get_validator('ignore_missing'),
                    tk.get_converter('convert_to_tags')('country_codes')]
                })
        # Add our custom_test metadata field to the schema, this one will use
        # convert_to_extras instead of convert_to_tags.

        #XXX das hier waere der Punkt fuer dara metadaten, wenn wir sie in das
        #'extra' dictionary packen wollen
        schema.update({
                'custom_text': [tk.get_validator('ignore_missing'),
                    tk.get_converter('convert_to_extras')]
                })

        schema.update({
            'dara_year' : [tk.get_validator('ignore_missing'),
                tk.get_converter('convert_to_extras')]
            })

        return schema

    def create_package_schema(self):
        schema = super(DaraMetadataPlugin, self).create_package_schema()
        schema = self._modify_package_schema(schema)
        return schema

    def update_package_schema(self):
        schema = super(DaraMetadataPlugin, self).update_package_schema()
        schema = self._modify_package_schema(schema)
        return schema

    def show_package_schema(self):
        schema = super(DaraMetadataPlugin, self).show_package_schema()

        # Don't show vocab tags mixed in with normal 'free' tags
        # (e.g. on dataset pages, or on the search page)
        schema['tags']['__extras'].append(tk.get_converter('free_tags_only'))

        # Add our custom country_code metadata field to the schema.
        schema.update({
            'country_code': [
                tk.get_converter('convert_from_tags')('country_codes'),
                tk.get_validator('ignore_missing')]
            })

        # Add our custom_text field to the dataset schema.
        schema.update({
            'custom_text': [tk.get_converter('convert_from_extras'),
                tk.get_validator('ignore_missing')]
            })

        schema.update({
            'dara:year': [tk.get_converter('convert_from_extras'),
                tk.get_validator('ignore_missing')]
            })


        return schema

