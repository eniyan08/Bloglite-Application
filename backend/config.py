import os

current_dir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+  os.path.join(current_dir, "database3.db")
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'super-secret'
    SECURITY_PASSWORD_SALT = "salt"
    WTF_CSRF_ENABLED = False
    SECURITY_TOKEN_AUTHENTICATION_HEADER = "Authentication-Token" 
    SECURITY_PASSWORD_HASH = "bcrypt"
    REDIS_URL = "redis://localhost"
    CACHE_TYPE = "RedisCache"
    CACHE_REDIS_HOST = "localhost"
    CACHE_REDIS_PORT = 6379

class DevelopmentConfig(Config):
    DEBUG = True



