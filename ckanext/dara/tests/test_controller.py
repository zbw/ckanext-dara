import ckan.model as model
import ckan.tests.factories as factories
#from ckan.lib.create_test_data import CreateTestData
import nose.tools as nt
import ckan.plugins as plugins
from ckan.tests.helpers import FunctionalTestBase
#from routes import url_for
import ckan.plugins.toolkit as tk
import ckan.tests.legacy as tests
import untangle
import pylons.config as config
import webtest
import ckan
from ckanext.dara.controller import darapi


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


class TestDaraController(FunctionalTestBase):
    """
    """

    def setup(self):
        """
        Create users and organizations
        """
        #super(TestDaraController).setup()
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
        self.test_package = self._dara_testpackage()
    
    @classmethod
    def setup_class(cls):
        super(TestDaraController, cls).setup_class()
        plugins.load('dara')

    def teardown(self):
        model.repo.rebuild_db()

    @classmethod
    def teardown_class(cls):
        plugins.unload('dara')
        super(TestDaraController, cls).teardown_class()
   
    def _dara_testpackage(self):
        pkg = factories.Dataset(
            dara_authors=['Bargfrede', 'Philipp', '', '', ''],
            dara_PublicationDate='2002',
            dara_currentVersion="1",
            owner_org=self.test_org_1['id']
        )
        return pkg

    def test_dataset_xml(self):
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
    
    def test_resource_xml(self):
            
        app = self._get_test_app()
        pkg = self.test_package
        res = factories.Resource(package_id=pkg['id'])
        response = _get_resource_action_page(app, pkg['name'], res['id'], 'dara_xml')
        nt.eq_(response.headers['Content-Type'], 'text/xml; charset=utf-8')
    
    def test_darapi_dataset(self):
        dataset = self.test_package
        app = self._get_test_app()
        response = _get_package_action_page(app, dataset['name'], 'dara_xml')
        xml = response.unicode_body
        import ipdb; ipdb.set_trace()
        auth = (config.get('ckanext.dara.demo.user'),
                config.get('ckanext.dara.demo.password'))
        dara = darapi(auth, xml, test=True, register=True)
        assert dara in [200, 201]



        


