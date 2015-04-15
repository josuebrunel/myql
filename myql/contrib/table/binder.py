from  base import Base, BaseInput, BasePaging, BaseBinder
from xml.etree import cElementTree as xtree

class Binder(BaseBinder):

    def __init__(self, name, itemPath, produces, pollingFrequencySeconds=0, urls=[], inputs=[], paging=None): 

        super(Binder, self).__init__(name, itemPath=itemPath, produces=produces, pollingFrequencySeconds=0, urls=urls, inputs=inputs, paging=paging)

        
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

