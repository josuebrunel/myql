import unittest

from lokingyql import lokingyql

class lokingyqlTestCase(unittest.TestCase):
  
  def setUp(self,):
    self.yql = lokingyql()

  def tearUp(self,):
    pass

if __name__ == "__main__":
  unittest.main()
