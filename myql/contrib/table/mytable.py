import pdb

try:
    from myql.contrib.table import BinderMeta, TableMeta, BinderModel, BinderKey, BinderPage, TableModel
except:
    from binder import BinderModel, BinderPage, BinderKey
    from table import TableModel

class SelectBinder(BinderModel):
    name = 'select'
    itemPath = 'products.product'
    produces = 'xml'
    pollingFrequencySeconds = 30
    urls = ['http://lol.com/services?artist=$','http://lol.com/services/song=$']
    paging = BinderPage('page', {'id': 'ItemPage', 'default': '1'}, {'id':'Count' ,'max':'25'},{'default': '10'})
    artist = BinderKey(id='artist', type='xs:string', paramType='path')
    song = BinderKey(id='song', type='xs:string', paramType='path', required='true')
    

class TestTable(TableModel):
    name = 'Test'
    author = 'Josue Kouka'
    apiKeyURL = 'http://josuebrunel.org/api'
    documentationURL = 'http://josuebrunel.org/doc.html'
    sampleQuery = 'SELECT * FROM mytable'
    select = SelectBinder


print(TestTable.toxml())
