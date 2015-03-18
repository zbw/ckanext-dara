#Hendrik Bunke
#ZBW - Leibniz Information Centre for Economics
#2013-04-11

"""CKAN plugin for da|ra schema based metadata"""

#import logging
import ckan.plugins as plugins
import ckan.plugins.toolkit as tk
#from pylons import c
from ckan.common import c, request, response
import ckan.model as model
#from pylons import h
#from ckan.lib.navl.dictization_functions import missing, StopOnError, Invalid
from ckanext.dara.schema import DaraFields
from ckanext.dara import utils
from datetime import datetime
from hashids import Hashids
import random
from StringIO import StringIO
from datetime import datetime
import string

#XXX OrderedDict is not available in 2.6, which is the Python Version on
#CentOS...
#from collections import OrderedDict


Fields = DaraFields()
HIDDEN = Fields.hidden()
LEVEL_1 = Fields.level_1()
LEVEL_2 = Fields.level_2()
LEVEL_3 = Fields.level_3()
LEVEL_ALL = Fields.level_all()
PUBLICATION = Fields.publication_fields()
RESOURCE = Fields.resource_fields()
PREFIX = 'dara_'



def dara_debug():
    pkg_dict = dara_pkg()

    import ipdb; ipdb.set_trace()


def dara_pkg():
    """
    get package for several helper functions
    XXX DO WE REALLY NEED THIS?
    """
    
    pkg_id = tk.c.id
    try:
        pkg = tk.get_action('package_show')(None, {'id': pkg_id})
    except:
        pkg = model.Package.by_name(pkg_id)
    
    return pkg


def dara_resource():
    """
    somehow hack. c.resource doesnt return a resource when calling .../dara_xml
    """
    #XXX improve this. we should somehow be able to get the type of the context
    #(resource or package)
    if 'resource' in request.path:
        resource = tk.get_action('resource_show')(None, {'id': c.resource_id})
    else:
        resource = c.resource
    #import pdb; pdb.set_trace()
    return resource
 

def dara_resource_url(url):
    """
    for development. dara does not accept localhost urls
    """
    if 'localhost' in url:
        url = url.replace('localhost', 'edawax.de')
    return url


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
    pkg = dara_pkg()
    authors = []
    try:
        for k in pkg.keys():
            if 'dara_author' in k:
                authors.append(pkg[k])

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
    pkg = dara_pkg()
    author = pkg['author']
    return utils.author_name_split(author)

def dara_additional_authors():
    """
    workaround
    """
    authors = dara_authors()
    dalist = []
    for author in authors:
        da = utils.author_name_split(author)
        dalist.append(da)
    return dalist


def dara_publications():
    """
    checks for publications
    """
    pkg = dara_pkg()
    for k in pkg.keys():
        if 'dara_Publication_' in k and pkg[k] is not u'':
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
    pkg = dara_pkg()
    auto = Fields.auto_fields(pkg)
    return auto


def create_doi(pkg_dict):
    """
    this should go in a function directly after package is created. 
    DOI would than be stored in pkg_dict and not created here. That way we 
    could use random ints. For now it only takes the pkg creation date and
    creates a unique hash of it. If there are than one uploads in one second
    and for the same journal/organization we'd have a collision. This case
    might be rare ;-)
    """
    
    prefix = u"10.2345" #XXX fake! change this. could be config
        
    #make sure we ALWAYS get the org id
    try:
        group = pkg_dict['group_id']
        data_dict = {'id': group, 'include_datasets': False}
        org = tk.get_action('organization_show')(None, data_dict)
        journal = org['name']
    except:
        journal = 'edawax'  #fallback
    
    #building a unique DOI id
    now = datetime.now()
    salt = now.strftime("%Y.%m.%d - %H:%M:%S:%f")    
    now_string = now.strftime("%y%j%H%M")
    hashids = Hashids(salt=salt)
    num = hashids.encode(int(now_string))

    doi = prefix + '/' + journal + '.' + num

    return doi


def dara_doi(pkg):
    """
    used in snippets/package_metadata_fields 
    """
    #pkg = dara_pkg()

    key = 'dara_DOI_Proposal'
    if key in pkg and pkg[key]:
        return pkg[key]
    doi = create_doi(pkg)
    return doi


def dara_resource_doiid():
    """
    Called when form for resource is edited first time
    """
    now = datetime.now()
    now_string = now.strftime("%y%j")
    salt = now.strftime("%Y.%m.%d - %H:%M:%S:%f")
    hashids = Hashids(salt=salt)
    num = hashids.encode(int(now_string))
    return num

class DaraResourcesPlugin(plugins.SingletonPlugin, tk.DefaultDatasetForm):
    """
    testing resource manipulation
    """
    plugins.implements(plugins.IResourceController, inherit=False)

    #def before_show(self):
    #    import pdb; pdb.set_trace()


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
    
   #def after_update(self, context, id):
   #    pkg = dara_pkg()
   #    import pdb; pdb.set_trace()

    def _dara_package_schema(self, schema):
        # Add our custom metadata field to the schema.


        #hidden fields
        for f in HIDDEN:
            field_name = PREFIX + f
            schema.update({
                field_name: [tk.get_validator('ignore_missing'),
                    tk.get_converter('convert_to_extras')
                ]
            })
        
        
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

        
        #hidden fields
        for f in HIDDEN:
            field_name = PREFIX + f
            schema.update({
                field_name: [
                    tk.get_converter('convert_from_extras'),
                    tk.get_validator('ignore_missing'),
                ]
            })

        
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
        return {
                'dara_md': dara_md,
                'dara_pkg': dara_pkg,
                'dara_resource': dara_resource,
                'dara_debug': dara_debug,
                'dara_c': tk.c,
                'dara_authors': dara_authors,
                'dara_publication_fields': dara_publication_fields,
                'dara_publications': dara_publications,
                'dara_level3_fields': dara_level3_fields,
                'dara_level2_fields': dara_level2_fields,
                'dara_level1_fields': dara_level1_fields,
                'dara_resource_fields': dara_resource_fields,
                'dara_auto_fields': dara_auto_fields,
                'dara_first_author': dara_first_author,
                'dara_additional_authors': dara_additional_authors,
                'dara_doi': dara_doi,
                'dara_resource_doiid' : dara_resource_doiid,
                'dara_resource_url' : dara_resource_url,
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
       #        )

        return map




