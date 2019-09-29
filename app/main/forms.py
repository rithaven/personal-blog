from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, SelectField, RadioField
from wtforms.validators import Required

class CommentsForm(FlaskForm):
      comment = TextAreaField('Comment', validators=[Required()])
      vote=RadioField('default field arguments', choices=[('1', 'Upvote'),('1', 'DownVote')])
      submit = SubmitField('SUBMIT')

class UpdateProfile(FlaskForm):
     bio = TextAreaField('Tell us about you.', validators =[Required()])
     submit = SubmitField('Submit')

class BlogForm(FlaskForm):
     category_id= SelectField('Select Category', choices=[('1','Interview'),('2','Pick Up Lines'),('3','Promotion'),('4','Production')])
     content = TextAreaField('YOUR Blog')
     submit = SubmitField('CreateBlog')

class UpvoteForm(FlaskForm):
     '''
     Class to create a wtf form for upvoting a Blog
     '''

     submit = SubmitField('Upvote')
