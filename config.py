import os
from environs import Env

BASEDIR = os.path.abspath(os.path.dirname(__file__))

env = Env()
env.read_env(os.path.join(BASEDIR, ".env"))  # read .env file, if it exists

DB_USERNAME = env.str("DB_USERNAME")
DB_PASSWORD = env.str("DB_PASSWORD")
DB_HOST = env.str("DB_HOST")
DB_PORT = env.int("DB_PORT")
DB_NAME = env.str("DB_NAME")

SECRET_KEY = env.str("SECRET_KEY")

DATABASE_URL = f"mysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = SECRET_KEY
    SQLALCHEMY_DATABASE_URI = DATABASE_URL


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig
}