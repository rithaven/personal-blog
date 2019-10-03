import unittest
from app.models import User

class UserModelTest(unittest.TestCase)
    '''
    Test class to test behaviours of the [Class] class
    Args:
         unittest.TestCase: Test case class that helps create test cases
    '''
    
    def setUp(self):
      '''
      Set up method that will run before avery Test
      '''
      self.user= User(password = 'twenty')

    def test_password_setter(self):
      self.asserTrue(self.writer.pass_secure is not None)

    def test_no_access_password(self):
      with self.assertRaises(AttributeError):
        self.writer.password

    def test_password_verification(self):
      self.assertTrue(self.writer.verify_password('aggy'))

  