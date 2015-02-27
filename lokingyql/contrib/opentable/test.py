import pdb
from xml.etree import cElementTree as xtree
from binder import Binder, BinderKey
from yqltable import YqlTable

import readline, rlcompleter
readline.parse_and_bind('tab: complete')

def dump(data):
    print xtree.tostring(data.etree)

stuff = {
    'name': 'mytest',
    'author': 'josuebrunel',
    'apiKeyURL': 'http://josuebrunel.org/api',
    'documentationURL': 'http://josuebrunel.org/doc.html',
    'sampleQuery': 'SELECT * FROM mytable',
}

select = {
    'name': 'select',
    'itemPath': 'products.product',
    'produces': 'xml'
}
insert = {
    'name': 'insert',
    'itemPath': 'products.product',
    'produces': 'json'
}

b_select = Binder(**select)
b_insert = Binder(**insert)

key = {
    'id': 'artist',
    'type': 'xs:string',
    'paramType': 'path'
}

b_key = BinderKey(**key)

b_select.addInput(b_key)
b_insert.addInput(b_key)

function = "type your code here"

b_select.addFunction(function, from_file='jscode.js')

stuff['bindings']=[b_select, b_insert]

table = YqlTable(**stuff)
#table.save()

table.addBinder(b_select.etree)

#pdb.set_trace()
