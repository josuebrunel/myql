from xml.etree import cElementTree as ctree

class Base(object):

    def addElement(self, elt, tagName=None):
        root = self.etree
        t_elt = root.find(tagName)
        if not t_elt:
            t_elt = ctree.SubElement(root, tagName)

        root.append(t_elt)
        return True

    def removeElement(self, elt, tagName=None):
        root = self.etree
        t_elt = root.find(tagName)

        try:
            root.remove(t_elt)
            return True
        except Exception,e:
            print(e)

        return False

    def addFunction(self, func_code, from_file=''):
        """Add function 
        """
        if from_file:
            with open(from_file) as f:
                func_code = f.read()

        root = self.etree
        t_execute = root.find('execute')

        if not t_execute :
            t_execute = ctree.SubElement(root, 'execute')

        t_execute.text = "\n\t![CDATA]{0:>5}]]\n\t".format(func_code.ljust(4))

        return True

    def removeFunction(self):
        """Remove function tag
        """
        root = self.etree
        t_execute = root.find('execute')
        try:
            root.remove(t_execute)
            return True
        except Exception,e:
            print(e)

        return False

class BaseInput(object):
    """This class represents an Input Element under Binding element.
    Input Element can be : <key>, <value> or <map>
    Full Documentation https://developer.yahoo.com/yql/guide/yql-opentables-reference.html#yql-opentables-key
    """

    def __init__(self, input_type, id, type, paramType, like='', required=False, default='', private=False, const=False, batchable=False, maxBatchItems=1):
        """
        - input_type : can be <key>, <value> or <map>
        - id : The name of the key. This represents what the user needs to provide in the WHERE clause.
        - like (as):  The alias of the key used in YQL statements.
        - type : The type of data coming back from the Web service.
        - required : A boolean that answers the question
        - paramType : Determines how this key is represented and passed on to the Web service.
        - default : This value is used if one isn't specified by the developer in the SELECT.
        - private : Hide this key's value to the user (in both "desc" and "diagnostics"). 
        - const : A boolean that indicates whether the default attribute must be present and cannot be changed by the end user.
        - batchable : A boolean which answers the question: Does this select and URL support multiple key fetches/requests in a single request (batched fetching)?
        - maxBatchItems : How many requests should be combined in a single batch call. 
        """
        self.name = input_type
        self.id = id
        self.like = like # as is a python <keyword>, that's why in argument we use <like>
        self.type = type
        self.required = required
        self.default = default
        self.private = private
        self.const = const
        self.batchable = batchable
        self.maxBatchItems = maxBatchItems

        self.etree = self._buildElementTree()

    def _buildElementTree(self,):
        """Turn object into an ElementTree
        """
        t_elt = ctree.Element(self.name)

        for k,v in [ (key,value) for key,value in self.__dict__.items() if key != 'name']: # Excluding name from list of items
            if v and v != 'false' :
                t_elt.set(k if k != 'like' else 'as', str(v).lower())

        self._etree = t_elt
        return t_elt

class BasePaging(object):
    """Class representing a <paging> element under a <select> element of a OpenTable file description
    """

    #def __init__(self, model, start={}, pagesize={}, total={}, nextpage={}):
    def __init__(self, model, *args, **kwargs):

        kwargs['model'] = model
        vars(self).update(kwargs)
        
        self.etree = self._buildElementTree()

    def _buildElementTree(self,):
        """Turn object into an Element Tree
        """

        t_paging = ctree.Element('paging')
        t_paging.set('model', self.model)
        for key in self.__dict__.keys():
            if key != 'model':
                t_tag = ctree.SubElement(t_paging, key)
                for item in self.__dict__[key].items():
                    t_tag.set(*item)

        self.etree = t_paging
        return  t_paging
