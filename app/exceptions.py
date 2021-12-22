"""Module for managing exceptions.

References
----------
flask-restx: https://flask-restx.readthedocs.io/en/latest/errors.html

"""
import logging
import traceback
import typing

from flask import current_app
from flask import Flask
from flask import jsonify
from marshmallow import ValidationError
from werkzeug.exceptions import HTTPException

from app.extensions import db

if typing.TYPE_CHECKING:
    from werkzeug.sansio.response import Response

logger = logging.getLogger(__name__)


class DoesNotExist(HTTPException):
    code = 422
    description = 'The record doesn\'t exist'

    def __init__(
        self,
        description: typing.Optional[str] = None,
        response: typing.Optional['Response'] = None,
    ) -> None:
        if description is not None:
            self.description = description
        self.response = response
        super(DoesNotExist, self).__init__(description, response)


def init_app(app: Flask) -> None:
    app.errorhandler(ValidationError)(_handle_validation_error_exception)


def _handle_validation_error_exception(ex: ValidationError) -> tuple:
    """Handler ValidationError exception.

    The errors catched by `app.errorhandler` are not passed
    to teardown_appcontext. So db.session.rollback is required to reverts
    the session objects added to the session.

    """
    db.session.rollback()

    if current_app.debug and not current_app.config['TESTING']:
        logger.exception(traceback.format_exc())

    return jsonify({'message': ex.normalized_messages()}), 422
