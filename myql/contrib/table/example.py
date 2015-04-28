from binder import BinderModel, InputKey, PagingPage, PagingUrl, InputValue, BinderFunction
from table import TableModel, BinderFrom

class SelectBinder(BinderModel):
    name = 'select'
    itemPath = 'products.product'
    produces = 'xml'
    pollingFrequencySeconds = 30
    urls = ['http://lol.com/services?artist={artis}','http://lol.com/services/song={song}']
    paging = PagingPage({'id': 'ItemPage', 'default': '1'}, {'id':'Count' ,'max':'25'},{'default': '10'})
    artist = InputKey(id='artist', type='xs:string', paramType='path')
    song = InputKey(id='song', type='xs:string', paramType='path', required=True)

class InsertBinder(BinderModel):
    name = 'insert'
    itemPath = 'products.product'
    produces = 'xml'
    pollingFrequencySeconds = 30
    urls = ['http://lol.com/services?artist={artis}','http://lol.com/services/song={song}']
    paging = PagingUrl(nextpage={'path':'yqlsearch.nextpage'})
    artist = InputKey(id='artist', type='xs:string', paramType='path')
    song = InputValue(id='song', type='xs:string', paramType='path', required=True)
    

class TestTable(TableModel):
    name = 'Test'
    author = 'Josue Kouka'
    apiKeyURL = 'http://josuebrunel.org/api'
    documentationURL = 'http://josuebrunel.org/doc.html'
    description = "Just a test table"
    sampleQuery = ['SELECT * FROM mytable','SELECT name FROM mytable WHERE id=4656', "SELECT * FROM mytable WHERE name='Josh'"]
    select = BinderFrom(SelectBinder)
    insert = BinderFrom(InsertBinder)
    func1 = BinderFunction('concat', func_code="console.log('Hello Josh!!!')")

TestTable.table.save(name='Example')
