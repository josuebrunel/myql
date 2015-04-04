import os, logging
import pdb
import unittest
from xml.dom import minidom
from xml.etree import cElementTree as xtree
from binder import Binder, BinderKey, BinderPage
from table import Table

import readline, rlcompleter
readline.parse_and_bind('tab: complete')

logging.basicConfig(level=logging.DEBUG,format="[%(asctime)s %(levelname)s] [%(funcName)s] %(message)s \n")

class TestTable(unittest.TestCase):

    def setUp(self,):
        self.table_desc = {
            'name': 'mytest',
            'author': 'josuebrunel',
            'apiKeyURL': 'http://josuebrunel.org/api',
            'documentationURL': 'http://josuebrunel.org/doc.html',
            'sampleQuery': 'SELECT * FROM mytable',
        }

        self.table = Table(**self.table_desc)

        self.binder_desc = {
            'name': 'select',
            'itemPath': 'products.product',
            'produces': 'xml'
        }

        self.binder = Binder(**self.binder_desc)
        self.binder_insert = Binder('insert','products.product','json')

        self.key_desc = {
            'id': 'artist',
            'type': 'xs:string',
            'paramType': 'path'
        }

        self.key = BinderKey(**self.key_desc)
        self.key2 = BinderKey(id='song', type='xs:string', paramType='path', required='true')

        start= {'id': 'ItemPage', 'default': '1'}
        pageSize= {'id':'Count' ,'max':'25'}
        total= {'default': '10'}
        self.paging = BinderPage('page', start, pageSize, total)

    def xml_pretty_print(self, data):
        """Pretty logging.debug xml data
        """
        raw_string = xtree.tostring(data, 'utf-8')
        parsed_string = minidom.parseString(raw_string)
        return parsed_string.toprettyxml(indent='\t')

    def test_add_binder(self,):
        self.assertEqual(self.table.addBinder(self.binder),True)
        logging.debug(self.xml_pretty_print(self.table.etree))

    def test_remove_binder(self,):
        self.binder.addInput(self.key)
        self.binder_insert.addInput(self.key)
        self.binder.addFunction('', from_file='tests_data/jscode.js')
        self.binder_insert.addFunction("console.log('hello this is an insert function'); ")
        self.table.addBinder(self.binder)
        self.table.addBinder(self.binder_insert)
        self.table.save(name='before', path='tests_data')
        self.assertEqual(os.path.isfile('tests_data/before.xml'),True)
        self.table.removeBinder('select')
        self.table.save(name='after', path='tests_data')
        self.assertEqual(os.path.isfile('tests_data/after.xml'),True)

    def test_add_input_to_binder(self,):
        self.assertEqual(self.binder.addInput(self.key),True)
        logging.debug(self.xml_pretty_print(self.binder.etree))

    def test_remove_input(self,):
        self.assertEqual(self.binder.addInput(self.key),True)
        self.assertEqual(self.binder.addInput(self.key2),True)
        logging.debug(self.xml_pretty_print(self.binder.etree))
        self.assertEquals(self.binder.removeInput(key_id='artist'),True)
        logging.debug(self.xml_pretty_print(self.binder.etree))

    def test_add_function_from_file(self,):
        self.assertEqual(self.binder.addFunction('', from_file='tests_data/jscode.js'),True)
        logging.debug(self.xml_pretty_print(self.binder.etree))

    def test_remove_function(self,):
        self.assertEqual(self.binder.addFunction('', from_file='tests_data/jscode.js'),True)
        logging.debug(self.xml_pretty_print(self.binder.etree))
        self.assertEqual(self.binder.removeFunction(), True)
        logging.debug(self.xml_pretty_print(self.binder.etree))

    def test_add_paging(self,):
        logging.debug(self.xml_pretty_print(self.binder.etree))
        self.assertEquals(self.binder.addPaging(self.paging), True)
        logging.debug(self.xml_pretty_print(self.binder.etree))

    def test_remove_paging(self,):
        logging.debug(self.xml_pretty_print(self.binder.etree))
        self.assertEquals(self.binder.addPaging(self.paging), True)
        logging.debug(self.xml_pretty_print(self.binder.etree))
        self.assertEqual(self.binder.removePaging(), True)
        logging.debug(self.xml_pretty_print(self.binder.etree))

    def test_add_url(self,):
        url = 'http://josuebrunel.org/service.js'
        self.assertEquals(self.binder.addUrl(url), True)
        logging.debug(self.binder.urls)
        logging.debug(self.xml_pretty_print(self.binder.etree))

    def test_remove_url(self,):
        url = 'http://josuebrunel.org/service.js'
        url2 = 'http://google.com'
        self.assertEquals(self.binder.addUrl(url), True)
        self.assertEquals(self.binder.addUrl(url2), True)
        logging.debug(self.xml_pretty_print(self.binder.etree))
        self.assertEquals(self.binder.removeUrl(url), True)
        logging.debug(self.xml_pretty_print(self.binder.etree))

    def test_save_file(self,):
        self.table.save()
        self.assertEquals(os.path.isfile('mytest.xml'),True) 

    def test_save_with_another_name(self):
        name = "tests_data/toto"
        self.table.save(name)
        self.assertEquals(os.path.isfile(name+'.xml'),True)

    def test_save_to_different_location(self,):
        fname = "titi"
        path = 'tests_data'
        name = os.path.join(path,fname)
        self.table.save(name=fname, path=path)
        self.assertEquals(os.path.isfile(name+'.xml'),True)

    def test_create_table(self,):
        self.binder.addInput(self.key)
        self.binder.addFunction('', from_file='tests_data/jscode.js')
        self.table.addBinder(self.binder)
        self.table.save(name='mytable', path='tests_data')
        self.assertEqual(os.path.isfile('tests_data/mytable.xml'),True)

    def test_create_table_and_add_two_binders(self,):
        self.binder.addInput(self.key)
        self.binder_insert.addInput(self.key)
        self.binder.addFunction('', from_file='tests_data/jscode.js')
        self.binder_insert.addFunction("console.log('hello this is an insert function'); ")
        self.table.addBinder(self.binder)
        self.table.addBinder(self.binder_insert)
        self.table.save(name='mytable', path='tests_data')
        self.assertEqual(os.path.isfile('tests_data/mytable.xml'),True)

    def test_create_table_with_binder(self,):
        self.binder.addInput(self.key)
        self.binder.addFunction('', from_file='tests_data/jscode.js')
        self.table_desc['bindings'] = [self.binder]
        table = Table(**self.table_desc)
        table.save(name='mytable', path='tests_data')
        self.assertEqual(os.path.isfile('tests_data/mytable.xml'),True)

    def test_add_function_table(self):
        logging.debug(self.xml_pretty_print(self.table.etree))
        self.assertEquals(self.table.addFunction('', from_file='tests_data/jscode.js'),True)
        logging.debug(self.xml_pretty_print(self.table.etree))

    def test_remove_function_table(self,):
        logging.debug(self.xml_pretty_print(self.table.etree))
        self.assertEquals(self.table.addFunction('', from_file='tests_data/jscode.js'),True)
        logging.debug(self.xml_pretty_print(self.table.etree))
        self.assertEquals(self.table.removeFunction(),True)
        logging.debug(self.xml_pretty_print(self.table.etree))

    def tearUp(self):
        os.path.unlink('tests_data/mytest.xml')
        os.path.unlink('tests_data/toto.xml')
        
if '__main__' == __name__:
    unittest.main()

