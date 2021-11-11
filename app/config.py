import os
class Config:
    """
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True


class ProdConfig(Config):
    """
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL","")
    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI =SQLALCHEMY_DATABASE_URI.replace("postgres://","postgresql://",1)

class DevConfig(Config):
    """
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://synthia:123@localhost/pitches'
    DEBUG = True
    
config_options = {
    "development": DevConfig,
    "production": ProdConfig
}