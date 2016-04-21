import os

class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = '\xd2\x16\xd6<\xc6.J\x8b]\xda\x9d\x82'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False
