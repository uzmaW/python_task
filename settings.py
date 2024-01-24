import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    ALGORITHM = os.getenv('ALGORITHM')
    APP_NAME = os.getenv('APP_NAME')
    APP_VERSION = os.getenv('APP_VERSION')
    APP_DESCRIPTION = os.getenv('APP_DESCRIPTION')
    DEBUG = os.getenv('DEBUG')
    #UPLOADED_PHOTOS_DEST ='app/static/photos'
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    # simple mde  configurations
    #SIMPLEMDE_JS_IIFE = True
    #SIMPLEMDE_USE_CDN = True        

    