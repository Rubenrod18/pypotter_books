from flask import Blueprint
from flask import jsonify
from flask import request
from flask_restx import Resource

from app.extensions import api as root_api

blueprint = Blueprint('base', __name__)
_api = root_api.namespace('', description='Base endpoints')


class BaseResource(Resource):
    @staticmethod
    def _request_payload():
        return request.get_json() or {}


@blueprint.route('/swagger.json')
def swagger_spec():
    schema = root_api.__schema__
    return jsonify(schema)


@_api.route('/welcome')
class WelcomeResource(BaseResource):
    @_api.doc(
        responses={
            200: 'Welcome to PyPotter Books!',
        },
    )
    def get(self) -> tuple:
        return 'Welcome to PyPotter Books API!', 200
