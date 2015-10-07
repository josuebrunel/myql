import os
from xml.dom import minidom
from xml.etree import cElementTree as xtree

from myql.contrib.table.base import Base
from myql.contrib.table.binder import Binder, BinderFunction

class Table(Base):
    """Class representating a YQL Table
    """

    _TAB_ATTR = {'xmlns':'http://query.yahooapis.com/v1/schema/table.xsd', 'securityLevel':'any', 'https':'false'}

    def __init__(self, name, author, apiKeyURL, documentationURL, sampleQuery=[], description=None, table_attr=None, bindings=[]):
        """Initialize the class
        """
        self.name = name
        self.author = author
        self.apiKey = apiKeyURL
        self.documentationURL = documentationURL
        self.description = description
        self.sampleQuery = sampleQuery
        self.table_attr = table_attr
        self.etree = self._init_table_elementTree()
        self.bindings = bindings

        if bindings:
            [ self.addBinder(binder) for binder in bindings ]

    def __repr__(self,):
        return "<Table:{0}>".format(self.name)

    def _xml_pretty_print(self, data):
        """Pretty print xml data
        """
        raw_string = xtree.tostring(data, 'utf-8')
        parsed_string = minidom.parseString(raw_string)
        return parsed_string.toprettyxml(indent='\t')

    def _create_table_xml_file(self, data, fname=None):
        """Creates a xml file of the table
        """
        content = self._xml_pretty_print(data)
        if not fname:
            fname = self.name
        with open(fname+".xml", 'w') as f:
            f.write(content)

    def _init_table_elementTree(self, xml=True, db_table=True):
        """Create a table 
        """
        # <table> tag object
        t_table =  xtree.Element('table')
        # <table xmlns='' securityLevel='' htpps=''>
        if not self.table_attr :
            self.table_attr = self._TAB_ATTR
        for attr in self.table_attr.items() :
            t_table.set(*attr)

        # <meta>
        t_meta = xtree.SubElement(t_table, 'meta')

        # Loop over a sorted key,value of class attributes while ignoring table_attr and name
        for key, value in [(k,v) for k,v in sorted(self.__dict__.items(), key=lambda x: x[0]) if k not in ('table_attr','name') ]:
            if isinstance(value, list): # Works for element like sampleQuery
                for elt in value:
                    t_tag = xtree.SubElement(t_meta, key) # setting attribute name as a tag name
                    t_tag.text = elt # Setting attribute  value as text
            else:
                t_tag = xtree.SubElement(t_meta,key)
                t_tag.text = value
      
        ## <bindings>
        t_bindings = xtree.SubElement(t_table, 'bindings')
        ##

        self.etree = t_table
        return t_table

    def save(self, name=None, path=None):
        """Save file as xml
        """
        if path :
            name = os.path.join(path,name)

        try:
            self._create_table_xml_file(self.etree, name)
        except (Exception,) as e:
            print(e)
            return False

        return True

    def addBinder(self, binder):
        """Adds a binder to the file
        """
        root = self.etree
        bindings = root.find('bindings')
        bindings.append(binder.etree)

        return True

    def removeBinder(self, name):
        """Remove a binder from a table
        """
        root = self.etree
        
        t_bindings = root.find('bindings')
        
        t_binder = t_bindings.find(name)

        if t_binder :
            t_bindings.remove(t_binder)
            return True
        
        return False

    
class TableMeta(type):

    TABLE_KEYS = ['name', 'author', 'apiKeyURL', 'documentationURL', 'sampleQuery','description']

    def __new__(cls, name, bases, dct):
        if name != 'TableModel':
            table_attr = {key: value for (key, value) in dct.items() if key in cls.TABLE_KEYS }
            table_attr['bindings'] = [ value for value in dct.values() if isinstance(value, Binder) or isinstance(value, BinderFunction)]
            table = Table(**table_attr)
            dct = { key : value for (key, value) in dct.items() if key in ('__module__', '__metaclass__')}
            dct['table'] = table

        return super(TableMeta, cls).__new__(cls, name, bases, dct)


class TableModel(Table):
    __metaclass__ = TableMeta


def BinderFrom(cls_binder_meta):
    return cls_binder_meta.binder

