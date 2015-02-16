from xml.etree import cElementTree as xtree

class Binder(object):
    """Class describing binders : select, insert, update, delete
        name : select, insert, update, delete
        itemPath : dotted path i.e : products.product
        produces : json or xml 
        urls : list of urls related to the api
        inputs : list of key object
    """

    def __init__(self, name, itemPath, produces, pollingFrequencySeconds=30, urls=[], inputs=[]):
        """Initializes the class
        """
        self.name = name
        self.itemPath = itemPath
        self.pollingFrequencySeconds = str(pollingFrequencySeconds)
        self.produces = produces

        # Builds the element tree
        self.etree = self._buildElementTree()

    def _buildElementTree(self,):
        """Builds ElementTree out of Binder object
        """
        t_binder = xtree.Element(self.name)

        for item in self.__dict__.items():
            t_binder.set(*item)

        return t_binder

    def addInput(self, key):
        """Add key element to the binder
        """
        root = self.etree

        t_input = root.find('inputs')

        if not t_input :
            t_input = xtree.SubElement(root, 'inputs')
        
        t_input.append(key.etree)
        
class BinderKey(object):
    """Class representing a key which is part of inputs
    """

    def __init__(self, id, type, paramType, required='false', like=''):
        """Initializes the class
        """
        self.id = id
        self.type = type
        self.paramType = paramType
        self.required = required

        self.etree = self._buildElementTree()

    def _buildElementTree(self,):
        """Turns object into ElementTre
        """
        t_key = xtree.Element('key')
        for item in self.__dict__.items():
            t_key.set(*item)
        
        return t_key
        
    def to_elementTree(self,):
        """Returns object as ElementTree
        """
        return self.etree



    
