#Hendrik Bunke
#ZBW - Leibniz Information Centre for Economics

"""CKAN plugin for da|ra schema based metadata"""

#import logging
import ckan.plugins as plugins
import ckan.plugins.toolkit as tk
#from pylons import c
from ckan.common import c, request, response
import ckan.model as model
#from pylons import h
#from ckan.lib.navl.dictization_functions import missing, StopOnError, Invalid
from ckanext.dara import schema as dara_schema
from ckanext.dara import utils
from datetime import datetime
from hashids import Hashids
import random
from StringIO import StringIO
from datetime import datetime
import string

from collections import OrderedDict


def level(le, fields):
    level = lambda key: fields[key].level == le
    f = [(key,value) for key,value in fields.iteritems() if level(key)]
    return OrderedDict(f)

def adaptable(typ, fields):
    is_adaptable = lambda key: typ in fields[key].adapt
    f = [(key,value) for key,value in fields.iteritems() if is_adaptable(key)]
    return OrderedDict(f)

FIELDS = dara_schema.fields()
HIDDEN = dara_schema.hidden_fields()
LEVEL_1 = adaptable('dataset', level(1, FIELDS))
LEVEL_2 = adaptable('dataset', level(2, FIELDS))
RESOURCE = adaptable('resource', FIELDS)
RESOURCE_1 = level(1, RESOURCE)
RESOURCE_2 = level(2, RESOURCE)
PUBLICATION = dara_schema.publication_fields()
test = dara_schema.testfields()
PREFIX = 'dara_'
#import pdb; pdb.set_trace()

#TODO adapting dara_form for resources


def dara_debug():
    pkg_dict = dara_pkg()

    import ipdb; ipdb.set_trace()


def dara_auto_fields():
    pkg = dara_pkg()
    auto = dara_schema.auto_fields(pkg)
    return auto


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
    all_levels = dara_schema.all_fields()

    for key in all_levels.keys():
        d = PREFIX + key
        named_levels[d] = {'name': all_levels[key].widget['name']}
    return named_levels


def dara_authors():
    """
    return all author fields
    """
    pkg = dara_pkg()
    try:
        ## list comprehension. one-liner  but with statements
        #authors = [pkg[k] for k in pkg.keys() if 'dara_author' in k]
        
        #more functional
        author_keys = filter(lambda k: 'dara_author' in k, pkg.keys())
        authors = map(lambda key: pkg[key], author_keys)
        return authors
    except:
        return None

def dara_first_author():
    """
    workaround until we have a proper authors implementation
    """
    pkg = dara_pkg()
    return utils.author_name_split(pkg['author'])


def dara_additional_authors():
    """
    workaround
    """
    return map(lambda author: utils.author_name_split(author), dara_authors())


def dara_publications():
    """
    checks for publications
    """
    pkg = dara_pkg()
    for k in pkg.keys():
        if 'dara_Publication_' in k and pkg[k] is not u'':
            return True
    return False




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
    
   #def after_update(self, context, id):
   #    pkg = dara_pkg()
   #    import pdb; pdb.set_trace()


    def _dara_package_schema(self, schema):
        # Add our custom metadata field to the schema.
        

        def schema_update(field):
            schema.update({
                field: [tk.get_validator('ignore_missing'),
                        tk.get_converter('convert_to_extras'),
                ]
            })
        
        
        #XXX optimise!
        for key in HIDDEN:
            field = PREFIX + key
            schema_update(field)
        for key in LEVEL_1:
            field = PREFIX + key
            schema_update(field)
        for key in LEVEL_2:
            field = PREFIX + key
            schema_update(field)
        for key in PUBLICATION:
            field = PREFIX + key
            schema_update(field)
                
        #resources (NEW! in 2.3)
        #XXX optimise
        for key in RESOURCE_1:
            field = PREFIX + key
            schema['resources'].update({
                field: [ tk.get_validator('ignore_missing') ]
                })
        for key in RESOURCE_2:
            field = PREFIX + key
            schema['resources'].update({
                field: [ tk.get_validator('ignore_missing') ]
                })

        
        for n in range(2, 21):
            field = PREFIX + 'author_' + str(n)
            schema_update(field)
        
   
        # better in edawax_theme  ?
        schema.update({
            'edawax_article_url': [
                tk.get_validator('ignore_missing'),
                tk.get_converter('convert_to_extras')
            ]
        })
        
        return schema


    def show_package_schema(self):

        schema = super(DaraMetadataPlugin, self).show_package_schema()

        
        def schema_update(field):
            schema.update({
                field: [
                    tk.get_converter('convert_from_extras'),
                    tk.get_validator('ignore_missing'),
                ]
            })

        #XXX optimise!
        for key in HIDDEN:
            field = PREFIX + key
            schema_update(field)
        for key in LEVEL_1:
            field = PREFIX + key
            schema_update(field)
        for key in LEVEL_2:
            field = PREFIX + key
            schema_update(field)
        for key in PUBLICATION:
            field = PREFIX + key
            schema_update(field)
                
        #resources (NEW! in 2.3)
        #XXX optimise
        for key in RESOURCE_1:
            field = PREFIX + key
            schema['resources'].update({
                field: [ tk.get_validator('ignore_missing') ]
                })
        for key in RESOURCE_2:
            field = PREFIX + key
            schema['resources'].update({
                field: [ tk.get_validator('ignore_missing') ]
                })

       
        #authors
        for n in range(2,21):
            field = PREFIX + 'author_' + str(n)
            schema_update(field)

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
                'dara_publication_fields': PUBLICATION,
                'dara_publications': dara_publications,
                #'dara_level3_fields': dara_level3_fields,
                'dara_level2_fields': LEVEL_2,
                'dara_level1_fields': LEVEL_1,
                'dara_resource_fields': RESOURCE,
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




