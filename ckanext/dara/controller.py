#Hendrik Bunke
#ZBW - Leibniz Information Centre for Economics


from ckan.controllers.package import PackageController
import ckan.plugins.toolkit as tk
from ckan.common import c, request, response
from ckan import model
from StringIO import StringIO
from ckanext.dara.dara_schema_3 import schema
from lxml import etree
from darapi import DaraClient


#XXX this might also be sufficient for dara submission, e.g. we would not need
#an URL call

class DaraController(PackageController):
    """
    displays and validates dara XML for the dataset or resource, and registers
    it at da|ra
    """

    def __init__(self):
        self.schema = schema

    def xml(self, id):
        """
        returning dara xml
        """
        
        response.headers['Content-Type'] = "text/xml; charset=utf-8"

        context = {'model': model, 'session': model.Session,
                   'user': c.user or c.author, 'for_view': True,
                   'auth_user_obj': c.userobj}
        data_dict = {'id': id}


       ## check if package exists
        try:
            c.pkg_dict = tk.get_action('package_show')(context, data_dict)
            c.pkg = context['package']
        except tk.NotFound:
            tk.abort(404, 'Dataset not found')
        except tk.NotAuthorized:
            tk.abort(401, 'Unauthorized to read package %s' % id)

        template = "package/read.xml"
        xml_string = tk.render(template)

        #validate before show. Errors are caught by lxml
        #XXX perhaps it makes more sense to validate later in the process (before
        #submitting to dara, for example)
        self._validate(xml_string)

        return xml_string
    

    def _validate(self, xmlstring):
        """
        validate against dara schema
        
        """
        #print "Validating..."
        xml = StringIO(xmlstring)
        xsd = StringIO(self.schema)
        xmlschema_doc = etree.parse(xsd)
        xmlschema = etree.XMLSchema(xmlschema_doc)
        doc = etree.parse(xml)
        xmlschema.assertValid(doc)

    
    def register(self, id):
        """
        register at da|ra
        """
        #XXX darapi is so small, it should be integrated into ckanext-dara
        xml = self.xml(id)
        
        dara = DaraClient('demo', 'testdemo', xml, test=True, register=False)
        dara = dara.calldara()
        

        return dara
        
    
    def doi(self, id):
        """
        DOI manager page
        """

        context = {'model': model, 'session': model.Session,
                   'user': c.user or c.author, 'for_view': True,
                   'auth_user_obj': c.userobj}
        data_dict = {'id': id}


       ## check if package exists
        try:
            c.pkg_dict = tk.get_action('package_show')(context, data_dict)
            c.pkg = context['package']
        except tk.NotFound:
            tk.abort(404, 'Dataset not found')
        except tk.NotAuthorized:
            tk.abort(401, 'Unauthorized to read package %s' % id)

        template = "package/dara.html"
        page = tk.render(template)

        return page

