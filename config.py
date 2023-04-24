class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
 
class ProdConfig(Config): 
    pass 
 
class DevConfig(Config): 
    DEBUG = True