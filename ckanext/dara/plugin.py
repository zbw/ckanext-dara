#Dr. Hendrik Bunke
#ZBW - Leibniz Information Centre for Economics
#2013-04-11

"""CKAN plugin for da|ra schema based metadata"""

#import logging
import ckan.plugins as plugins
import ckan.plugins.toolkit as tk
#from pylons import c
from ckan.common import c
import ckan.model as model
#from pylons import h
#from ckan.lib.navl.dictization_functions import missing, StopOnError, Invalid
from ckanext.dara.schema import DaraFields
from ckanext.dara import utils
#from ckanext.dara.test_xml import xml
from datetime import datetime
from hashids import Hashids
import random
from StringIO import StringIO


#XXX OrderedDict is not available in 2.6, which is the Python Version on
#CentOS...
#from collections import OrderedDict


###TODO dara auto fields als helper methode uebergeben und fertig ;-)


Fields = DaraFields()
LEVEL_1 = Fields.level_1()
LEVEL_2 = Fields.level_2()
LEVEL_3 = Fields.level_3()
LEVEL_ALL = Fields.level_all()
PUBLICATION = Fields.publication_fields()
RESOURCE = Fields.resource_fields()
PREFIX = 'dara_'



def dara_validate(xml):
    v = utils.DaraValidation()
    val = v.validate(xml)
    return val


def _get_pkg():
    """
    """
    #this does not work with ckan 2.1?
    #pkg = c.pkg_dict
    
    #XXX from 2.2 on there's no pkg in c!
    #this was new for 2.1
    #pkg = c.pkg

    #this is new for 2.2
    #XXX can we import pkg without calling the model?

    pkg_id = tk.c.id
    pkg = model.Package.by_name(pkg_id)
    return pkg


def dara_debug():
    #pkg_dict = c.pkg_dict

    import pdb; pdb.set_trace()


def dara_extras():
    """returns dara extra metadata as separate dictionary
    """

    pkg = _get_pkg()
    #an empty package returns ''
    if pkg:
        extras = pkg.extras


        #filtering dara extras
        dara_extras = {}
        for key, value in extras.items():
            if key.startswith(PREFIX):
                dara_extras[key] = value
        #XXX sorting is still to be done. this is way it does not work exactly.
        # we'll need the dara_md['name'] as key!
        #ordered_dara_extras = OrderedDict(sorted(dara_extras.items()))
        #return ordered_dara_extras
        return dara_extras
    return None


def package_extras():
    """
    """
    pkg = _get_pkg()
    if pkg:
        extras = pkg.extras
        return extras
    return None


def dara_pkg():
    """to avoid pkg changes by ckan
    """
    return _get_pkg()


def dara_md():
    """
    returns dara keys with dara names
    """
    named_levels = {}
    all_levels = LEVEL_ALL

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
    try:
        for k in extras.keys():
            if 'author' in k:
                authors.append(extras[k])

    #XXX this can only be a temporary workaround! XXX
    #when deleting a field in the form, the author extras is not removed, but
    #just empty. So we have to filter those empty strings out of here
    #return filter(None, authors)
        return authors
    except:
        return None

def dara_first_author():
    """
    workaround until we have a proper authors implementation
    """
    pkg = _get_pkg()
    author = pkg.author
    return utils.author_name_split(author)


def dara_publications():
    """
    checks for publications
    """
    extras = dara_extras()
    for k in extras.keys():
        if 'dara_Publication_' in k and extras[k] is not u'':
            return True
    return False


def dara_publication_fields():
    """
    returns fields for related publications forms
    """
    
    fields = PUBLICATION

    return fields


def dara_level3_fields():
    """
    """
    fields = LEVEL_3
    return fields

def dara_level2_fields():
    """
    """
    fields = LEVEL_2
    return fields

def dara_level1_fields():
    return LEVEL_1

def dara_resource_fields():
    return RESOURCE


def dara_auto_fields():
    pkg = _get_pkg()
    auto = Fields.auto_fields(pkg)
    return auto


def dara_doi():
    """
    this should go in a function directly after package is created. 
    DOI would than be stored in pkg_dict and not created here. That way we 
    could use random ints. For now it only takes the pkg creation date and
    creates a unique hash of it. If there are than one uploads in one second
    and for the same journal/organization we'd have a collision. This case
    might be rare ;-)
    """
    
    prefix = u"10.2345" #XXX fake! change this. could be config
    cpkg = tk.c.pkg_dict
    org = cpkg['organization']
    journal = org['name']
    hashids = Hashids()
    created = cpkg['metadata_created'] #date string
    dt = datetime.strptime(created, "%Y-%m-%dT%H:%M:%S.%f") #object
    datestring = dt.strftime("%Y%m%d%H%M%S")
    
    ###XXX only use random int when doi is created and stored directly after
    #package creation
    #numrange = range(0,100) #twodigit
    #rd_num = random.choice(numrange)
    #date  = datestring + str(rd_num)
    
    date = int(datestring)
    num = hashids.encrypt(date)

    doi = prefix + '/' + journal + '.' + num
    return doi
    







class DaraResourcesPlugin(plugins.SingletonPlugin, tk.DefaultDatasetForm):
    """
    testing resource manipulation
    """
    plugins.implements(plugins.IResourceController, inherit=False)

    def before_show(self):
        import pdb; pdb.set_trace()


class DaraMetadataPlugin(plugins.SingletonPlugin, tk.DefaultDatasetForm):
    '''
    A CKAN plugin for da|ra metadata schema
    '''

    plugins.implements(plugins.IConfigurer, inherit=False)
    plugins.implements(plugins.IDatasetForm, inherit=True)
    plugins.implements(plugins.ITemplateHelpers, inherit=True)
    plugins.implements(plugins.IPackageController, inherit=True)
    plugins.implements(plugins.IResourceController, inherit=True)
    plugins.implements(plugins.IRoutes, inherit=True)



    #XXX debugging methods

    #def after_update(self,context, pkg_dict):
    #     """
    #     test
    #     """
    #     import ipdb; ipdb.set_trace()


    # def before_view(self, pkg_dict):
    #       import pdb; pdb.set_trace()
    


    #def before_show(self, resource_dict):
    #    import pdb; pdb.set_trace()
    #    return resource_dict


    def _dara_package_schema(self, schema):
        # Add our custom metadata field to the schema.

        #mandatory fields
        for key in LEVEL_1:
            field_name = PREFIX + key
            schema.update({
                field_name: [
                    tk.get_validator('ignore_missing'),
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

        # schema.update({
        #     'Counter': [
        #         tk.get_validator('ignore_missing'),
        #         tk.get_converter('convert_to_extras')
        #         ]
        #     })

        for n in range(2, 21):
            field_name = PREFIX + 'author_' + str(n)
            schema.update({
                field_name: [
                    tk.get_validator('ignore_missing'),
                    tk.get_converter('convert_to_extras')
                ]
            })

        #publications
        # for now we support only ONE publication per dataset. Again, the flat
        # structure of CKANs extras is a pain in the ass here
        #for n in range(1,11):
        for key in PUBLICATION:
            field_name = PREFIX + key
            schema.update({
                field_name: [
                tk.get_validator('ignore_missing'),
                tk.get_converter('convert_to_extras')
                ]   
            })

        # better in edawax_theme?
        schema.update({
            'edawax_article_url': [
                tk.get_validator('ignore_missing'),
                tk.get_converter('convert_to_extras')
            ]
        })

        
        return schema


    def show_package_schema(self):

        schema = super(DaraMetadataPlugin, self).show_package_schema()

        for key in LEVEL_1:
            field_name = PREFIX + key
            schema.update({
                field_name: [
                    tk.get_converter('convert_from_extras'),
                    tk.get_validator('ignore_missing'),
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

        #authors
        for n in range(2,21):
            field_name = PREFIX + 'author_' + str(n)
            schema.update({
                field_name: [
                tk.get_converter('convert_from_extras'),
                tk.get_validator('ignore_missing')
                ]
            })
        
        #publications
        #publications
        # for now we support only ONE publication per dataset. Again, the flat
        # structure of CKANs extras is a pain in the ass here
        #for n in range(1,11):
        for key in PUBLICATION:
            field_name = PREFIX + key
            schema.update({
                field_name: [
                tk.get_converter('convert_from_extras'),
                tk.get_validator('ignore_missing')
                ]   
            })



        schema.update({
             'edawax_article_url' : [
                tk.get_converter('convert_from_extras'),
                tk.get_validator('ignore_missing'),
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
                'dara_pkg': dara_pkg,
                'dara_debug': dara_debug,
                'dara_c': tk.c,
                'dara_authors': dara_authors,
                'package_extras': package_extras,
                'dara_publication_fields': dara_publication_fields,
                'dara_publications': dara_publications,
                'dara_level3_fields': dara_level3_fields,
                'dara_level2_fields': dara_level2_fields,
                'dara_level1_fields': dara_level1_fields,
                'dara_resource_fields': dara_resource_fields,
                'dara_auto_fields': dara_auto_fields,
                'dara_first_author': dara_first_author,
                'dara_doi': dara_doi,
                'dara_validate': dara_validate,
                
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
        map.connect('/dataset/{id}/dara_xml', 
                controller="ckanext.dara.controller:DaraController",
                action='xml',
                )
        
        map.connect('/dataset/{id}/dara_register',
                controller="ckanext.dara.controller:DaraController",
                action="register",
                )

        map.connect('dara_doi', '/dataset/edit/{id}/dara_doi',
                controller="ckanext.dara.controller:DaraController",
                action="doi",
                ckan_icon="exchange"
                )


        return map






















