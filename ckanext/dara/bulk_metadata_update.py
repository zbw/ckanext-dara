"""
    Script to update metadata in the JDA for fields that exist
"""
import ast
import requests


class BulkUpdater:
    def __init__(self, base='http://www.journaldata.zbw.eu/api/3/action/{action}'):
        self.base = base
        self.lookup_base = 'http://zbw.eu/beta/econ-ws/suggest2?dataset=econ_corp&query={name}'
        self.errors = []
        self.packages = self.get_packages


    def get_packages(self):
        """ return list of packages """
        url = self.base.format(action='package_list')
        packages = requests.get(url).json()['result']
        return packages


    def get_package(self, package):
        """ get data for one package """
        url = self.base.format(action='package_show') + '?id={package}'.format(package=package)
        data = requests.get(url).json()['result']
        return data


    def update_package(self, package):
        """ update a packages affilID """
        data = self.get_package(package)
        try:
            authors = ast.literal_eval(data['dara_authors'])
            for author in authors:
                if author['affil'] != '':
                    affil_id = lookup(author['affil'])
                    #print("{}: {}".format(author['affil'], affil_id))
                    if 'affilID' in author.keys():
                        print('Dont add anything')
                    else:
                        if affil_id is not False:
                            author['affilID'] = affil_id
                else:
                    pass
        except Exception as e:
            self.errors.append(data['id'])


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

            if unicode(name, 'utf-8') == prefLabel or unicode(name, 'utf-8') == prefName:
                return b_id

        return False
