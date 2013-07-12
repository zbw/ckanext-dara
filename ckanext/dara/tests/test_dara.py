from ckan import plugins
from unittest import TestCase
#from pylons import h
import ckan.lib.helpers as h
from pylons import c
from ckan.lib.create_test_data import CreateTestData
import ckan.logic as logic
import ckan.model as model
import paste.fixture
from ckan.config.middleware import make_app
import pylons.config as config

class TestDaraPlugin(TestCase):

    @classmethod
    def setup_class(cls):
        # Use the entry point name of your plugin as declared
        # in your package's setup.py
        plugins.load('dara')
        wsgiapp = make_app(config['global_conf'], **config)
        cls.app = paste.fixture.TestApp(wsgiapp)
        
        # create a test data package. 
        # TODO: create package with schema and/or form
        CreateTestData.create_arbitrary(dara_testpackage)
        cls.package = model.Package.get('daratest')

    @classmethod
    def teardown_class(cls):
        plugins.reset()

    def test_dara_extras(self):
        package = self.package
        #import ipdb; ipdb.set_trace()
        assert 'dara_PublicationDate' in package.extras

    def test_dara_helpers(self):
        url = h.url_for(controller='package', action='read', id=self.package.name)
        result = self.app.get(url)



    def test_dara_extras_shown(self):
        url = h.url_for(controller='package', action='read', id=self.package.name)
        result = self.app.get(url)
        # TODO assert all given extras
        assert 'dara_PublicationDate' in result.body
        assert '2011' in result.body


dara_testpackage = [
    {'name':'daratest',
     'title':'Private Fostering',
     'notes':'Figures on children cared for and accommodated in private \
            fostering arrangements, England, Year ending 31 March 2009',
     'resources':[
        {'url':'http://www.dcsf.gov.uk/rsgateway/DB/SFR/s000859/SFR17_2009_tables.xls',
            'format':'XLS',
            'description':'December 2009 | http://www.statistics.gov.uk/hub/id/119-36345'},
        {'url':'http://www.dcsf.gov.uk/rsgateway/DB/SFR/s000860/SFR17_2009_key.doc',
            'format':'DOC',
            'description':'http://www.statistics.gov.uk/hub/id/119-34565'}],
     'url':'http://www.dcsf.gov.uk/rsgateway/DB/SFR/s000859/index.shtml',
     'author':'DCSF Data Services Group',
     'author_email':'statistics@dcsf.gsi.gov.uk',
     'license':'ukcrown',
     'tags':'children fostering',
     'extras':{
        'dara_PublicationDate':'2011',
        'dara_Availabilitycontrolled':'Download',
        'dara_OtherTitle':'Ein da|ra Test'
        }
     }
]
