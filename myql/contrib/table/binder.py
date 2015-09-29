from  myql.contrib.table.base import BaseInput, BasePaging, BaseBinder

class Binder(BaseBinder):
    """Represent a binder : <select>, <insert>, <update>, <delete> 
    """
    def __init__(self, name, itemPath, produces, pollingFrequencySeconds=0, urls=[], inputs=[], paging=None): 

        super(Binder, self).__init__(name, itemPath=itemPath, produces=produces, pollingFrequencySeconds=pollingFrequencySeconds, urls=urls, inputs=inputs, paging=paging)

        
class BinderFunction(BaseBinder):
    """Represent a function : <function>
    """

    def __init__(self, func_name, func_code='', func_file=None, inputs=[]):
        """
        - func_name : name of the stored procedure
        - func_code : your js code passed through a str
        - func_file : file containing your code
        """
        super(BinderFunction, self).__init__('function', inputs=inputs)
        self.func_name = func_name
        self.etree.set('name', func_name)

        if func_code:
            self.addFunction(func_code)

        if func_file:
            self.addFunction('', from_file=func_file)


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
    """Class representing <paging model='page'>
    """
    def __init__(self, start, pageSize, total):
        super(PagingPage, self).__init__('page', start=start, pageSize=pageSize, total=total)


class PagingOffset(BasePaging):
    """Class representing <paging model='offset' matrix='true'>
    """
    def __init__(self, matrix, start, pageSize, total):
        super(PagingOffset, self).__init__('offset', matrix, start=start, pageSize=pageSize, total=total)
        self.matrix = str(matrix).lower()
        self.etree.set('matrix', self.matrix)
        

class PagingUrl(BasePaging):
    """Class representing <paging model='url'>
    """
    def __init__(self, nextpage):
        super(PagingUrl, self).__init__('url', nextpage=nextpage)
       

class BinderMeta(type):

    INPUT_KEYS = ['name', 'itemPath', 'produces', 'pollingFrequencySeconds', 'urls', 'keys', 'pages']

    def __new__(cls, name, bases, dct):

        if name != 'BinderModel':
            binder_attr = {key: value for (key, value) in dct.items() if key in cls.INPUT_KEYS}
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
        return super(BinderMeta,cls).__new__(cls, name, bases, dct)


class BinderModel(Binder):
    __metaclass__ = BinderMeta

