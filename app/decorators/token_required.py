import functools
import re

from flask import current_app
from flask import request
from werkzeug.exceptions import Forbidden
from werkzeug.exceptions import Unauthorized

from app.wrappers import SecurityWrapper


def token_required(fnc):
    @functools.wraps(fnc)
    def decorator(*args, **kwargs):
        if (
            current_app.config.get('DEVELOPMENT') is True
            and current_app.config.get('TESTING') is False
        ):
            return fnc(*args, **kwargs)

        key = current_app.config.get('SECURITY_TOKEN_AUTHENTICATION_HEADER')
        token = request.headers.get(key, '')
        match_data = re.match(r'^Bearer\s(\S+)$', token)

        if not token or not match_data:
            raise Unauthorized('User is not authorized')

        expired, invalid, user = SecurityWrapper.login_token_status(
            match_data[1]
        )

        if not expired and not invalid and user:
            if user.active:
                return fnc(*args, **kwargs)
            else:
                raise Forbidden('User is not active')
        elif expired:
            raise Unauthorized('Token has expired')
        else:
            raise Unauthorized('Token is invalid')

    return decorator
