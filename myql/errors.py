class NoTableSelectedError(Exception):
    '''Error raised when no table has been selected
    '''
    def __init__(self, msg=None):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)
 
