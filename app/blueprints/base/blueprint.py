import logging

from flask import Blueprint
from flask import jsonify
from flask import request
from flask_restx import Resource

from app.extensions import api as root_api

blueprint = Blueprint('base', __name__)
logger = logging.getLogger(__name__)
api = root_api.namespace('', description='Base endpoints')


class BaseResource(Resource):
    @staticmethod
    def request_payload():
        return request.get_json() or {}


@blueprint.route('/swagger.json')
def swagger_spec():
    schema = root_api.__schema__
    return jsonify(schema)


@api.route('/welcome')
class WelcomeResource(BaseResource):
    @api.doc(
        responses={
            200: 'Welcome to flask_api!',
        },
    )
    def get(self) -> tuple:
        return 'Welcome to flask_api!', 200
