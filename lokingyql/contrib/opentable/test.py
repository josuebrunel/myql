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

b_select = Binder(**select)

key = {
    'id': 'artist',
    'type': 'xs:string',
    'paramType': 'path'
}

b_key = BinderKey(**key)

b_select.addInput(b_key)

pdb.set_trace()

#table = YqlTable(**stuff)
#table.save()
