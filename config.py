import os


class Config:
    SECRET_KEY = "infinity"


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}    
