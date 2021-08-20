"""Package for building a Flask application.

The app package loads application configuration and registers middleware,
blueprints, database models, etc.

"""

__project__ = 'PyPotter Books'
__author__ = 'Rubén Rodríguez Ramírez'
__version__ = '0.3.0'
__description__ = (
    'PyPotter Books is a small shopping books API where you can buy any '
    'Harry Potter book, from chapter one to chapter five.'
)

import logging
import os

import flask
from flask import Flask, send_from_directory
from werkzeug.utils import import_string

from app import exceptions
from app import extensions
from app.blueprints import BLUEPRINTS
from app.cli import cli


def _init_logging(app: Flask) -> None:
    log_basename = os.path.basename(app.config.get('ROOT_DIRECTORY'))
    log_dirname = '{}/app'.format(app.config.get('LOG_DIRECTORY'))
    log_filename = f'{log_dirname}/{log_basename}.log'

    log_directories = [app.config.get('LOG_DIRECTORY'), log_dirname]

    for log_dir in log_directories:
        if not os.path.exists(log_dir):
            os.mkdir(log_dir)

    logging.basicConfig(
        **{
            'format': '%(asctime)s - %(levelname)s - %(name)s - %(message)s',
            'level': logging.DEBUG,
            'filename': log_filename,
        }
    )


def _register_blueprints(app: Flask) -> None:
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)


def _register_static_routes(app: Flask) -> None:
    @app.route('/static/<path:path>')
    def static_files(path: str):
        return send_from_directory(app.config['STATIC_FOLDER'], path)


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
    config = import_string(env_config)

    app = flask.Flask(
        __name__,
        static_url_path=config.STATIC_FOLDER,
        template_folder=config.TEMPLATES_FOLDER,
    )
    app.config.from_object(env_config)

    _init_logging(app)
    cli.init_app(app)
    extensions.init_app(app)
    _register_blueprints(app)
    _register_static_routes(app)
    exceptions.init_app(app)

    return app
