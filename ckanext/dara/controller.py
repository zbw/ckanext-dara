#Hendrik Bunke
#ZBW - Leibniz Information Centre for Economics


from ckan.controllers.package import PackageController
import ckan.plugins.toolkit as tk
from ckan.common import c, request, response
from ckan import model
import ckan.lib.helpers as h
from StringIO import StringIO
from lxml import etree
from darapi import DaraClient
from datetime import datetime
from hashids import Hashids
import random
from ckanext.dara.dara_schema_3_1 import schema

NotAuthorized = tk.NotAuthorized



class DaraController(PackageController):
    """
    displays and validates dara XML for the dataset or resource, and registers
    it at da|ra
    """
    

    def __init__(self):
        self.schema = schema
        ## using tk.c as context does not work here
    
    
    def __context(self):
        return {'model': model, 'session': model.Session,
            'user': c.user or c.author, 'for_view': True,
            'auth_user_obj': c.userobj}
    
    def __check_access(self, id):
        context = self.__context()
        try:
            tk.check_access('package_update', context, {'id': id})
        except NotAuthorized:
            tk.abort(401, 'Unauthorized to manage DOI.')
    
    def __params(self):
        """
        test for parameters. For testserver DOI registration is not possible,
        so we fake it (test_register)
        defaults: register at 'real' server and get a DOI
        """

        params = tk.request.params
        
        #default
        test = False
        register = True
        test_register = False
        
        if 'testserver' in params:
            test = True
        if not 'DOI' in params:
            register = False
        if test and register:
            register = False
            test_register = True

        return {'test':test, 'register':register,
                'test_register':test_register}


    def xml(self, id, template):
        """
        returning valid dara XML
        """
        response.headers['Content-Type'] = "text/xml; charset=utf-8"
        xml_string = tk.render(template)

        #validate before show. Errors are caught by lxml
        xml = StringIO(xml_string)
        xsd = StringIO(self.schema)
        xmlschema_doc = etree.parse(xsd)
        xmlschema = etree.XMLSchema(xmlschema_doc)
        doc = etree.parse(xml)
        xmlschema.assertValid(doc)

        return xml_string
    
    
    def register(self, id, template):
        """
        register at da|ra
        """
        #XXX darapi is too small, should it be integrated here?
        
        self.__check_access(id)
        context = self.__context()
        data_dict = {'id': id}
                
        date = datetime.now()
        datestring = date.strftime("%Y-%m-%d-%H:%M:%S")
                
        c.pkg_dict = tk.get_action('package_show')(context, data_dict)
                
        # first register resources
        resources = c.pkg_dict['resources']
        resources_to_be_registered = filter(lambda res: res['id'] in tk.request.params,
                resources)
        for res in resources_to_be_registered:
            self.register_resource(id, res)

        #resources might have been updated so we must get the new package
        c.pkg_dict = tk.get_action('package_show')(context, data_dict)
        
        xml = self.xml(id, template)
        params = self.__params()
        dara = DaraClient('demo', 'testdemo', xml, test=params['test'],
                register=params['register'])
        dara = dara.calldara()
        
        def store():
            if params['register'] or params['test_register']:
                #XXX in case of update we might not need to store the doi...?
                c.pkg_dict['dara_DOI'] = c.pkg_dict['dara_DOI_Proposal']
            tk.get_action('package_update')(context, c.pkg_dict)

        if dara == 201:
            c.pkg_dict['dara_registered'] = datestring
            store()
            h.flash_success("Dataset successfully registered.")
        elif dara == 200:
            c.pkg_dict['dara_updated'] = datestring
            store()
            h.flash_success("Dataset successfully updated.")
        else:
            h.flash_error("ERROR! Sorry, dataset has not been registered or "
                    "updated. Please consult the logs. (%s) " %dara)

        tk.redirect_to('dara_doi', id=id)


    def register_resource(self, id, resource):
        """
        separate resource registration
        """
        self.__check_access(id)
        context = self.__context()
        resource_id = resource['id']
        params = self.__params()
        c.resource = tk.get_action('resource_show')(context, {'id':resource_id})
        xml = self.xml(id, 'package/resource.xml')
        dara = DaraClient('demo', 'testdemo', xml, test=params['test'],
                register=params['register'])
        dara = dara.calldara()
        if dara == 201 or 200:
            doi  = u'%s.%s' %(c.pkg_dict['dara_DOI_Proposal'], resource['dara_doiid']) 
            c.resource['dara_DOI'] = doi
            tk.get_action('resource_update')(context, c.resource)
        else:
            h.flash_error("ERROR! Resource %s could not be registered\
                (%s). Dataset has not been registered" %(resource_id, dara))
            tk.redirect_to('dara_doi', id=id)


    def doi(self, id):
        """
        DOI manager page
        """
        self.__check_access(id)
        context = self.__context()
        data_dict = {'id': id}
        
        c.pkg_dict = tk.get_action('package_show')(context, data_dict)
        c.pkg = context['package']
            
        template = "package/doi.html"
        page = tk.render(template)

        return page
    



