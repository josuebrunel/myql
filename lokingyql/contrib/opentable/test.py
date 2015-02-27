import pdb
import unittest

from xml.etree import cElementTree as xtree
from binder import Binder, BinderKey
from yqltable import YqlTable

import readline, rlcompleter
readline.parse_and_bind('tab: complete')

class TestYqlTable(unittest.TestCase):

    def setUp(self,):
        self.table_desc = {
            'name': 'mytest',
            'author': 'josuebrunel',
            'apiKeyURL': 'http://josuebrunel.org/api',
            'documentationURL': 'http://josuebrunel.org/doc.html',
            'sampleQuery': 'SELECT * FROM mytable',
        }

        self.table = YqlTable(**self.table_desc)

        self.binder_desc = {
            'name': 'select',
            'itemPath': 'products.product',
            'produces': 'xml'
        }

        self.binder = Binder(**self.binder_desc)

        self.key_desc = {
            'id': 'artist',
            'type': 'xs:string',
            'paramType': 'path'
        }

        self.key = BinderKey(**self.key_desc)

    def test_add_binder(self,):
        self.assertEqual(self.table.addBinder(self.binder),True)

    def test_add_input_to_binder(self,):
        self.assertEqual(self.binder.addInput(self.key),True)

    def test_add_function_from_file(self,):
        self.assertEqual(self.binder.addFunction('', from_file='jscode.js'),True)

    def tearUp(self,):
        pass

if '__main__' == __name__:
    unittest.main()





