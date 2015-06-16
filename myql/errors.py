class NoTableSelectedError(Exception):
    '''Error raised when no table has been selected
    '''
    def __init__(self, msg=None):
        if not msg:
            msg = 'No table selected'
        self.msg = msg

    def __str__(self):
        return repr(self.msg)
 
