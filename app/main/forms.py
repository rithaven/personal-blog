from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError
from wtforms.validators import Required,Email
from ..models import Subscription
class CommentsForm(FlaskForm):
     #  title = StringField('Title',validators = [Required()])
      comment = TextAreaField('Comment', validators=[Required()])
      submit = SubmitField('SUBMIT')

class UpdateProfile(FlaskForm):
     title = StringField('Title',validators = [Required()])
     bio = TextAreaField('Tell us about you.', validators =[Required()])
     submit = SubmitField('Submit')

class BlogForm(FlaskForm):
     # title = StringField('Title',validators = [Required()])
     content = TextAreaField('YOUR Blog')
     submit = SubmitField('CreateBlog')
class UpdateBlogForm(FlaskForm):
     # title = StringField('Title',validators = [Required()])
     content = TextAreaField('Content', validators = [Required()])
     submit = SubmitField('submit')

class SubscriptionForm(FlaskForm):
     name=StringField('Name',validators=[Required()])
     email=StringField('Email',validators=[Required(),Email()])
     submit =SubmitField('Submit')
     def validate_email(self,data_field):
          if Subscription.query.filter_by(email =data_field.data).first():
               raise ValidationError('There is an account with that email')

     def validate_name(self,data_field):
          if Subscription.query.filter_by(name =data_field.data).first():
               raise ValidationError('That name is taken')
