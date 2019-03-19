import ast
import random

import ckanapi
import requests
import ckanext.dara.tests.data_test as data

from ckanext.dara.bulk_metadata_update import BulkUpdater


class TestBulkUpdater:
    def __init__(self):
        self.key = '4e78656e-51e0-43a2-a173-69e1b88b81e9'
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


    def _delete_package(self, id):
        self.ckan.action.package_delete(id=id)


    def setup(self):
        print('\n\n**start')
        owner = self._create_journal()
        self.owner_org = owner['id']


    def teardown(self):
        print('finishing')
        #self._delete_package(self.pack1_id)
        #self._delete_package(self.pack2_id)
        #self._delete_package(self.pack3_id)
        #self._delete_journal()


    def test_1_get_package(self):
        bulk = BulkUpdater(base='http://127.0.0.1:5000/api/3/action/{action}')

        packages = bulk.get_packages()
        assert len(packages) == 1, len(packages)
        assert 'federal-reserve' in packages


    def test_2_get_package1(self):
        bulk = BulkUpdater(base='http://127.0.0.1:5000/api/3/action/{action}')

        packages = bulk.get_packages()
        package = bulk.get_package('federal-reserve')
        authors = ast.literal_eval(package['dara_authors'])

        assert len(authors) == 3, len(authors)
        assert authors[0]['affil'] == 'Federal Reserve Bank <Saint Louis, Mo.>', authors[0]['affil']
        assert authors[1]['affil'] == 'Federal Reserve Bank <San Francisco, Calif.>', authors[1]['affil']
        assert authors[2]['affil'] == 'NoWhere', authors[2]['affil']


    def test_3_lookup(self):
        bulk = BulkUpdater(base='http://127.0.0.1:5000/api/3/action/{action}')

        packages = bulk.get_packages()
        package = bulk.get_package('federal-reserve')
        authors = ast.literal_eval(package['dara_authors'])
        affiliations = []
        for author in authors:
            l = bulk.lookup(author['affil'].encode('utf-8'))
            affiliations.append( (author['affil'], l) )

        assert (u'NoWhere', False) in affiliations, affiliations
        assert (u'Federal Reserve Bank <Saint Louis, Mo.>', u'75261-7') in affiliations, affiliations
        assert (u'Federal Reserve Bank <San Francisco, Calif.>', u'270186-8') in affiliations, affiliations




    def _test_4_update_record(self):
        pass
