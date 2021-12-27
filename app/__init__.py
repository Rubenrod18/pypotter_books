"""Package for building a Flask application.

The app package loads application configuration and registers middleware,
blueprints, database models, etc.

"""

__project__ = 'PyPotter Books'
__author__ = 'Rubén Rodríguez Ramírez'
__version__ = '1.0.0'
__description__ = (
    'PyPotter Books is a small shopping books API where you can buy any '
    'Harry Potter book, from chapter one to chapter five.'
)

import logging
import os
import pprint
import typing as t

import flask
from flask import Flask, send_from_directory
from werkzeug.utils import import_string

from app import exceptions
from app import extensions
from app.blueprints import BLUEPRINTS
from app.cli import cli_register

if t.TYPE_CHECKING:
    from config import Config


def _create_logging_file(app: Flask) -> str:
    log_basename = os.path.basename(app.config.get('ROOT_DIRECTORY'))
    log_dirname = '{}/app'.format(app.config.get('LOG_DIRECTORY'))
    log_filename = f'{log_dirname}/{log_basename}.log'

    log_directories = [app.config.get('LOG_DIRECTORY'), log_dirname]

    for log_dir in log_directories:
        if not os.path.exists(log_dir):
            os.mkdir(log_dir)

    return log_filename


def _init_logging(app: Flask) -> None:
    del app.logger.handlers[:]
    loggers = [
        app.logger,
    ]
    handlers = []

    console_handler = logging.FileHandler(filename=_create_logging_file(app))
    console_handler.setLevel(app.config.get('LOGGING_LEVEL'))
    console_handler.setFormatter(
        logging.Formatter(
            '%(asctime)s - %(levelname)s - %(name)s - %(message)s',
            datefmt='%d/%m/%Y %H:%M:%S',
        )
    )
    handlers.append(console_handler)

    for logger in loggers:
        for handler in handlers:
            logger.addHandler(handler)
        logger.propagate = False
        logger.setLevel(app.config.get('LOGGING_LEVEL'))

    app.logger.debug(pprint.pformat(app.config, indent=4))


def _register_blueprints(app: Flask) -> None:
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)


def _register_static_routes(app: Flask) -> None:
    @app.route('/static/<path:path>')
    def static_files(path: str):
        return send_from_directory(app.config['STATIC_FOLDER'], path)


def create_app(env_config: t.Union[str, t.Type['Config']]) -> Flask:
    """Builds an application based on environment configuration.

    Parameters
    ----------
    env_config : str or Config
        Environment configuration. Posible values::

            config.ProdConfig
            config.DevConfig
            config.TestConfig

    Returns
    -------
    Flask
        A `flask.flask` instance.

    """
    config = env_config

    if isinstance(env_config, str):
        config = import_string(env_config)

    app = flask.Flask(
        __name__,
        static_url_path=config.STATIC_FOLDER,
        template_folder=config.TEMPLATES_FOLDER,
    )
    app.config.from_object(env_config)

    _init_logging(app)
    cli_register.init_app(app)
    extensions.init_app(app)
    _register_blueprints(app)
    _register_static_routes(app)
    exceptions.init_app(app)

    return app
