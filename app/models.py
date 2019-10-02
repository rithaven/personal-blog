from . import db 
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime 



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True) 
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    
    blog = db.relationship('Blog',backref = 'users',lazy="dynamic")
    # comments = db.relationship('Comment', backref='users', lazy='dynamic')

    @classmethod
    def get_comments(cls,id):
        reviews = Comment.query.filter_by(blog_id=id).all()
        return comments

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
            return check_password_hash(self.pass_secure, password)
    
    def save_user(self):
        db.session.add(self)
        db.session.commit()
    def save_comment(self):
        '''
        Function that saves comments
        '''
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'User {self.username}'

class Blog(db.Model):
    '''
    Blog class to define Blog Objects
    '''
    __tablename__ = 'blog'

    id = db.Column(db.Integer,primary_key = True)
    blog = db.Column(db.String)
    
    # time=db.Column(db.Datetime,nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comments = db.relationship('Comment',backref = 'blog',lazy="dynamic")
        

    def save_blog(self):
        '''
        Function that saves blogs
        '''
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_all_blogs(cls):
        '''
        Function that queries the databse and returns all the blogs
        '''
        return Blog.query.all()

    def update_blog(self,id):
        blogs = Blog.query.filter_by(id = id).all()

        db.session.update(self)
        db.session.commit()

    def __repr__(self):
        return f'Blog {self.blog}'

    def delete_blog(self,id):
        blogs = Blog.query.filter_by(id = id).all()
        
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'Blog {self.blog}'
  



class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    comment= db.Column(db.String)
    blog_id = db.Column(db.Integer,db.ForeignKey('blog.id'))
    username =  db.Column(db.String)
   
    

    def save_comment(self):
        '''
        Function that saves comments
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_comments(cls):
        Comment.all_comments.clear()

    @classmethod
    def get_comments(cls,id):
        comments = Comment.query.filter_by(blog_id=id).all()

        return comments
    @classmethod
    def delete_comment(self):
        comments = Comment.query.filter_by(id= id).all()
        # for comment in comments:
        #     db.session.delete(comment)
        #     db.session.commit()
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'Comment{self.comment}'

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic") 

    def __repr__(self):
        return f'User {self.name}'  
class Quotes:
    '''
    Quotes class to define Quotes Objects
    '''

    def __init__(self,author,quote):

        self.author = author
        self.quote = quote

class Subscription(db.Model):
    __tablename__='subscribes'

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(255))
    email=db.Column(db.String(255),unique=True, index=True)
    def __repr__(self):
        return f'{self.email}'
       



