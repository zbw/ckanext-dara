"""
Test Implementation of a DOI validator for the related publication
form
"""
import pylons.test, pylons, pylons.config as c, ckan.model as model, ckan.tests as tests, ckan.plugins as plugins, ckan.tests.factories as factories
from ckan.tests import helpers
import ckanext.dara.validators as v
import unittest
import ckan.lib.navl.dictization_functions as df
from ckan.plugins.toolkit import Invalid
StopOnError = df.StopOnError

pylons.app_globals._push_object(c['pylons.app_globals'])


class TestNewInvites(object):
    def __init__(self):
        self.key = 'ID'
        self.errors = ''
        self.context = ''

    @classmethod
    def setup_class(cls):
        plugins.load('dara')

    def teardown(self):
        model.repo.rebuild_db()

    @classmethod
    def teardown_class(cls):
        plugins.unload('dara')

    #dara_doi_validator(key, data, errors, context):
    def test_good_DOI(self):
        data = {'ID': '10.15456/ger.2018262.132251', ('dara_Publication_PIDType', ): 'DOI'}
        valid = v.dara_doi_validator(self.key, data, self.errors, self.context)
        assert valid == '10.15456/ger.2018262.132251', valid

    def test_good_fake_DOI(self):
        data = {'ID': '10.2150/125-ver1', ('dara_Publication_PIDType', ): 'DOI'}
        try:
            valid = v.dara_doi_validator(self.key, data, self.errors, self.context)
            assert False
        except Invalid as ed:
            assert True


    def test_bad_DOI(self):
        data = {'ID': 'doi.org/10.15456/ger.2018262.132251', ('dara_Publication_PIDType', ): 'DOI'}
        try:
            valid = v.dara_doi_validator(self.key, data, self.errors, self.context)
            assert False
        except Invalid as e:
            assert True


    def test_empty_field(self):
        data = {'ID': None, ('dara_Publication_PIDType', ): ''}
        try:
            valid = v.dara_doi_validator(self.key, data, self.errors, self.context)
            assert False
        except StopOnError as e:
            assert True


    def test_not_empty_but_not_doi(self):
        data = {'ID': 'TESTTESTTEST', ('dara_Publication_PIDType', ): 'ARK'}
        valid = v.dara_doi_validator(self.key, data, self.errors, self.context)
        assert valid == 'TESTTESTTEST'
