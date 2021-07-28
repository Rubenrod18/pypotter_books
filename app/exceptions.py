"""Module for managing exceptions.

References
----------
flask-restx: https://flask-restx.readthedocs.io/en/latest/errors.html

"""
import logging
import traceback

from flask import current_app
from flask import Flask
from marshmallow import ValidationError

logger = logging.getLogger(__name__)


def init_app(app: Flask) -> None:
    app.errorhandler(ValidationError)(_handle_validation_error_exception)


def _handle_validation_error_exception(ex: ValidationError) -> tuple:
    if current_app.debug:
        logger.debug(traceback.format_exc())
    return {'message': ex.messages}, 422
