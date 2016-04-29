import ckan.model as model
import ckan.tests.factories as factories
import nose.tools as nt
import ckan.plugins as plugins
from ckan.tests.helpers import FunctionalTestBase, change_config, reset_db
# from routes import url_for
import ckan.plugins.toolkit as tk
# import ckan.tests.legacy as tests
import untangle
import pylons.config as config
import ckan.lib.search as search
from ckanext.dara.controller import darapi
from ckanext.dara.tests.example_xml import DS_XML, RES_XML


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


def _dara_testpackage():
    pkg = factories.Dataset(
        dara_authors=['Bargfrede', 'Philipp', '', '', '', '', ''],
        dara_PublicationDate='2002',
        dara_currentVersion="1",
    )
    return pkg


class TestDaraController(FunctionalTestBase):
    """
    """
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
        self.test_package = self._dara_testpackage()
    
    @classmethod
    def setup_class(cls):
        super(TestDaraController, cls).setup_class()
        plugins.load('dara')

    def teardown(self):
        #del config['ckanext.dara.use_testserver']
        model.repo.rebuild_db()

    @classmethod
    def teardown_class(cls):
        plugins.unload('dara')
        super(TestDaraController, cls).teardown_class()
   
    def _dara_testpackage(self):
        pkg = factories.Dataset(
            dara_authors=['Bargfrede', 'Philipp', '', '', '', '', ''],
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
        assert "<firstName>Philipp</firstName>" in response.body
        assert "<lastName>Bargfrede</lastName>" in response.body
    
    def test_resource_xml(self):
        app = self._get_test_app()
        pkg = self.test_package
        res = factories.Resource(package_id=pkg['id'])
        response = _get_resource_action_page(app, pkg['name'], res['id'], 'dara_xml')
        nt.eq_(response.headers['Content-Type'], 'text/xml; charset=utf-8')
        assert "<firstName>Philipp</firstName>" in response.body
        assert "<lastName>Bargfrede</lastName>" in response.body
   
    def test_register(self):
        """ test DOI registration
        """
        # this is in test.ini, but just to be sure ;-)
        change_config('ckanext.dara.use_testserver', True)
        
        dataset = self.test_package
        app = self._get_test_app()
        user = self.sysadmin
        env = {'REMOTE_USER': user['name'].encode('ascii')}
        pkg_url = tk.url_for(controller='package', action="read",
                id=dataset['name'])
        action_url = "{}/dara_register".format(pkg_url)

        response = app.get(
            url=action_url,
            extra_environ=env,
        )

        redirect = app.get(url=response.headers['Location'],
                   extra_environ=env)
    
        assert 'Dataset registered (Test)' in redirect.body


def test_darapi_dataset():
    auth = (config.get('ckanext.dara.demo.user'),
            config.get('ckanext.dara.demo.password'))
    dara = darapi(auth, DS_XML, test=True, register=False)
    assert dara in [200, 201]


def test_darapi_resource():
    auth = (config.get('ckanext.dara.demo.user'),
            config.get('ckanext.dara.demo.password'))
    dara = darapi(auth, RES_XML, test=True, register=False)
    assert dara in [200, 201]



            


