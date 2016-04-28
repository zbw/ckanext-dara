# testing helper functions does not work yet, we get 
# "TypeError: No object (name: tmpl_context or C) has been registered for this thread"
# in addition, ckan.lib.helpers does not have the plugin helpers
# So, in short: I don't know how to test helpers :-)


import paste.fixture
import pylons.test
import pylons.config as config
import webtest

from ckanext.dara import helpers as dara_helpers
import ckan.model as model
# import ckan.tests.legacy as tests
import ckan.tests.factories as factories
import nose.tools as nose_tools

import ckan.plugins as plugins
import ckan.tests.helpers as test_helpers
from ckan.tests.helpers import FunctionalTestBase
import ckan.lib.helpers as ckan_helpers

class TestDaraHelpers(FunctionalTestBase):
    """
    """
    @classmethod
    def setup_class(cls):
        super(TestDaraHelpers, cls).setup_class()
        plugins.load('dara')

    def teardown(self):
        model.repo.rebuild_db()

    @classmethod
    def teardown_class(cls):
        plugins.unload('dara')
        super(TestDaraHelpers, cls).teardown_class()
   
    def test_dara_auto_fields(self):
        pkg = factories.Dataset()
        af = dara_helpers.dara_auto_fields()
        pkg_url = ckan_helpers.url_for(controller='package', action='read',
                id=pkg.id)
        assert af['URL'] == 'http://edawax.de' + pkg_url
    
   #def test_check_journal_role_true(self):
   #    user = factories.User()
   #    org_users = [{'name': user['name'], 'capacity': 'admin'}]
   #    org = factories.Organization(users=org_users)
   #    pkg = factories.Dataset(owner_org=org['id'])
   #    context = {'user': user['name'], 'model': model}
   #    import ipdb; ipdb.set_trace()
   #    result = ckan_helpers.check_journal_role(pkg, 'admin')
   #    nt.assert_is(result, True)
        

