#Test 
#based on ckanext/example_idatasetform
#HB 2013-04-11

#import logging

import ckan.plugins as plugins
import ckan.plugins.toolkit as tk
from pylons import c
#from pylons import h
#from ckan.lib.navl.dictization_functions import missing, StopOnError, Invalid
from ckanext.dara.md_schema import level_1, level_2


###TODO write list for mandatory fields. choose the original names from dara
#schema


def dara_extras():
    """returns dara extra metadata as separate dictionary
    """
    prefix = 'dara_'
    try:
        pkg = c.pkg_dict
        extras = pkg['extras']
    
        #simplifying the pkg[extras]
        normalised_extras = {}
        for extra in extras:
            normalised_extras[extra['key']] = extra['value']
        
        #filtering dara extras
        dara_extras = {}
        for key,value in normalised_extras.items():
            if key.startswith(prefix):
                dara_extras[key] = value
        return dara_extras

    except:
        return None


def dara_md():
    """
    returns dara keys with dara names
    """
    all_levels = {}
    for key in level_1:
        d = 'dara_' + key
        all_levels[d] = {'name':level_1[key]['name']}
    for key in level_2:
        d = 'dara_' + key
        all_levels[d] = {'name':level_2[key]['name']}
    return all_levels



class DaraMetadataPlugin(plugins.SingletonPlugin, tk.DefaultDatasetForm):
    '''
    A CKAN plugin for adding da|ra metadata schema
    '''
    
    plugins.implements(plugins.IConfigurer, inherit=False)
    plugins.implements(plugins.IDatasetForm, inherit=True)
    plugins.implements(plugins.ITemplateHelpers, inherit=True)
    plugins.implements(plugins.IPackageController, inherit=True)

    ###XXX debugging methods XXX
   
   #def after_update(self,context, pkg_dict):
   #    """
   #    test
   #    """
   #    import pdb; pdb.set_trace()

   #def before_view(self, pkg_dict):
   #    dmd = dara_md
   #    import pdb; pdb.set_trace()


    def update_config(self, config):
        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        tk.add_template_directory(config, 'templates')
        tk.add_public_directory(config, 'public')
        tk.add_resource('resources', 'dara')

    def get_helpers(self):
        #return {'country_codes': country_codes}
        return {'dara_extras' : dara_extras, 'dara_md' : dara_md,}
       
        #return {}

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
       
        #mandatory fields
        for key in level_1:
            name = level_1[key]['name']
            field_name = 'dara_' + key
            schema.update({
                field_name : [
                   tk.get_validator('not_empty'),
                   tk.get_converter('convert_to_extras')
                  ]
              })


        ### optional fields ###
        #XXX very basic here. what about validation???
        for key in level_2:
            field_name = 'dara_' + key
            schema.update({
                field_name : [
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

        ###mandatory fields ###

        for key in level_1:
            name = level_1[key]['name']
            field_name = 'dara_' + key
            schema.update({
                field_name : [
                   tk.get_converter('convert_from_extras'),
                   tk.get_validator('not_empty'),
                  ]
              })


      #     'dara_year': [
      #         tk.get_converter('convert_from_extras'),
      #         tk.get_validator('not_empty'),
      #         ]
      #     })

      # schema.update({
      #     'dara_DOI': [
      #         tk.get_converter('convert_from_extras'),
      #         tk.get_validator('not_empty'),
      #         ]
      #     })

      # schema.update({
      #     'dara_availability' : [
      #         tk.get_converter('convert_from_extras'),
      #         tk.get_validator('not_empty'),
      #         ]
      #     })

        for key in level_2:
            field_name = 'dara_' + key
            schema.update({
                field_name : [
                    tk.get_converter('convert_from_extras'),
                    tk.get_validator('ignore_missing'),
                    ]
                })


       
        return schema

 
