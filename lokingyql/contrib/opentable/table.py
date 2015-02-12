from xml.etree import cElementTree

class Table(object):
    """Class representating a YQL Table
    """

    def __init__(self, name, author, apiKey, documentationURL, description, sampleQuery):
        """Initialize the class
        """
        self.name = name
        self.author = author
        self.apiKey = apiKey
        self.documentationURL = documentationURL
        self.description = description
        self.sampleQuery = sampleQuery


    def create_file(self, xml=True, db_table=True):
        """Create a table 
        """
        pass
