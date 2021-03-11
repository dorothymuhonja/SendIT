import os


class Config:
    SECRET_KEY = "infinity"
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Moringa@localhost/sendit'


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}    
