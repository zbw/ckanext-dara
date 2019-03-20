"""
    Script to update metadata in the JDA for fields that exist
"""
import ast
import json
import requests
import ckanapi



class BulkUpdater:
    def __init__(self, app, key, test):
        if test:
            self.obj = ckanapi.TestAppCKAN(app, apikey=key)
        else:
            self.obj = ckanapi.RemoteCKAN(app, apikey=key)
        self.lookup_base = u'http://www.zbw.eu/beta/econ-ws/suggest2?dataset=econ_corp&query={name}'


    def get_packages(self):
        return self.obj.action.package_list()


    def get_package(self, id):
        return self.obj.action.package_show(id=id)


    def patch_package(self, id, update):
        return self.obj.action.package_patch(id=id, dara_authors=json.dumps(update, ensure_ascii=False))


    def lookup(self, name):
        name = name.replace('-', ' ').replace('  ', ' ').replace('  ', ' ')
        url = self.lookup_base.format(name=name)
        r = requests.get(url).json()['results']

        if len(r['bindings']) == 1:
            b_id = r['bindings'][0][u'concept'][u'value'].replace('http://d-nb.info/gnd/', '')
            return b_id

        for binding in r['bindings']:
            b_id=binding[u'concept'][u'value'].replace('http://d-nb.info/gnd/', '')
            prefLabel = binding[u'prefLabel'][u'value']
            prefName = binding[u'prefName'][u'value']

            if name == prefLabel or name == prefName:
                return b_id

        return False


    def update_affil_id(self, name):
        package = self.get_package(name)
        try:
            authors = package['dara_authors']
        except Exception:
            return False

        updated_authors = []
        for author in json.loads(authors):
            aff = author['affil']
            if aff and aff != '':
                affID = self.lookup(aff)

                if affID != False and affID != '':
                    author['affilID'] = affID
                updated_authors.append(author)

        #package['dara_authors'] = updated_authors
        return updated_authors

