"""Module for managing exceptions.

References
----------
flask-restx: https://flask-restx.readthedocs.io/en/latest/errors.html

"""
import logging
import traceback

from flask import current_app
from flask import Flask
from flask import jsonify
from marshmallow import ValidationError
from werkzeug.exceptions import InternalServerError
from werkzeug.exceptions import UnprocessableEntity

from app.extensions import db

logger = logging.getLogger(__name__)


class DoesNotExist(UnprocessableEntity):
    pass


def init_app(app: Flask) -> None:
    app.errorhandler(ValidationError)(_handle_validation_error_exception)
    app.errorhandler(Exception)(_handle_general_error_exception)


def _handle_validation_error_exception(ex: ValidationError) -> tuple:
    """Handler ValidationError exception.

    The errors catched by `app.errorhandler` are not passed
    to teardown_appcontext. So db.session.rollback is required to reverts
    the session objects added to the session.

    """
    db.session.rollback()

    if current_app.config['TESTING'] is False:
        logger.exception(traceback.format_exc())

    return jsonify({'message': ex.normalized_messages()}), 422


def _handle_general_error_exception(ex: Exception) -> tuple:  # noqa
    """Handler InternalServerError exception.

    The errors catched by `app.errorhandler` are not passed
    to teardown_appcontext. So db.session.rollback is required to reverts
    the session objects added to the session.

    """
    db.session.rollback()

    if current_app.config['TESTING'] is False:
        logger.exception(traceback.format_exc())

    return jsonify({'message': InternalServerError.description}), 500
