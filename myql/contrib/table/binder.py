from  base import Base, BaseInput, BasePaging
from xml.etree import cElementTree as xtree

class Binder(Base):
    """Class describing binders : select, insert, update, delete
        name : select, insert, update, delete
        itemPath : dotted path i.e : products.product
        produces : json or xml 
        urls : list of urls related to the api
        inputs : list of InputKey object
    """

    def __init__(self, name, itemPath, produces, pollingFrequencySeconds=30, urls=[], inputs=[], paging=None):
        """Initializes the class
        """
        self.name = name
        self.itemPath = itemPath
        self.pollingFrequencySeconds = str(pollingFrequencySeconds)
        self.produces = produces
        self.urls = urls
        self.inputs = inputs
        self.paging = paging

        # Builds the element tree
        self.etree = self._buildElementTree()

        # Adding urls
        if urls:
            [ self.addUrl(url) for url in urls ]

        # Adding inputs passed as parameters
        if inputs:
            [ self.addInput(key) for key in inputs ]

        # Adding paging
        if paging:
            self.addPaging(paging)

    def __repr__(self):
        return "<Binder:{0}>".format(self.name)

    def _buildElementTree(self,):
        """Builds ElementTree out of Binder object
        """
        t_binder = xtree.Element(self.name)

        for item in self.__dict__.items():
            if item[0] not in ('name', 'inputs', 'urls', 'paging'):
                t_binder.set(*item)

        return t_binder

    def addUrl(self, url):
        """Adds url to binder
        """
        if not url in self.urls:
            self.urls.append(url)

        root = self.etree

        t_urls = root.find('urls')
        if not t_urls:
            t_urls = xtree.SubElement(root, 'urls')

        t_url = xtree.SubElement(t_urls, 'url')
        t_url.text = url 

        return True

    def removeUrl(self, url):
        """Removes a specified url of a binder
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
        """Add key element to the binder
        """
        if not key in self.inputs:
            self.inputs.append(key)
        root = self.etree

        t_input = root.find('inputs')

        if not t_input :
            t_input = xtree.SubElement(root, 'inputs')
        
        t_input.append(key.etree)

        return True

    def removeInput(self, key_id):
        """Removes an input from a binder
        """
        root = self.etree
        t_inputs = root.find('inputs')

        keys = t_inputs.findall('key')

        key = [ key for key in keys if key.get('id') == key_id ]

        try:
            t_inputs.remove(key[0])
            return True
        except Exception, e:
            print(e)
            return False 

    def addPaging(self, paging):
        """Adds paging to binder
        """
        if not self.paging: 
            self.paging = paging    

        root = self.etree
        try:
            root.append(paging.etree)
            return True
        except Exception, e:
            print(e)
        
        return False

    def removePaging(self,):
        """Removes paging from Binder
        """
        root = self.etree
        t_paging = root.find('paging')

        try:
            root.remove(t_paging)
            return True
        except Exception, e:
            print(e)

        return False

        
class InputKey(BaseInput):
    """Class representing a key of an Input
    """

    def __init__(self, *args, **kwargs):
        super(InputKey, self).__init__('key', *args, **kwargs)
        
class InputValue(BaseInput):
    """Class representing value under an Input
    """
    def __init__(self, *args, **kwargs):
        super(InputValue, self).__init__('value', *args, **kwargs)


class InputMap(BaseInput):
    """Class representing map under an Input
    """
    def __init__(self, *args, **kwargs):
        super(InputMap, self).__init__('map', *args, **kwargs)


class PagingPage(BasePaging):

    def __init__(self, start, pageSize, total):
        super(PagingPage, self).__init__('page', start=start, pageSize=pageSize, total=total)


class PagingOffset(BasePaging):

    def __init__(self, matrix, start, pageSize, total):
        super(PagingOffset, self).__init__('offset', matrix, start=start, pageSize=pageSize, total=total)
        self.matrix = str(matrix).lower()
        self.etree.set('matrix', self.matrix)
        

class PagingUrl(BasePaging):

    def __init__(self, nextpage):
        super(PagingUrl, self).__init__('url', nextpage=nextpage)
       

class BinderMeta(type):

    INPUT_KEY = ['name', 'itemPath', 'produces', 'pollingFrequencySeconds', 'urls', 'keys', 'pages']

    def __new__(cls, name, bases, dct):

        if name != 'BinderModel':
            binder_attr = {key: value for (key, value) in dct.items() if key in cls.INPUT_KEY}
            binder_attr['inputs'] = [ value for value in dct.values() if isinstance(value, BaseInput)]
            paging = [ value for value in dct.values() if isinstance(value, BasePaging)]
            if paging :
                binder_attr['paging'] = paging[0]

            binder = Binder(**binder_attr)
            if dct.get('function',None):
                binder.addFunction(func_code='', from_file=dct['function'])
            dct = { key : value for (key, value) in dct.items() if key in ('__module__', '__metaclass__')}
            dct['binder'] = binder
            # Add KeyException Management
        return super(BinderMeta,cls).__new__(cls, name, (Binder,), dct)

    def toxml(cls,):
        return xtree.tostring(cls.binder.etree)


class BinderModel(Binder):
    __metaclass__ = BinderMeta

