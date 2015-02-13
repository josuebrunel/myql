from xml.etree import cElementTree as xtree

class YqlTable(object):
    """Class representating a YQL Table
    """

    _TAB_ATTR = {'xmlns':'', 'securityLevel':'any', 'https':'false'}

    def __init__(self, name, author, apiKeyURL, documentationURL, sampleQuery, description=None, table_attr=None):
        """Initialize the class
        """
        self.name = name
        self.author = author
        self.apiKey = apiKeyURL
        self.documentationURL = documentationURL
        self.description = description
        self.sampleQuery = sampleQuery
        self.table_attr = table_attr

    def _create_table_xml_file(self, data):
        """Creates a xml file of the table
        """
        import pdb
        pdb.set_trace()
        content = xtree.tostring(data, pretty_print= True)

        with open(self.name+".xml", 'w') as f:
            f.write(content)


    def save(self, xml=True, db_table=True):
        """Create a table 
        """
        # <table> tag object
        t_table =  xtree.Element('table')
        # <table xmlns='' securityLevel='' htpps=''>
        if not self.table_attr :
            self.table_attr = self._TAB_ATTR
        for attr in self.table_attr.items() :
            t_table.set(*attr)
        
        self._create_table_xml_file(t_table)
    
        
