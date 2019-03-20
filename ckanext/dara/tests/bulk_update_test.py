
import ckan
import json
import webtest
import datetime
import paste.fixture
import ckan.model as model
from ckan.tests import helpers
from ckan.lib.helpers import url_for
import pylons.test, pylons, pylons.config as c, ckan.model as model, ckan.tests as tests, ckan.plugins as plugins, ckan.tests.factories as factories


import ckanext.dara.tests.data_test as rd
from ckanext.dara.bulk_metadata_update import BulkUpdater

import ckan.model as model
engine = model.meta.engine

"""
    TODO:
        * check for DOIs
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
                resources.append(factories.Resource(package_id=datasets[0]['id'], url='http://test.link/{}'.format(_)))
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








