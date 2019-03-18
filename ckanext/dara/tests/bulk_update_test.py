import ast
import random

import ckanapi
import requests
import ckanext.dara.tests.data_test as data

from ckanext.dara.bulk_metadata_update import BulkUpdater


class TestBulkUpdater:
    def __init__(self):
        self.key = 'd8e4e1af-3ee0-4815-ae9a-839822ec02e1'
        self.ckan=ckanapi.RemoteCKAN('http://127.0.0.1:5000', apikey=self.key)
        self.journal_name = 'test-journal-test'


    def _create_journal(self):
        try:
            journal = self.ckan.action.organization_create(name=self.journal_name)
            return journal
        except Exception as e:
            journal = self.ckan.action.organization_show(id=self.journal_name)
            return journal


    def _delete_journal(self):
        self.ckan.action.organization_purge(id=self.journal_name)


    def _create_package(self, pack_data):
        try:
            package = self.ckan.action.package_create(**pack_data)
            return package
        except Exception as e:
            pass  #print(e)

    def _delete_package(self, id):
        self.ckan.action.package_delete(id=id)


    def setup(self):
        print('\n**start')
        owner = self._create_journal()
        self.owner_org = owner['id']

        d = data.record1
        d['owner_org'] = self.owner_org
        pack1 = self._create_package(d)

        d = data.record2
        d['owner_org'] = self.owner_org
        pack2 = self._create_package(d)

        d = data.record3
        d['owner_org'] = self.owner_org
        pack3 = self._create_package(d)


    def teardown(self):
        print('finishing')
        #self._delete_package(self.pack1_id)
        #self._delete_package(self.pack2_id)
        #self._delete_package(self.pack3_id)
        #self._delete_journal()


    def test_1_get_three_packages(self):
        bulk = BulkUpdater(base='http://127.0.0.1:5000/api/3/action/{action}')

        packages = bulk.get_packages()
        assert len(packages) == 3, len(packages)
        assert 'a-title' in packages
        assert 'industrial-relations' in packages
        assert 'still-different-after-all-these-years-replication-data' in packages


    def test_2_get_package1(self):
        bulk = BulkUpdater(base='http://127.0.0.1:5000/api/3/action/{action}')

        packages = bulk.get_packages()
        package = bulk.get_package('a-title')
        authors = ast.literal_eval(package['dara_authors'])

        assert len(authors) == 3, len(authors)
        assert authors[0]['affil'] in [u'Deutsche Zentralbibliothek f\xfcr Wirtschaftswissenschaften  Leibniz-Informationszentrum Wirtschaft', u'Fake Plce', u'Institut f\xfcr Weltwirtschaft'], authors[0]['affil']
        assert authors[1]['affil'] in [u'Deutsche Zentralbibliothek f\xfcr Wirtschaftswissenschaften  Leibniz-Informationszentrum Wirtschaft', u'Fake Plce', u'Institut f\xfcr Weltwirtschaft'], authors[1]['affil']
        assert authors[2]['affil'] in [u'Deutsche Zentralbibliothek f\xfcr Wirtschaftswissenschaften  Leibniz-Informationszentrum Wirtschaft', u'Fake Plce', u'Institut f\xfcr Weltwirtschaft'], authors[2]['affil']


    def test_3_lookup(self):
        bulk = BulkUpdater(base='http://127.0.0.1:5000/api/3/action/{action}')

        packages = bulk.get_packages()
        package = bulk.get_package('a-title')
        authors = ast.literal_eval(package['dara_authors'])
        affiliations = []
        for author in authors:
            l = bulk.lookup(author['affil'].encode('utf-8'))
            affiliations.append( (author['affil'], l) )

        assert (u'Fake Plce', False) in affiliations, affiliations
        assert (u'Institut f\xfcr Weltwirtschaft', u'1007681-5') in affiliations, affiliations

        package = bulk.get_package('industrial-relations')
        authors = ast.literal_eval(package['dara_authors'])
        affiliations = []
        for author in authors:
            l = bulk.lookup(author['affil'].encode('utf-8'))
            affiliations.append( (author['affil'], l) )

        assert ('NoWhere', False) in affiliations, affiliations
        assert ('University of California Berkeley', u'2025100-2') in affiliations, affiliations


        package = bulk.get_package('still-different-after-all-these-years-replication-data')
        authors = ast.literal_eval(package['dara_authors'])
        affiliations = []
        for author in authors:
            l = bulk.lookup(author['affil'].encode('utf-8'))
            affiliations.append( (author['affil'], l) )

        assert ('Federal Reserve Bank <Boston, Mass.>', u'270861-9') in affiliations, affiliations


    def test_4_update_record(self):
        pass
