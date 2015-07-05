from xml.etree import cElementTree as ctree

class Base(object):

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
        except (Exception,) as e:
            print(e)

        return False


class BaseBinder(Base):
    """Represents any element under <bindings> : <select>,<insert>,<update>,<delete> and <function>
    """
    def __init__(self, name, **kwargs):
        """
        """
        self.name = name
        vars(self).update(kwargs)

        self.etree = self._buildElementTree()

        if vars(self).get('urls',None):
            [ self.addUrl(url) for url in self.urls ]

        if vars(self).get('inputs',None):
            [ self.addInput(elt) for elt in self.inputs ]

        if vars(self).get('paging',None):
            self.addPaging(self.paging)
        
    def _buildElementTree(self,):
        """Turns object into a Element Tree
        """
        t_binder = ctree.Element(self.name)

        for k,v in self.__dict__.items():
            if k not in ('name', 'urls', 'inputs', 'paging') and v :
                t_binder.set(k,v)

        self.etree = t_binder
        return t_binder

    def addUrl(self, url):
        """Add url to binder
        """

        if url not in self.urls:
            self.urls.append(url)

        root = self.etree
        t_urls = root.find('urls')

        if not t_urls:
            t_urls = ctree.SubElement(root, 'urls')

        t_url = ctree.SubElement(t_urls, 'url')
        t_url.text = url

        return True

    def removeUrl(self, url):
        """Remove passed url from a binder
        """

        root = self.etree
        t_urls = root.find('urls')

        if not t_urls:
            return False

        for t_url in t_urls.findall('url'):
            if t_url.text == url.strip():
                t_urls.remove(t_url)
                if url in self.urls:
                    self.urls.remove(url)
                return True

        return False

    def addInput(self, key):
        """Add key to input : key, value or map
        """
        if key not in self.inputs:
            self.inputs.append(key)

        root = self.etree
        t_inputs = root.find('inputs')

        if not t_inputs :
            t_inputs = ctree.SubElement(root, 'inputs')

        t_inputs.append(key.etree)

        return True

    def removeInput(self, key_id, input_type='key'):
        """Remove key (key, value, map) from Input
        key_id : id of the input element i.e <key id='artist' />
        input_type : type of the input ; key, value or map
        """
        root = self.etree
        t_inputs = root.find('inputs')

        if not t_inputs:
            return False

        keys = t_inputs.findall(input_type)

        key = [ key for key in keys if key.get('id') == key_id ]

        try:
            t_inputs.remove(key[0])
            return True
        except (Exception,) as e:
            print(e)

        return False

    def addPaging(self,paging):
        """Add paging to Binder
        """
        if not vars(self).get('paging', None):
            self.paging = paging
        root = self.etree

        try:
            root.append(paging.etree)
            return True
        except (Exception,) as e:
            print(e)

        return False

    def removePaging(self,):
        """Remove paging from Binder
        """
        root = self.etree
        t_paging = root.find('paging')

        try:
            root.remove(t_paging)
            return True
        except (Exception,) as e:
            print(e)

        return False


class BaseInput(object):
    """This class represents an Input Element under Binding element.
    Input Element can be : <key>, <value> or <map>
    Full Documentation https://developer.yahoo.com/yql/guide/yql-opentables-reference.html#yql-opentables-key
    """

    def __init__(self, input_type, id, type, paramType, like='', required=False, default='', private=False, const=False, batchable=False, maxBatchItems=0):
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
        self.paramType = paramType
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
