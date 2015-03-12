import os
from xml.dom import minidom
from xml.etree import cElementTree as xtree

class YqlTable(object):
    """Class representating a YQL Table
    """

    _TAB_ATTR = {'xmlns':'', 'securityLevel':'any', 'https':'false'}

    def __init__(self, name, author, apiKeyURL, documentationURL, sampleQuery, description=None, table_attr=None, bindings=[]):
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
        return "<YqlTable:{0}>".format(self.name)

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

        ## <author>
        t_author = xtree.SubElement(t_meta, 'author')
        t_author.text = self.author
        ##

        ## <apiKeyURL>
        t_apiKeyURL = xtree.SubElement(t_meta, 'apiKeyURL')
        t_apiKeyURL.text = self.apiKey
        ##

        ## <documentationURL>
        t_documentationURL = xtree.SubElement(t_meta, 'documentationURL')
        t_documentationURL.text = self.documentationURL
        ##

        ## <description>
        t_description = xtree.SubElement(t_meta, 'description')
        t_description.text = self.description
        ##

        ## <sampleQuery>
        t_sampleQuery = xtree.SubElement(t_meta, 'sampleQuery')
        t_sampleQuery.text = self.sampleQuery
        ##

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
        except Exception,e:
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

    def addFunction(self, func_code, from_file=None):
        """Adds function to a YQL Table
        """

        if from_file:
            with open(from_file) as f:
                func_code = f.read()

        root = self.etree

        t_execute = xtree.SubElement(root, 'execute')
        t_execute.text = "\n [!CDATA[ {0} ]]\n".format(func_code)

        return True

