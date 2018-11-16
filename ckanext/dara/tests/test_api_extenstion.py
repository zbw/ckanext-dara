import json
import untangle
import ckan.model as model
from routes import url_for
import ckan.plugins as plugins
import ckan.lib.search as search
import ckan.plugins.toolkit as tk
import ckan.tests.factories as factories
from ckan.tests.helpers import FunctionalTestBase, change_config, reset_db


import nose.tools as nt


class TestDaraApiExtension(FunctionalTestBase):
    def setup(self):
        """
        Create users and organizations
        """
        reset_db()
        search.clear()
        
        self.sysadmin = factories.Sysadmin()
        self.test_member_1 = factories.User()
        self.test_member_2 = factories.User()
        self.test_editor = factories.User()

        users = [{'name': self.test_member_1['name'], 'capacity': 'member'},
                 {'name': self.test_member_2['name'], 'capacity': 'member'},
                 {'name': self.test_editor['name'], 'capacity': 'editor'}]

        self.test_org_1 = factories.Organization(users=users,
            name="testjournal")
        self.test_org_2 = factories.Organization()
        self.test_package = self._dara_testpackage_fullset()
        #self.resource_package = self._dara_resource_testpackage()
    
    @classmethod
    def setup_class(cls):
        super(TestDaraApiExtension, cls).setup_class()
        plugins.load('dara')

    def teardown(self):
        #del config['ckanext.dara.use_testserver']
        model.repo.rebuild_db()

    @classmethod
    def teardown_class(cls):
        plugins.unload('dara')
        super(TestDaraApiExtension, cls).teardown_class()
   
    def _dara_testpackage_fullset(self):
        pkg = factories.Dataset(
            dara_authors=['last1', 'first1', 'affil1', 'affil_id1', 'web1', 'pid1', 'GND', 'last2', 'first2', 'affil2', 'affil_id2', 'web2', 'pid2', 'Repec'],
            dara_PublicationDate='2018',
            dara_currentVersion="1",
            owner_org=self.test_org_1['id'],
            dara_jda_submission_id='jda-578',
            dara_jels=["A3", "B4", "B21"],
            tags=[{"vocabulary_id": None, "state": "active", "display_name": "keyword", "id": "94f805f3-9d9e-47a7-98cc-4168ca59d54e", "name": "keyword"}, {"vocabulary_id": None, "state": "active", "display_name": "keywords", "id": "d4409c44-1fab-498b-88e1-c815578a6e23", "name": "keywords"}, {"vocabulary_id": None, "state": "active", "display_name": "nwe keyword", "id": "c0a9a259-4cd5-4076-b2f5-daa447852840", "name": "new keyword"}],
            dara_Publication_Issue='888',
            dara_Publication_Volume='999',
            dara_Publication_StartPage='1',
            dara_Publication_EndPage='100',
            title='Test Collection',
            name='test-collection',
            dara_Publication_PID='10.215/125-ver2',
            dara_Publication_PIDType='DOI',
        )
        return pkg

    def test_collection_api(self):
        dataset = self.test_package
        app = self._get_test_app()
        id_ = dataset['id']
        name = dataset['name']
        #r = tk.get_action('xml_show')({'id': name})
        url = '/api/3/action/xml_show?id={id}'
        response = app.get(
                            url=url.format(id=id_)
                          )
        assert "resource was found" in response.body

    def test_resource_api(self):
        app = self._get_test_app()
        pkg = self.test_package
        res = factories.Resource(package_id=pkg['id'], **full_resource)
        pkg_id = res['package_id']
        res_id = res['id']
        #r = tk.get_action('xml_show')({'id': res_id})
        url = '/api/3/action/xml_show?id={id}'
        response = app.get(
                            url=url.format(id=res_id)
                          )
        assert "resource was found" in response.body

    def test_resource_api_fail(self):
        app = self._get_test_app()
        pkg = self.test_package
        res = factories.Resource(package_id=pkg['id'], **full_resource)
        pkg_id = res['package_id']
        res_id = res['id']
        #r = tk.get_action('xml_show')({'id': res_id})
        url = '/api/3/action/xml_show?id={id}'
        response = app.get(url=url.format(id='fail'))
        data = json.loads(response.body)
        assert data['result'] == "Unable to generate XML.", data


full_resource = {
    'dara_authors': "[u'Jackson', u'Matthew O.', u'Jackson State University', u'129605522', u'10064214-7', u'', u'', u'Tony Fretton Architects', u'', u'6012742-9']",
    'dara_geographicCoverageFree': 'Someplace',
    'dara_temporalCoverageFree': 'Sometime',
    'dara_universeSampled': "Der Michel",
    'dara_geographicCoverage': "[u'AX', u'BD']",
    'dara_temporalCoverageFormal': '2017-01-01',
    'dara_temporalCoverageFormal_end': '2018-01-01',
    'dara_unitType': 'Family',
    'dara_numberVariables': '20',
    'dara_numberUnits': '16'
}

