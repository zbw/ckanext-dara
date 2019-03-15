import ckan
import webtest
import datetime
import paste
import paste.fixture
from ckan.tests import helpers
from ckan.lib.helpers import url_for

import pylons.test, pylons, pylons.config as c, ckan.model as model, ckan.plugins as plugins, ckan.tests.factories as factories

import ckanext.dara.bulk_metadata_update as bmu
import ckanext.dara.tests.data_test as data

import ckan.model as model
engine = model.meta.engine


class TestBulkUpdater(helpers.FunctionalTestBase):
    def teardown(self):
        model.repo.rebuild_db()


    def _get_app(self):
        c['global_conf']['debug'] = 'true'
        app = ckan.config.middleware.make_app(c['global_conf'], **c)
        app = webtest.TestApp(app)

        return app


    def _create_package(self, data):
        sysadmin = factories.Sysadmin()
        context = {
                    'user': sysadmin['name'],
                    'ignore_auth': True
                    }
        user = helpers.call_action('user_create',
                                    context=context,
                                    email='sysadmin@email.email',
                                    name='user',
                                    password='required',
                                    password_hash='hash')

        org = helpers.call_action('organization_create',
                                   context=context,
                                   name='test_org')

        data['owner_org'] = org['id']
        helpers.call_action('package_create', **data)


    def test_1_three_packages(self):
        obj = bmu.BulkUpdater()
        d1 = self._create_package(data.record1)
        d2 = self._create_package(data.record2)
        d3 = self._create_package(data.record3)
        assert len(obj.packages) == 3, d1

