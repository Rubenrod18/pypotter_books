"""Module loads the application's configuration.

The extension and custom configurations are defined here.

"""
import os

from dotenv import load_dotenv

load_dotenv()


def _build_test_sqlalchemy_database_uri(config: 'Config') -> str:
    database_uri_lst = config.SQLALCHEMY_DATABASE_URI.split('/')
    database_uri_lst[1] = '//'
    tmp = ''.join(database_uri_lst[0:-1])

    dbname = _build_database_name(config)
    test_db_uri = f'{tmp}/{dbname}'
    return test_db_uri


def _build_database_name(config: 'Config') -> str:
    dbname = config.SQLALCHEMY_DATABASE_URI.split('/')[-1:][0]
    return f'test_{dbname}'


class Config:
    """Default configuration options."""

    # Flask
    DEVELOPMENT = False
    DEBUG = False
    TESTING = False
    SERVER_NAME = os.getenv('SERVER_NAME')
    LOGIN_DISABLED = False

    # Flask-Security-Too
    SECRET_KEY = os.getenv('SECRET_KEY')
    SECURITY_PASSWORD_SALT = os.getenv('SECURITY_PASSWORD_SALT')
    SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
    SECURITY_TOKEN_AUTHENTICATION_HEADER = 'Authorization'
    SECURITY_TOKEN_MAX_AGE = None
    SECURITY_PASSWORD_LENGTH_MIN = 8

    # Flask-Mail
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = os.getenv('MAIL_PORT')
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', True)
    MAIL_USE_SSL = os.getenv('MAIL_USE_SSL', False)

    # Flask Swagger UI
    SWAGGER_URL = os.getenv('SWAGGER_URL', '/docs')
    SWAGGER_API_URL = os.getenv(
        'SWAGGER_API_URL', f'http://{SERVER_NAME}/static/swagger.yaml'
    )

    # Flask Restful
    RESTX_ERROR_404_HELP = False
    FLASK_RESTFUL_PREFIX = '/api'
    RESTX_MASK_SWAGGER = False

    # Flask SQLAlchemy
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Mr Developer
    ROOT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
    LOG_DIRECTORY = '%s/log' % ROOT_DIRECTORY


class ProdConfig(Config):
    """Production configuration options."""

    pass


class DevConfig(Config):
    """Development configuration options."""

    # Flask
    DEVELOPMENT = True
    DEBUG = True


class TestConfig(Config):
    """Testing configuration options."""

    # Flask
    DEVELOPMENT = True
    DEBUG = True
    TESTING = True

    # Flask SQLAlchemy
    SQLALCHEMY_DATABASE_URI = _build_test_sqlalchemy_database_uri(Config)
