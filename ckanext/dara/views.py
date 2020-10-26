import os
import requests
import mimetypes
from ckan import model
import ckan.lib.helpers as h
import ckan.plugins.toolkit as tk
import ckan.lib.uploader as uploader
from ckan.common import g, request
from toolz.dicttoolz import keyfilter, get_in

from lxml import etree
from io import StringIO
import xml.etree.ElementTree as ET
from ckanext.dara.dara_schema.v4_0 import schema

import ckan.logic as logic
import ckan.lib.base as base
import ckan.lib.uploader as uploader
from ckanext.dara.helpers import check_journal_role
from ckanext.dara import doi as digital_object

import flask
import ckanext.dara.doi as doi_helpers
from datetime import datetime
from flask import make_response

from ckan.common import config
from functools import wraps

import logging
log = logging.getLogger(__name__)

NotFound = logic.NotFound
NotAuthorized = logic.NotAuthorized
get_action = logic.get_action


def params():
    """
    test for parameters. For testserver DOI registration is not possible,
    so we fake it (test_register).
    defaults: register at 'real' server and get a DOI
    """

    ptest = lambda p: p in tk.request.params
    ctest = {'true': True, 'false': False}.get(config.get('ckanext.dara.use_testserver', 'false'))

    # defaults
    test = False
    register = ptest('DOI')
    test_register = False

    if ctest or ptest('testserver'):
        test = True

    if test and register:
        register = False
        test_register = True
    return {'test': test, 'register': register,
            'test_register': test_register}

def admin_req(func):
    @wraps(func)
    def check(*args, **kwargs):
        id = kwargs['id']
        try:
            pkg = tk.get_action('package_show')(None, {'id': id})
        except:
            h.flash_error("Unauthorized to manage DOIs")
            return h.redirect_to(u"home.index")

        if not check_journal_role(pkg, 'admin') and not h.check_access('sysadmin'):
            base.abort(401, 'Unauthorized to manage DOIs')
        return func(id)
    return check


class DaraError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)

def _context():
    return {'model': model, 'session': model.Session,
            'user': g.user or g.author, 'for_view': True,
            'auth_user_obj': g.userobj}

# TODO do this as decorator, as in edawax.controller
def _check_access(id):
    context = _context()
    pkg = tk.get_action('package_show')(context, {'id': id})
    if not check_journal_role(pkg, 'admin') and not h.check_access('sysadmin'):
        tk.abort(401, 'Unauthorized to manage DOIs')

@admin_req
def register(id):
    """
    register at da|ra
    """
    _check_access(id)
    context = _context()

    request_url = request.url
    if 'resource' in request_url:
        template = 'package/resource.xml'
    else:
        template = 'package/collection.xml'

    if params()['test'] or params()['test_register']:
        doi_key = 'dara_DOI_Test'
        a = {201: ('dara_registered_test', 'Dataset registered (Test)'),
                200: ('dara_updated_test', 'Dataset updated (Test)')}
    else:
        doi_key = 'dara_DOI'
        a = {201: ('dara_registered', 'Dataset registered'),
                200: ('dara_updated', 'Dataset updated')}

    def store():
        d = digital_object.pkg_doi(pkg_dict)
        pkg_dict.update({doi_key: d})
        date = f'{datetime.now():%Y-%m-%d %H:%M:%S}'
        k = get_in([dara, 0], a)
        pkg_dict[k] = date
        tk.get_action('package_update')(context, pkg_dict)

    def response():
        if dara in a.keys():
            store()
            h.flash_success(get_in([dara, 1], a))
        else:
            h.flash_error(f"ERROR! Sorry, dataset has not been registered or\
                        updated. Please contact your friendly sysadmin. ({dara})")
        return h.redirect_to(u'dara_doi', id=id)

    def register_resources():
        def reg(resource):
            resource_id = resource['id']
            resource = tk.get_action('resource_show')(context, {'id': resource_id})
            xml = xml(id, 'package/resource.xml')
            dara = darapi(auth(), xml, test=params()['test'],
                    register=params()['register'])
            if dara in a.keys():
                resource[doi_key] = digital_object.res_doi(resource)
                tk.get_action('resource_update')(context, resource)
            else:
                h.flash_error(f"ERROR! Resource {resource_id} could not be registered ({dara}).\
                        Dataset has not been registered")
                tk.redirect_to('dara_doi', id=id)

        pkg_dict = tk.get_action('package_show')(context, {'id': id})
        resources = filter(lambda res: res['id'] in tk.request.params,
                pkg_dict['resources'])
        map(reg, resources)

    # first register resources
    register_resources()

    # register package. we must first get the pkg with the updated resources to
    # get their DOIs/URLs
    pkg_dict = tk.get_action('package_show')(context, {'id': id})
    dara = darapi(auth(), xml(id, template),
                test=params()['test'], register=params()['register'])
    return response()

def xml(id, resource_id=None):
    """
    returning valid dara XML
    """
    # Determine which template to use
    request_url = request.url
    if 'resource' in request_url:
        template = 'package/resource.xml'
    else:
        template = 'package/collection.xml'
    # certs = '/etc/pki/tls/certs/ca-bundle.crt'
    headers = {u'Content-Type': u"text/xml; charset=utf-8"}
    xml_string = tk.render(template)
    # validate
    xmlschema_doc = etree.fromstring(str.encode(schema))
    xmlschema = etree.XMLSchema(xmlschema_doc)
    doc = etree.fromstring(xml_string)
    xmlschema.assertValid(doc)

    if 'dara_xml' in request.url:
        return make_response(xml_string, 200, headers)
    return xml_string

@admin_req
def doi(id):
    """
    DOI manager page
    """
    context = _context()
    pkg_dict = tk.get_action('package_show')(context, {'id': id})
    pkg = context['package']

    extra_vars = {u'pkg_dict': pkg_dict}

    return tk.render('package/doi.html', extra_vars)

def _check_extension(filename):
    """
    check if the file extension should force a download
    """
    extensions_for_download = ['.txt', '.do', '.log']
    if filename:
        try:
            name, ext = os.path.splitext(filename)
        except:
            return False
        if ext in extensions_for_download:
            return True
    return False

def resource_download(id, resource_id, filename=None):
    """
    Force the download for the specified files
    """
    context = _context()
    context['ignore_auth'] = True

    force_download = _check_extension(filename)

    try:
        rsc = tk.get_action('resource_show')(context, {'id': resource_id})
        pkg = tk.get_action('package_show')(context, {'id': id})
    except tk.ObjectNotFound:
        tk.abort(404, 'Resource not found')
    except tk.NotAuthorized:
        tk.abort(401, 'Unauthorized to read resource %s' % id)

    try:
        rsc = get_action('resource_show')(context, {'id': resource_id})
        get_action('package_show')(context, {'id': id})
    except (NotFound, NotAuthorized):
        abort(404, _('Resource not found'))

    if rsc.get(u'url_type') == u'upload':
        upload = uploader.get_resource_uploader(rsc)
        filepath = upload.get_path(rsc[u'id'])
        return flask.send_file(filepath)
    elif u'url' not in rsc:
        return base.abort(404, _(u'No download is available'))
    return h.redirect_to(rsc[u'url'])


def cancel(pkg_id):
    """
        When a user cancels adding additional resources, they were being
        put into the `draft` state which prevented them from appearing
        in the list of datasets.

        Drafts only appear in the list of author's submissions even if they have been published.

        This assumes `canceled` datasets are finished but the author made
        a mistake in trying to add too many resources.
    """
    context = _context()
    pkg = tk.get_action('package_show')(None, {'id': pkg_id})
    pkg['state'] = 'active'
    update = tk.get_action('package_update')(context, pkg)

    redirect(pkg_id)


def redirect(id):
    #tk.redirect_to(controller='package', action='read', id=id)
    h.redirect_to('dataset.read', id=id)

def darapi(auth, xml, test=False, register=False):
    """
    talking with da|ra API. See da|ra reference:
    http://www.da-ra.de/fileadmin/media/da-ra.de/PDFs/dara_API_reference_v1.pdf
    http://www.da-ra.de/fileadmin/media/da-ra.de/PDFs/dara_API_-_registration.pdf
    :param auth: tuple with username and password for the account at da|ra for
                 the account at da|ra
    :param xml: the XML string to post to da|ra, *without* the <?xml ... ?>
                instruction. XML must validate against the dara XSD-Schema
    :param test: if True connects to dara production server, otherwise it uses
                the test-server (default: False)
    :param register: register a DOI. Note that the test server cannot register
                    DOI. If you try it will return an additional message
                    (default: False)
    da|ra response http codes:
        201 Created operation successful, returned if a new dataset created
        200 OK operation successful, returned if an existing dataset updated
        400 Bad Request - request body must be valid xml
        401 Unauthorized - no or wrong login
        500 Internal Server Error - server internal error, try later and if
            problem persists please contact da|ra
    '500' usually means that there's an error in your request. It unfortunately
    also returns a huge chunk of html output. However, it can be used for
    debugging.
    POST: create a new resource. If the item already exists in the system.
    It will be updated.
        Requires the identifier and currentVersion in the `resourceIdentifier`
    """
    d = {False: 'http://www.da-ra.de/dara/study/importXML',
#         True: 'http://dara-test.gesis.org:8084/dara/study/importXML'}
          True: 'http://labs.da-ra.de/dara/study/importXML'}
    url = d.get(test)
    # socket does not take unicode, so we need to encode our unicode object
    # see http://stackoverflow.com/questions/9752521/sending-utf-8-with-sockets
    # XXX do we always get unicode object???
    xml_encoded = xml.encode('utf-8')

    parameters = keyfilter(lambda x: register, {'registration': 'true'})
    headers = {'content-type': 'application/xml;charset=UTF-8'}
    req = requests.post(url, auth=auth, headers=headers, data=xml_encoded,
            params=parameters)
    log.info(f"Requesting DOI [{test}]: {url}")
    log.error(f"Response: {req} {req.reason} {req.text}")

    return req.status_code

def auth():
    def gc(kw):
        auths = list(map(lambda t: config.get(t, False), kw))
        if not all(auths):
            raise DaraError(f"User and/or password ({kw[0]}, {kw[1]}) not \
                   set in CKAN config")
        return tuple(auths)  # requests needs tuple

    if params()['test']:
        return gc(['ckanext.dara.demo.user', 'ckanext.dara.demo.password'])
    return gc(['ckanext.dara.user', 'ckanext.dara.password'])
