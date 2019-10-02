from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class CommentsForm(FlaskForm):
      comment = TextAreaField('Comment', validators=[Required()])
      submit = SubmitField('SUBMIT')

class UpdateProfile(FlaskForm):
     bio = TextAreaField('Tell us about you.', validators =[Required()])
     submit = SubmitField('Submit')

class BlogForm(FlaskForm):
     content = TextAreaField('YOUR Blog')
     submit = SubmitField('CreateBlog')
class UpdateBlogForm(FlaskForm):
     title = StringField('Title',validators = [Required()])
     content = TextAreaField('Content', validators = [Required()])
     submit = SubmitField('submit')
