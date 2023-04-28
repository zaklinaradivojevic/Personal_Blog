class Config(object):
    POSTS_PER_PAGE = 10


class ProdConfig(Config):
    SECRET_KEY = 'abc'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'


class DevConfig(Config):
    DEBUG = True
    SECRET_KEY = 'abc'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'