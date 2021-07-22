import functools
import re
import time

from flask import current_app
from flask import request
from flask_security.passwordless import login_token_status
from werkzeug.exceptions import Forbidden
from werkzeug.exceptions import Unauthorized

from app.utils.constants import TOKEN_REGEX


def token_required(fnc):
    @functools.wraps(fnc)
    def decorator(*args, **kwargs):
        key = current_app.config.get('SECURITY_TOKEN_AUTHENTICATION_HEADER')
        token = request.headers.get(key, '')

        match_data = re.match(TOKEN_REGEX, token)

        if not token or not match_data:
            raise Unauthorized('User is not authorized')

        expired, invalid, user = login_token_status(match_data[1])

        if not expired and not invalid and user:
            if user.active:
                return fnc(*args, **kwargs)
            else:
                raise Forbidden('User is not active')
        elif expired:
            raise Unauthorized('Token has expired')
        else:
            raise Unauthorized('Unauthorized')

    return decorator


def seed_actions(fnc):
    @functools.wraps(fnc)
    def message(*args, **kwargs):
        seeder = args[0]

        print(' Seeding: %s' % seeder.name)
        exec_time = 0
        try:
            start = time.time()
            res = fnc(*args, **kwargs)
            exec_time = round((time.time() - start), 2)
        finally:
            print(' Seeded:  {} ( {} seconds )'.format(seeder.name, exec_time))
        return res

    return message
