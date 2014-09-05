class NoTableSelectedError(Exception):
  '''Error raised when no table has been selected
  '''
  def __init__(self, msg):
    self.msg = msg

  def __str__(self):
    return repr(self.msg)

class NoConfigFileError(Exception):
  '''Error raised when the config file passed
  doesn't exist 
  '''
  def __init__(self, msg):
    self.msg = msg

  def __str__(self,):
    return repr(self.msg)