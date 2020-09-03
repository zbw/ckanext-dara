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
def register(id, template):
    """
    register at da|ra
    """
    _check_access(id)
    context = _context()

    if params()['test'] or params()['test_register']:
        doi_key = 'dara_DOI_Test'
        a = {201: ('dara_registered_test', 'Dataset registered (Test)'),
                200: ('dara_updated_test', 'Dataset updated (Test)')}
    else:
        doi_key = 'dara_DOI'
        a = {201: ('dara_registered', 'Dataset registered'),
                200: ('dara_updated', 'Dataset updated')}

    def store():
        d = doi.pkg_doi(c.pkg_dict)
        c.pkg_dict.update({doi_key: d})
        date = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.now())
        k = get_in([dara, 0], a)
        c.pkg_dict[k] = date
        tk.get_action('package_update')(context, c.pkg_dict)

    def response():
        if dara in a.iterkeys():
            store()
            h.flash_success(get_in([dara, 1], a))
        else:
            h.flash_error("ERROR! Sorry, dataset has not been registered or\
                        updated. Please contact your friendly sysadmin. ({})\
                        ".format(dara))
        tk.redirect_to('dara_doi', id=id)

    def register_resources():
        def reg(resource):
            resource_id = resource['id']
            c.resource = tk.get_action('resource_show')(context, {'id': resource_id})
            xml = xml(id, 'package/resource.xml')
            dara = darapi(auth(), xml, test=params()['test'],
                    register=params()['register'])
            if dara in a.iterkeys():
                c.resource[doi_key] = doi.res_doi(c.resource)
                tk.get_action('resource_update')(context, c.resource)
            else:
                h.flash_error("ERROR! Resource {} could not be registered ({}).\
                        Dataset has not been registered".format(resource_id, dara))
                tk.redirect_to('dara_doi', id=id)

        c.pkg_dict = tk.get_action('package_show')(context, {'id': id})
        resources = filter(lambda res: res['id'] in tk.request.params,
                c.pkg_dict['resources'])
        map(reg, resources)

    # first register resources
    register_resources()

    # register package. we must first get the pkg with the updated resources to
    # get their DOIs/URLs
    c.pkg_dict = tk.get_action('package_show')(context, {'id': id})
    dara = darapi(auth(), xml(id, template),
                test=params()['test'], register=params()['register'])
    response()

def xml(id, template):
    """
    returning valid dara XML
    """
    # certs = '/etc/pki/tls/certs/ca-bundle.crt'
    response.headers['Content-Type'] = "text/xml; charset=utf-8"
    xml_string = tk.render(template)
    # validate
    xmlschema_doc = etree.parse(StringIO(schema))
    xmlschema = etree.XMLSchema(xmlschema_doc)
    doc = etree.parse(StringIO(xml_string))
    xmlschema.assertValid(doc)
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
