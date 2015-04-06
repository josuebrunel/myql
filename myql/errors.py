class NoTableSelectedError(Exception):
  '''Error raised when no table has been selected
  '''
  def __init__(self, msg=None):
    if not msg:
      msg = 'No table selected'
    self.msg = msg

  def __str__(self):
    return repr(self.msg)

class NoConfigFileError(Exception):
  '''Error raised when the config file passed
  doesn't exist 
  '''
  def __init__(self, msg=None):
    if not msg:
      msg = 'Config file is invalid or doesn\'t exist'

    self.msg = msg

  def __str__(self,):
    return repr(self.msg)


class NoConfigParameter(Exception):
  '''Error raised when config parameters don't exist
  '''
  def __init__(self, msg=None):
    if not msg:
      msg = 'Invalid config parameters'

    self.msg = msg

  def __str__(self,):
    return repr(self.msg)
  
