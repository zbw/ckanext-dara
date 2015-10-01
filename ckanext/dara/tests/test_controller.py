import ckan.model as model
import ckan.tests.factories as factories
#from ckan.lib.create_test_data import CreateTestData
import nose.tools as nt
import ckan.plugins as plugins
from ckan.tests.helpers import FunctionalTestBase
#from routes import url_for
import ckan.plugins.toolkit as tk
import untangle


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

def _dara_testpackage():
    pkg = factories.Dataset(
        dara_authors=['Bargfrede','Philipp', '', '', ''],
        dara_PublicationDate='2002',
        
        # this is fake; TODO: test with real DOI generation method in helpers
        dara_DOI_Proposal="10.1234/fake.234Mt" 
        )
    return pkg


class TestDaraController(FunctionalTestBase):
    """
    """
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
   
    def test_xml(self):
        """
        test dara_xml generation and view
        """
        dataset = _dara_testpackage()
        app = self._get_test_app()
        response = _get_package_action_page(app, dataset['name'], 'dara_xml')
        nt.eq_(response.headers['Content-Type'], 'text/xml; charset=utf-8')

        obj = untangle.parse(response.body)
        nt.assert_equals(obj.resource.publicationDate.year.cdata,
                         dataset['dara_PublicationDate'])
        
        # TODO test other elements, at the dara requrired (DOIproposal, authors
        


