import unittest
from app.models import Comment,Blog
from app import db
class TestBlogComment(unittest.TestCase):

  def setUp(self):
    self.new_blog =Blog(content ="try it")
    self.new_comment=Comment(comment= "very nice", blogs=self.new_blog)


  def test_instance(self):
      self.assertTrue(isinstance(self.new_comment,Comment))

  def test_check_instance_variables(self):
    self.assertEquals(self.new_comment.comment,"very nice")
    self.assertEquals(self.new_comment.blogs,self.new_blog,'try it')