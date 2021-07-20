"""Package for building a Flask application.

The app package loads application configuration and registers middleware,
blueprints, database models, etc.

"""

__project__ = 'PyPotter Books'
__author__ = 'Rubén Rodríguez Ramírez'
__version__ = '0.2.0'
__description__ = (
    'PyPotter Books is a small shopping books API where you can buy any '
    'Harry Potter book, from chapter one to chapter five.'
)

import logging
import os

import flask
from flask import Flask

from app import exceptions
from app import extensions
from app.blueprints import BLUEPRINTS
from app.cli import cli


def _register_blueprints(app: Flask) -> None:
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)


def _init_logging(app: Flask) -> None:
    log_basename = os.path.basename(app.config.get('ROOT_DIRECTORY'))
    log_dirname = '{}/app'.format(app.config.get('LOG_DIRECTORY'))
    log_filename = f'{log_dirname}/{log_basename}.log'

    if not os.path.exists(log_dirname):
        os.mkdir(log_dirname)

    config = {
        'format': '%(asctime)s - %(levelname)s - %(name)s - %(message)s',
        'level': logging.DEBUG,
        'filename': log_filename,
    }

    logging.basicConfig(**config)


def create_app(env_config: str) -> Flask:
    """Builds an application based on environment configuration.

    Parameters
    ----------
    env_config
        Environment configuration. Posible values::

            config.ProdConfig
            config.DevConfig
            config.TestConfig

    Returns
    -------
    Flask
        A `flask.flask` instance.

    """
    app = flask.Flask(__name__)
    app.config.from_object(env_config)

    _init_logging(app)
    cli.init_app(app)
    extensions.init_app(app)
    _register_blueprints(app)
    exceptions.init_app(app)

    return app
