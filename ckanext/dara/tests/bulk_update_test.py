import ast
import ckan
import json
import webtest
import xmltodict
import ckan.model as model
from ckan.tests import helpers
import pylons.config as config
from ckan.lib.helpers import url_for
import pylons.test, pylons, pylons.config as c, ckan.model as model, ckan.tests as tests, ckan.plugins as plugins, ckan.tests.factories as factories

import ckanext.dara.tests.data_test as rd
from ckanext.dara.controller import darapi
import ckanext.dara.controller as controller
from ckanext.dara.bulk_metadata_update import BulkUpdater

import ckan.model as model
engine = model.meta.engine

"""
    TODO:
        * checkt that XML is accurately updated, for resources
        * Add testing for da-ra API update
"""

class TestBulkUpdater(helpers.FunctionalTestBase):
    @classmethod
    def setup_class(cls):
        print('Starting class')
        super(TestBulkUpdater, cls).setup_class()


    def startup(self):
        print("Starting")
        helpers.reset_db()


    def teardown(self):
        print('Rebuilding DB')
        model.repo.rebuild_db()


    @classmethod
    def teardown_class(cls):
        print('Tearing down class')
        if plugins.plugin_loaded('edawax'):
            plugins.unload('edawax')
        if plugins.plugin_loaded('dara'):
            plugins.unload('dara')


    def _get_app(self):
        c['global_conf']['debug'] = 'true'
        app = ckan.config.middleware.make_app(c['global_conf'], **c)
        app = webtest.TestApp(app)
        if not plugins.plugin_loaded('edawax'):
            plugins.load('edawax')
        if not plugins.plugin_loaded('dara'):
            plugins.load('dara')
        return app


    def _create_package_resource(self, num_resources=1, resource=False, num_journals=1):
        user = factories.User(sysadmin=True)
        owner_org = factories.Organization(users=[{'name': user['id'], 'capacity': 'admin'}])

        datasets = []
        for _ in range(num_journals):
            datasets.append(factories.Dataset(owner_org=owner_org['id'], dara_currentVersion=1, dara_PublicationDate='2019', dara_authors=json.dumps(rd.records[_]['dara_authors'], ensure_ascii=False)))

        resources = []
        if resource:
            for _ in range(num_resources):
                resources.append(factories.Resource(package_id=datasets[0]['id'], url='http://test.link/{}'.format(_), dara_authors=rd.resources[_]))
            return datasets, resources
        return datasets


    def test_1_list_3_packages(self):
        pacakges = self._create_package_resource(num_journals=3)
        tester = BulkUpdater(self._get_app(), key='my-test-key',test=True)

        live_packages = tester.get_packages()

        assert len(live_packages) == 3, live_packages


    def test_2_get_packages(self):
        packages = self._create_package_resource(num_journals=3)
        tester = BulkUpdater(self._get_app(), key='my-test-key',test=True)

        package0 = tester.get_package(packages[0]['id'])
        package1 = tester.get_package(packages[1]['id'])
        package2 = tester.get_package(packages[2]['id'])

        assert package0 == packages[0], package0
        assert package1 == packages[1], package1
        assert package2 == packages[2], package2


    def test_3_lookup(self):
        packages = self._create_package_resource(num_journals=3)
        tester = BulkUpdater(self._get_app(), key='my-test-key',test=True)

        authors0 = json.loads(packages[0]['dara_authors'])
        authors1 = json.loads(packages[1]['dara_authors'])
        authors2 = json.loads(packages[2]['dara_authors'])

        affiliations = []
        for author in authors0:
            affil_id = tester.lookup(author['affil'])
            affiliations.append( (author['affil'], affil_id) )
        assert (u'Institut f\xfcr Weltwirtschaft', u'1007681-5') in affiliations, affiliations
        assert (u'Fake Plce', False) in affiliations, affiliations
        assert (u'Deutsche Zentralbibliothek f\xfcr Wirtschaftswissenschaften  Leibniz-Informationszentrum Wirtschaft', False) in affiliations, affiliations

        affiliations = []
        for author in authors1:
            affil_id = tester.lookup(author['affil'])
            affiliations.append( (author['affil'], affil_id) )
        assert (u'University of California Berkeley', u'2025100-2') in affiliations, affiliations
        assert (u'NoWhere', False) in affiliations, affiliations

        affiliations = []
        for author in authors2:
            affil_id = tester.lookup(author['affil'])
            affiliations.append( (author['affil'], affil_id) )
        assert (u'Federal Reserve Bank <Boston, Mass.>', u'270861-9') in affiliations, affiliations


    def test_4_update_record(self):
        packages = self._create_package_resource(num_journals=3)
        tester = BulkUpdater(self._get_app(),key='my-test-key',test=True)

        new_authors = tester.update_affil_id(packages[0]['name'])

        affiliations = []
        for author in new_authors:
            affil_id = tester.lookup(author['affil'])
            affiliations.append( (author['affil'], affil_id) )
        assert (u'Institut f\xfcr Weltwirtschaft', u'1007681-5') in affiliations, affiliations

        new_authors = tester.update_affil_id(packages[2]['name'])
        assert new_authors[0]['affilID'] == u'270861-9', new_authors


    def test_5_submit_updated_record(self):
        sysadmin = factories.Sysadmin()
        packages = self._create_package_resource(num_journals=3)
        tester = BulkUpdater(self._get_app(), key=sysadmin['apikey'],test=True)

        new_authors = tester.update_affil_id(packages[2]['name'])
        result = tester.patch_package(id=packages[2]['name'], update=new_authors)
        assert packages[2] != result, result
        assert 'dara_authors' in result.keys(), result.keys()
        assert json.loads(result['dara_authors'])[0]['affilID'] == u'270861-9', result['dara_authors'][0]['affilID']

        updated_record = tester.get_package(packages[2]['name'])
        assert '270861-9' in updated_record['dara_authors'], updated_record['dara_authors']

        assert packages[0] == tester.get_package(packages[0]['name'])

    def test_6_list_3_resources(self):
        packages,resources = self._create_package_resource(num_resources=3, resource=True)
        tester = BulkUpdater(self._get_app(), key='my-test-key',test=True)

        resources = tester.get_package(packages[0]['name'])['resources']

        assert len(resources) == 3, resources


    def test_7_get_resource(self):
        packages,resources = self._create_package_resource(num_resources=3, resource=True)
        tester = BulkUpdater(self._get_app(), key='my-test-key',test=True)

        resource = tester.get_resource(resources[0]['id'])
        assert resource == resources[0], resource
        assert 'Strickland Propane' in resource['dara_authors'], resource['dara_authors']

        resource = tester.get_resource(resources[1]['id'])
        assert resource == resources[1], resource
        assert 'Chicago Council on Foreign Relations' in resource['dara_authors'], resource['dara_authors']

        resource = tester.get_resource(resources[2]['id'])
        assert resource == resources[2], resource
        assert 'Zoologischer Garten <Frankfurt, Main>' in resource['dara_authors'], resource['dara_authors']


    def test_8_lookup_resource_aff(self):
        packages,resources = self._create_package_resource(num_resources=3, resource=True)
        tester = BulkUpdater(self._get_app(), key='my-test-key',test=True)

        authors0 = ast.literal_eval(resources[0]['dara_authors'])
        authors1 = ast.literal_eval(resources[1]['dara_authors'])
        authors2 = ast.literal_eval(resources[2]['dara_authors'])

        affiliations = []
        last = 0
        for x, author in enumerate(authors0):
            if last == 0 and x == 2:
                last = x
                affil_id = tester.lookup(author)
                affiliations.append( (author, affil_id) )
            elif x == last + 5:
                last = x
                affil_id = tester.lookup(author)
                affiliations.append( (author, affil_id) )

        assert (u'Strickland Propane', False) in affiliations, affiliations

        affiliations = []
        last = 0
        for x, author in enumerate(authors1):
            if last == 0 and x == 2:
                last = x
                affil_id = tester.lookup(author)
                affiliations.append( (author, affil_id) )
            elif x == last + 5:
                last = x
                affil_id = tester.lookup(author)
                affiliations.append( (author, affil_id) )

        assert (u'Federal Reserve Bank <Saint Louis, Mo.>', u'75261-7') in affiliations, affiliations
        assert (u'Chicago Council on Foreign Relations', u'1045637-5') in affiliations, affiliations


    def test_9_update_resource(self):
        packages,resources = self._create_package_resource(num_resources=3, resource=True)
        tester = BulkUpdater(self._get_app(), key='my-test-key',test=True)

        new_authors = tester.update_affil_resource(resources[1]['id'])

        assert u'1045637-5' in new_authors, new_authors
        assert u'75261-7' in new_authors, new_authors


    def test_91_submit_updated_resource(self):
        sysadmin = factories.Sysadmin()
        packages,resources = self._create_package_resource(num_resources=3, resource=True)
        tester = BulkUpdater(self._get_app(), key=sysadmin['apikey'],test=True)

        new_authors = tester.update_affil_resource(resources[1]['id'])
        result = tester.patch_resource(id=resources[1]['id'],update=new_authors)

        assert resources[1] != result, result
        assert 'dara_authors' in result.keys(), result.keys()
        assert u'1045637-5' in result['dara_authors'], result['dara_authors']
        assert u'75261-7' in result['dara_authors'], result['dara_authors']

        updated_record = tester.get_resource(resources[1]['id'])
        assert u'1045637-5' in updated_record['dara_authors'], updated_record['dara_authors']
        assert u'75261-7' in updated_record['dara_authors'], updated_record['dara_authors']

        assert u'Yellen' in updated_record['dara_authors'], updated_record['dara_authors']


    def test_92_xml_check_packages(self):
        sysadmin = factories.Sysadmin()
        packages = self._create_package_resource(num_journals=3)
        tester = BulkUpdater(self._get_app(), key=sysadmin['apikey'],test=True)

        new_authors = tester.update_affil_id(packages[0]['name'])
        result=tester.patch_package(id=packages[0]['name'],update=new_authors)

        new_authors = tester.update_affil_id(packages[1]['name'])
        result=tester.patch_package(id=packages[1]['name'],update=new_authors)

        new_authors = tester.update_affil_id(packages[2]['name'])
        result=tester.patch_package(id=packages[2]['name'],update=new_authors)

        ## Package 1 ##

        base = '/dataset/{id}/dara_xml'
        url = base.format(id=packages[0]['id'])
        app = self._get_app()
        tree = xmltodict.parse(app.get(url).body)

        assert tree['resource']['creators'], "Creators is missing"
        creators = tree['resource']['creators']
        assert len(creators['creator']) == 3, "Missing creators: {}".format(creators)
        assert creators['creator'][2]['person']['affiliation'], "Missing Gurg {}".format(creators['creator'])

        aff1 = creators['creator'][0]['person']['affiliation']
        aff2 = creators['creator'][1]['person']['affiliation']
        aff3 = creators['creator'][2]['person']['affiliation']

        assert aff1['affiliationName'] == u"Deutsche Zentralbibliothek f\xfcr Wirtschaftswissenschaften  Leibniz-Informationszentrum Wirtschaft", aff1['affiliationName']
        assert aff2['affiliationName'] == u"Fake Plce", aff2['affiliationName']
        assert aff3['affiliationName'] == u"Institut f\xfcr Weltwirtschaft", aff3['affiliationName']

        assert 'affiliationIDs' not in aff1.keys()
        assert 'affiliationIDs' not in aff2.keys()

        aff3_id = aff3['affiliationIDs']['affiliationID']['identifierURI']
        assert '1007681-5' in aff3_id, aff3_id

        ## Package 2 ##

        base = '/dataset/{id}/dara_xml'
        url = base.format(id=packages[1]['id'])
        app = self._get_app()
        tree = xmltodict.parse(app.get(url).body)

        assert tree['resource']['creators'], "Creators is missing"
        creators = tree['resource']['creators']

        aff1 = creators['creator'][0]['person']['affiliation']
        aff2 = creators['creator'][1]['person']['affiliation']

        assert aff1['affiliationName'] == u"University of California Berkeley", aff1['affiliationName']
        assert aff2['affiliationName'] == u"NoWhere", aff2['affiliationName']

        assert 'affiliationIDs' not in aff2.keys()
        aff1_id = aff1['affiliationIDs']['affiliationID']['identifierURI']
        assert '2025100-2' in aff1_id, aff1_id

        ## Package 3 ##

        base = '/dataset/{id}/dara_xml'
        url = base.format(id=packages[2]['id'])
        app = self._get_app()
        tree = xmltodict.parse(app.get(url).body)

        assert tree['resource']['creators'], "Creators is missing"
        creators = tree['resource']['creators']

        aff1 = creators['creator']['person']['affiliation']

        assert aff1['affiliationName'] == u"Federal Reserve Bank <Boston, Mass.>", aff1['affiliationName']

        aff1_id = aff1['affiliationIDs']['affiliationID']['identifierURI']
        assert '270861-9' in aff1_id, aff1_id


    def test_93_xml_check_resources(self):
        sysadmin = factories.Sysadmin()
        packages,resources = self._create_package_resource(num_resources=3, resource=True)
        tester = BulkUpdater(self._get_app(), key=sysadmin['apikey'],test=True)

        new_authors = tester.update_affil_resource(resources[0]['id'])
        result=tester.patch_resource(id=resources[0]['id'],update=new_authors)

        new_authors = tester.update_affil_resource(resources[1]['id'])
        result=tester.patch_resource(id=resources[1]['id'],update=new_authors)

        new_authors = tester.update_affil_resource(resources[2]['id'])
        result=tester.patch_resource(id=resources[2]['id'],update=new_authors)

        ## Resource 1 ##

        base = '/dataset/{id}/resource/{resource_id}/dara_xml'
        url = base.format(id=resources[0]['package_id'], resource_id=resources[0]['id'])
        app = self._get_app()
        tree = xmltodict.parse(app.get(url).body)

        assert tree['resource']['creators'], "Creators is missing"
        creators = tree['resource']['creators']['creator']
        assert len(creators) == 1, len(creators)

        aff1 = creators['person']['affiliation']
        assert aff1['affiliationName'] == u"Strickland Propane", aff1['affiliationName']

        assert 'affiliationID' not in aff1.keys(), aff1.keys()

        ## Resource 2 ##

        base = '/dataset/{id}/resource/{resource_id}/dara_xml'
        url = base.format(id=resources[1]['package_id'], resource_id=resources[1]['id'])
        app = self._get_app()
        tree = xmltodict.parse(app.get(url).body)

        assert tree['resource']['creators'], "Creators is missing"
        creators = tree['resource']['creators']['creator']
        assert len(creators) == 2, creators

        aff1 = creators[0]['person']['affiliation']
        assert aff1['affiliationName'] == u"Federal Reserve Bank <Saint Louis, Mo.>", aff1['affiliationName']

        assert creators[0]['person']['firstName'] == u"Janet", creators[0]['person']['firstName']

        aff1_id = aff1['affiliationIDs']['affiliationID']['identifierURI']
        assert '75261-7' in aff1_id, aff1_id

        aff2 = creators[1]['person']['affiliation']
        assert aff2['affiliationName'] == u"Chicago Council on Foreign Relations", aff2['affiliationName']

        assert creators[1]['person']['firstName'] == u"Mrs.", creators[1]['person']['firstName']

        aff2_id = aff2['affiliationIDs']['affiliationID']['identifierURI']
        assert '1045637-5' in aff2_id, aff2_id

        ## Resource 3 ##
        base = '/dataset/{id}/resource/{resource_id}/dara_xml'
        url = base.format(id=resources[2]['package_id'], resource_id=resources[2]['id'])
        app = self._get_app()

        tree = xmltodict.parse(app.get(url).body)

        assert tree['resource']['creators'], "Creators is missing"
        creators = tree['resource']['creators']['creator']
        assert len(creators) == 3, creators

        aff1 = creators[0]['person']['affiliation']
        assert aff1['affiliationName'] == u"Springfield Power Plant", aff1['affiliationName']

        assert creators[0]['person']['firstName'] == u"Homer", creators[0]['person']['firstName']

        assert 'affiliationIDs' not in aff1.keys(), aff1

        aff2 = creators[1]['person']['affiliation']
        assert aff2['affiliationName'] == u"Daily Bugel", aff2['affiliationName']

        assert creators[1]['person']['firstName'] == u"Mr.", creators[1]['person']['firstName']

        assert 'affiliationIDs' not in aff2.keys(), aff2

        aff3 = creators[2]['person']['affiliation']
        assert aff3['affiliationName'] == u"Zoologischer Garten <Frankfurt, Main>", aff3['affiliationName']

        assert creators[2]['person']['firstName'] == u"Max", creators[2]['person']['firstName']

        aff3_id = aff3['affiliationIDs']['affiliationID']['identifierURI']
        assert '2027192-X' in aff3_id, aff3_id


    def test_dara_submission_update(self):
        auth = (config.get('ckanext.dara.demo.user'),
            config.get('ckanext.dara.demo.password'))

        sysadmin = factories.Sysadmin()
        tester = BulkUpdater(self._get_app(), key=sysadmin['apikey'],test=True)
        packages,resources = self._create_package_resource(num_resources=3, resource=True)

        base = '/dataset/{id}/dara_xml'
        url = base.format(id=packages[0]['id'])
        app = self._get_app()
        xml = app.get(url).body

        dara = darapi(auth, xml.decode('utf-8'), test=True, register=False)
        assert dara in [200, 201], dara

        data = xmltodict.parse(xml)
        id_ = data['resource']['resourceIdentifier']['identifier']

        new_authors = tester.update_affil_id(packages[0]['name'])
        result=tester.patch_package(id=packages[0]['name'],update=new_authors)

        url = base.format(id=result['id'])
        app = self._get_app()
        new_xml = app.get(url).body
        tree = xmltodict.parse(new_xml)
        new_id = tree['resource']['resourceIdentifier']['identifier']
        assert id_ == new_id, "Old and new IDs don't match"

        creators = tree['resource']['creators']
        assert len(creators['creator']) == 3, "Missing creators: {}".format(creators)
        assert creators['creator'][2]['person']['affiliation'], "Missing Gurg {}".format(creators['creator'])

        aff1 = creators['creator'][0]['person']['affiliation']
        aff2 = creators['creator'][1]['person']['affiliation']
        aff3 = creators['creator'][2]['person']['affiliation']

        assert aff1['affiliationName'] == u"Deutsche Zentralbibliothek f\xfcr Wirtschaftswissenschaften  Leibniz-Informationszentrum Wirtschaft", aff1['affiliationName']
        assert aff2['affiliationName'] == u"Fake Plce", aff2['affiliationName']
        assert aff3['affiliationName'] == u"Institut f\xfcr Weltwirtschaft", aff3['affiliationName']

        assert 'affiliationIDs' not in aff1.keys()
        assert 'affiliationIDs' not in aff2.keys()

        aff3_id = aff3['affiliationIDs']['affiliationID']['identifierURI']
        assert '1007681-5' in aff3_id, aff3_id

        # resubmit to DARA
        dara=darapi(auth, new_xml.decode('utf-8'), test=True, register=False)
        assert dara in [200, 201], dara




