from flask import Blueprint
from flask import request
from flask_restx import Resource

from app.extensions import api as root_api

blueprint = Blueprint('base', __name__)
api = root_api.namespace('', description='Base endpoints')


class BaseResource(Resource):
    @staticmethod
    def request_payload():
        return request.get_json() or {}


@api.route('/welcome')
class WelcomeResource(Resource):
    @api.doc(
        responses={
            200: 'Welcome to flask_api!',
        },
    )
    def get(self) -> tuple:
        return 'Welcome to flask_api!', 200
