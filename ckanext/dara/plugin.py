#Dr. Hendrik Bunke
#ZBW - Leibniz Information Centre for Economics
#2013-04-11

"""
CKAN plugin for da|ra schema based metadata
"""

#import logging
import ckan.plugins as plugins
import ckan.plugins.toolkit as tk
from pylons import c
#from pylons import h
#from ckan.lib.navl.dictization_functions import missing, StopOnError, Invalid
from ckanext.dara.md_schema import LEVEL_1, LEVEL_2, LEVEL_3, dara_all_levels


PREFIX = 'dara_'

def dara_debug():
    pkg_dict = c.pkg_dict

    import ipdb; ipdb.set_trace()

def dara_extras():
    """returns dara extra metadata as separate dictionary
    """
   
    #this does not work with ckan 2.1?
    #pkg = c.pkg_dict
    
    #this is new for 2.1
    pkg = c.pkg
    
    #an empty package returns ''
    if pkg:
        extras = pkg.extras
        

        #filtering dara extras
        dara_extras = {}
        for key, value in extras.items():
            if key.startswith(PREFIX):
                dara_extras[key] = value
        return dara_extras
    return None


def dara_pkg():
    """to avoid pkg changes by ckan
    """
    return c.pkg


def dara_c():
    return c


def dara_md():
    """
    returns dara keys with dara names
    """
    named_levels = {}
    all_levels = dara_all_levels()
    
    for key in all_levels.keys():
        d = PREFIX + key
        named_levels[d] = {'name': all_levels[key]['name']}
    return named_levels


def dara_authors():
    """
    return all author fields
    """
    extras = dara_extras()
    authors = []
    for k in extras.keys():
        if 'author' in k:
            authors.append(extras[k])

    #XXX this can only be a temporary workaround! XXX
    #when deleting a field in the form, the author extras is not removed, but
    #just empty. So we have to filter those empty strings out of here
    #return filter(None, authors)
    return authors
    






class DaraMetadataPlugin(plugins.SingletonPlugin, tk.DefaultDatasetForm):
    '''
    A CKAN plugin for da|ra metadata schema
    '''

    plugins.implements(plugins.IConfigurer, inherit=False)
    plugins.implements(plugins.IDatasetForm, inherit=True)
    plugins.implements(plugins.ITemplateHelpers, inherit=True)
    plugins.implements(plugins.IPackageController, inherit=True)

    #XXX debugging methods

    #def after_update(self,context, pkg_dict):
    #
    #     """
    #     test
    #     """
    #     import ipdb; ipdb.set_trace()


    # def before_view(self, pkg_dict):
    #       import pdb; pdb.set_trace()

    def _dara_package_schema(self, schema):
        # Add our custom metadata field to the schema.

        #mandatory fields
        for key in LEVEL_1:
            field_name = PREFIX + key
            schema.update({
                field_name: [
                    tk.get_validator('not_empty'),
                    tk.get_converter('convert_to_extras')
                ]
            })

        ## optional fields ###
        #XXX very basic here. what about validation???
        for key in LEVEL_2:
            field_name = PREFIX + key
            schema.update({
                field_name: [
                    tk.get_validator('ignore_missing'),
                    tk.get_converter('convert_to_extras')
                ]
            })

        for key in LEVEL_3:
            field_name = PREFIX + key
            schema.update({
                field_name: [
                    tk.get_validator('ignore_missing'),
                    tk.get_converter('convert_to_extras')
                ]
            })

        schema.update({
            'Counter': [
                tk.get_validator('ignore_missing'),
                tk.get_converter('convert_to_extras')
                ]
            })

        for n in range(2,21):
            field_name = PREFIX + 'author_' + str(n)
            schema.update({
                field_name: [
                tk.get_validator('ignore_missing'),
                tk.get_converter('convert_to_extras')
                ]
            })
        
        return schema

    
    def update_config(self, config):
        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        tk.add_template_directory(config, 'templates')
        tk.add_public_directory(config, 'public')
        tk.add_resource('resources', 'dara')

    def get_helpers(self):
        return {'dara_extras': dara_extras, 
                'dara_md': dara_md, 
                'dara_pkg':dara_pkg, 
                'dara_debug':dara_debug,
                'dara_c' : dara_c,
                'dara_authors' : dara_authors
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

    def show_package_schema(self):

        schema = super(DaraMetadataPlugin, self).show_package_schema()

        for key in LEVEL_1:
            field_name = PREFIX + key
            schema.update({
                field_name: [
                    tk.get_converter('convert_from_extras'),
                    tk.get_validator('not_empty'),
                ]
            })

        for key in LEVEL_2:
            field_name = PREFIX + key
            schema.update({
                field_name: [
                    tk.get_converter('convert_from_extras'),
                    tk.get_validator('ignore_missing'),
                ]
            })


        for key in LEVEL_3:
            field_name = PREFIX + key
            schema.update({
                field_name: [
                    tk.get_converter('convert_from_extras'),
                    tk.get_validator('ignore_missing'),
                ]
            })

        for n in range(2,21):
            field_name = PREFIX + 'author_' + str(n)
            schema.update({
                field_name: [
                tk.get_validator('ignore_missing'),
                tk.get_converter('convert_from_extras')
                ]
            })
        return schema
