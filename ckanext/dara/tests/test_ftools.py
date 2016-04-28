import unittest
from ckanext.dara.ftools import list_dicter, dicter, grouper
from ckanext.dara.schema import author_fields



class TestFunctionalTools(unittest.TestCase):

    def setUp(self):
        self.seq = [u'Bunn', u'Derek W.', u'',
                u'http://d-nb.info/gnd/170390756', u'170390756', u'GND', u'',
                u'Manning', u'Alan', u'', u'http://d-nb.info/gnd/13188543X',
                u'13188543X', u'GND', u'']
        self.ids = map(lambda t: t.id, author_fields())

        
    def test_grouper(self):
        result = grouper(self.seq, len(self.ids))
        
        # for now only test if names are at the correct position
        # TODO: test all entries for correctness
        assert result.next()[0] == self.seq[0]
        assert result.next()[0] == self.seq[7]

    def test_dicter(self):
        seq = grouper(self.seq, len(self.ids))
        result = dicter(seq, self.ids)
        ts = result[0]
        ss = result[1]
        # TODO: test all seq items
        assert ts['firstname'] == self.seq[1]
        assert ts['lastname'] == self.seq[0]
        assert ss['firstname'] == self.seq[8]
        assert ss['lastname'] == self.seq[7]


    def test_list_dicter(self):
        pass

