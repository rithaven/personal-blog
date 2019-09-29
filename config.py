import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = 'Rithakv'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wecode:1234@localhost/blog'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    QUOTES_URL='http://quotes.stormconsultancy.co.uk/random.json'
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587 
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'One Minute blog'
    SENDER_EMAIL = 'enkakane@gmail.com'

    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://wecode:1234@localhost/blog'


class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    DEBUG = True
class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}