from flask import Blueprint

from app.extensions import api as root_api

_API_DESCRIPTION = ('Users with role admin or team_leader can manage '
                    'these endpoints.')
blueprint = Blueprint('users', __name__)
api = root_api.namespace('users', description=_API_DESCRIPTION)
