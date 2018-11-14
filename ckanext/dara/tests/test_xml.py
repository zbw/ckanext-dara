import untangle
import ckan.model as model
import ckan.plugins as plugins
import ckan.lib.search as search
import ckan.plugins.toolkit as tk
import ckan.tests.factories as factories
from ckan.tests.helpers import FunctionalTestBase, change_config, reset_db


import nose.tools as nt


def _get_package_action_page(app, package_name, action):
    # user = factories.User()
    # env = {'REMOTE_USER': user['name'].encode('ascii')}
    
    pkg_url = tk.url_for(controller='package', action="read", id=package_name)
    action_url = "{}/{}".format(pkg_url, action)

    response = app.get(
        url=action_url,
        # extra_environ=env,
    )

    return response


def _get_resource_action_page(app, package_name, resource_id, action):
    # user = factories.User()
    # env = {'REMOTE_USER': user['name'].encode('ascii')}
    
    pkg_url = tk.url_for(controller='package', action="read", id=package_name)
    action_url = "{}/resource/{}/{}".format(pkg_url, resource_id, action)

    response = app.get(
        url=action_url,
        # extra_environ=env,
    )

    return response


class TestDaraXml(FunctionalTestBase):
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
        self.test_partial = self._dara_testpackage_partialset()
        #self.resource_package = self._dara_resource_testpackage()
    
    @classmethod
    def setup_class(cls):
        super(TestDaraXml, cls).setup_class()
        plugins.load('dara')

    def teardown(self):
        #del config['ckanext.dara.use_testserver']
        model.repo.rebuild_db()

    @classmethod
    def teardown_class(cls):
        plugins.unload('dara')
        super(TestDaraXml, cls).teardown_class()
   
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

    def _dara_testpackage_partialset(self):
        pkg = factories.Dataset(
            dara_authors=['last1', 'first1', 'affil1', 'affil_id1', 'web1', 'pid1', 'GND'],
            dara_PublicationDate='2018',
            dara_currentVersion="1",
            owner_org=self.test_org_1['id'],
            dara_jda_submission_id='jda-578',
            dara_jels=["B4", "B21"],
            tags=[{"vocabulary_id": None, "state": "active", "display_name": "keyword", "id": "94f805f3-9d9e-47a7-98cc-4168ca59d54e", "name": "keyword"}, {"vocabulary_id": None, "state": "active", "display_name": "keywords", "id": "d4409c44-1fab-498b-88e1-c815578a6e23", "name": "keywords"}, {"vocabulary_id": None, "state": "active", "display_name": "nwe keyword", "id": "c0a9a259-4cd5-4076-b2f5-daa447852840", "name": "new keyword"}],
            dara_Publication_Volume='999',
            dara_Publication_StartPage='1',
            dara_Publication_EndPage='100',
            title='Partial Collection',
            name='partial-collection',
            dara_Publication_PID='10.215/125-partial',
            dara_Publication_PIDType='DOI',
        )
        return pkg

    def test_full_collection_xml(self):
        """
        test dara_xml generation and view for dataset
        """
        dataset = self.test_package
        app = self._get_test_app()
        response = _get_package_action_page(app, dataset['name'], 'dara_xml')
        nt.eq_(response.headers['Content-Type'], 'text/xml; charset=utf-8')

        obj = untangle.parse(response.body)
        nt.assert_equals(obj.resource.publicationDate.year.cdata,
                         dataset['dara_PublicationDate'])
        # check that expected tags are included
        assert "<firstName>" in response.body
        assert "<lastName>" in response.body
        assert "<personIDs>" in response.body
        assert "<personID>" in response.body
        assert "<affiliationName>" in response.body
        assert "<affiliationID>" in response.body
        assert "<dataURL>" in response.body
        assert "<publisher>" in response.body
        assert "<institutionName>" in response.body
        assert "<institutionID>" in response.body
        assert "<classifications>" in response.body
        assert "<classificationInternal>" in response.body
        assert "<publications>" in response.body
        assert "<unstructuredPublication>" in response.body
        assert "<titleName>" in response.body

        # check the content is correct and with the proper tags
        assert"<lastName>last1" in response.body
        assert"<lastName>last2" in response.body
        assert"<identifier>A3" in response.body
        assert"<identifierURI>http://d-nb.info/gnd/pid1" in response.body
        assert"<identifierURI>https://ideas.repec.org/e/pid2.html" in response.body
        assert"<freetext>last1, f., last2, f. (2018). Test Organization, 999(888), 1-100." in response.body
        assert"<ID>10.215/125-ver2" in response.body
        assert"<identifierURI>http://d-nb.info/gnd/1165319829" in response.body
        assert"<identifierURI>https://viaf.org/viaf/157505890" in response.body
        assert"<year>2018" in response.body

    def test_partial_collection_xml(self):
        """
        test dara_xml generation and view for dataset
        """
        dataset = self.test_partial
        app = self._get_test_app()
        response = _get_package_action_page(app, dataset['name'], 'dara_xml')
        nt.eq_(response.headers['Content-Type'], 'text/xml; charset=utf-8')

        obj = untangle.parse(response.body)
        nt.assert_equals(obj.resource.publicationDate.year.cdata,
                         dataset['dara_PublicationDate'])
        # check that expected tags are included
        assert "<firstName>" in response.body
        assert "<lastName>" in response.body
        assert "<personIDs>" in response.body
        assert "<personID>" in response.body
        assert "<affiliationName>" in response.body
        assert "<affiliationID>" in response.body
        assert "<dataURL>" in response.body
        assert "<publisher>" in response.body
        assert "<institutionName>" in response.body
        assert "<institutionID>" in response.body
        assert "<classifications>" in response.body
        assert "<classificationInternal>" in response.body
        assert "<publications>" in response.body
        assert "<unstructuredPublication>" in response.body
        assert "<titleName>" in response.body

        # check the content is correct and with the proper tags
        assert"<lastName>last1" in response.body
        assert"<lastName>last2" not in response.body
        assert"<identifier>A3" not in response.body
        assert"<identifierURI>http://d-nb.info/gnd/pid1" in response.body
        assert"<identifierURI>https://ideas.repec.org/e/pid2.html" not in response.body
        assert"<freetext>last1, f. (2018). Test Organization, 999, 1-100." in response.body, response.body
        assert"<ID>10.215/125-partial" in response.body
        assert"<identifierURI>http://d-nb.info/gnd/1165319829" in response.body
        assert"<identifierURI>https://viaf.org/viaf/157505890" in response.body
        assert"<year>2018" in response.body

    def test_full_resource_xml(self):
        app = self._get_test_app()
        pkg = self.test_package
        res = factories.Resource(package_id=pkg['id'], **full_resource)
        response = _get_resource_action_page(app, pkg['name'], res['id'], 'dara_xml')
        nt.eq_(response.headers['Content-Type'], 'text/xml; charset=utf-8')

        # check tags
        assert "<firstName>" in response.body
        assert "<lastName>" in response.body
        assert "<affiliationName>" in response.body
        assert "<identifierURI>" in response.body
        assert "<affiliationID>" in response.body
        assert "<institutionName>" in response.body
        assert "<doiProposal>" in response.body
        assert "<freetext>" in response.body
        assert "<geographicCoverageControlled>" in response.body
        assert "<geographicCoverageFree>" in response.body
        assert "<universe>" in response.body
        assert "<sampled>" in response.body
        assert "<temporalCoverageFormal>" in response.body
        assert "<startDate>" in response.body
        assert "<endDate>" in response.body
        assert "<date>" in response.body
        assert "<temporalCoverageFree>" in response.body
        assert "<unitType>" in response.body
        assert "<numberUnits>" in response.body
        assert "<numberVariables>" in response.body

        # check data and tags
        assert "<firstName>Matthew O." in response.body
        assert "<lastName>Jackson" in response.body
        assert "<affiliationName>Jackson State University" in response.body
        assert "<institutionName>Tony Fretton Architects" in response.body
        assert "<identifierURI>http://d-nb.info/gnd/10064214-7" in response.body
        assert "<identifierURI>http://d-nb.info/gnd/6012742-9" in response.body
        assert "<freetext>Someplace" in response.body
        assert "<freetext>Sometime" in response.body
        assert "<sampled>Der Michel" in response.body
        assert "<geographicCoverageControlled>AX" in response.body
        assert "<date>2017-01-01" in response.body, response.body
        assert "<date>2018-01-01" in response.body, response.body
        assert "<unitType>Family" in response.body
        assert "<numberVariables>20" in response.body
        assert "<numberUnits>16" in response.body

    def test_partial_resource_xml(self):
        app = self._get_test_app()
        pkg = self.test_package
        res = factories.Resource(package_id=pkg['id'], **partial_resource)
        response = _get_resource_action_page(app, pkg['name'], res['id'], 'dara_xml')
        nt.eq_(response.headers['Content-Type'], 'text/xml; charset=utf-8')

        # check tags
        assert "<firstName>" in response.body
        assert "<lastName>" in response.body
        assert "<affiliationName>" in response.body
        assert "<identifierURI>" in response.body
        assert "<affiliationID>" in response.body
        assert "<institutionName>" not in response.body
        assert "<doiProposal>" in response.body
        assert "<freetext>" in response.body
        assert "<geographicCoverageControlled>" in response.body
        assert "<geographicCoverageFree>" in response.body
        assert "<universe>" in response.body
        assert "<sampled>" in response.body
        assert "<temporalCoverageFormal>" in response.body
        assert "<startDate>" in response.body
        assert "<endDate>" in response.body
        assert "<date>" in response.body
        assert "<temporalCoverageFree>" in response.body
        assert "<unitType>" in response.body
        assert "<numberUnits>" in response.body
        assert "<numberVariables>" in response.body

        # check data and tags
        assert "<firstName>first1" in response.body
        assert "<lastName>last1" in response.body
        assert "<affiliationName>Jackson State University" not in response.body
        assert "<institutionName>Tony Fretton Architects" not in response.body
        assert "<identifierURI>http://d-nb.info/gnd/10064214-7" not in response.body
        assert "<identifierURI>http://d-nb.info/gnd/6012742-9" not in response.body
        assert"<identifierURI>http://d-nb.info/gnd/pid1" in response.body
        assert"<identifierURI>https://ideas.repec.org/e/pid2.html" in response.body
        assert "<freetext>Someplace" in response.body
        assert "<freetext>Sometime" in response.body
        assert "<sampled>Der Michel" in response.body
        assert "<geographicCoverageControlled>AX" in response.body
        assert "<date>2017-01-01" in response.body, response.body
        assert "<date>2018-01-01" in response.body, response.body
        assert "<unitType>Family" in response.body
        assert "<numberVariables>20" in response.body
        assert "<numberUnits>16" in response.body



# uses locally defined authors
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

# uses organization authors
partial_resource = {
    'dara_geographicCoverageFree': 'Someplace',
    'dara_temporalCoverageFree': 'Sometime',
    'dara_universeSampled': 'Der Michel',
    'dara_geographicCoverage': "[u'AX', u'BD']",
    'dara_temporalCoverageFormal': '2017-01-01',
    'dara_temporalCoverageFormal_end': '2018-01-01',
    'dara_unitType': 'Family',
    'dara_numberUnits': '16',
    'dara_numberVariables': '20'
}


