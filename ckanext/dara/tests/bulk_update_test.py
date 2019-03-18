import os
import json
import ckan
import webtest
import datetime
import paste
import paste.fixture
from ckan.tests import helpers
from ckan.lib.helpers import url_for

import pylons.test, pylons, pylons.config as c, ckan.model as model, ckan.plugins as plugins, ckan.tests.factories as factories

from ckanext.dara.bulk_metadata_update import BulkUpdater


class TestBulkUpdater(helpers.FunctionalTestBase):
    def teardown(self):
        model.repo.rebuild_db()


    def _get_app(self):
        c['global_conf']['debug'] = 'true'
        app = ckan.config.middleware.make_app(c['global_conf'], **c)
        app = webtest.TestApp(app)

        return app


    def _create_package_resource(self, num_resources=1, resource=False, num_packages=1):
        user = factories.User(sysadmin=True)
        owner_org = factories.Organization(users=[{'name': user['id'], 'capacity': 'admin'}])

        datasets = []
        for _ in range(num_packages):
            datasets.append(factories.Dataset(owner_org=owner_org['id'], dara_PublicationDate=2019, dara_currentVersion=1))

        resources = []
        if resource:
            for _ in range(num_resources):
                resources.append(factories.Resource(package_id=datasets[0]['id'], url='http://test.link/{}'.format(_)))
            return datasets, resources
        return datasets


    def test_1_five_packages(self):
        datasets = self._create_package_resource(num_packages=5)
        url = "/api/3/action/package_list"

        app = self._get_app()
        res = app.get(url=url)

        bulk = BulkUpdater(base='/api/3/action/{action}')
        print(bulk.get_packages())

        assert len(datasets) == 5, len(datasets)
        assert len(json.loads(res.body)['result']) == 5, len(json.loads(res.body)['result'])

        assert len(bulk.get_packages()) == 5, len(bulk.get_packages())

    def test_2(self):
        pass



