import os

from sqlalchemy import func

from app.blueprints.base import BaseTest
from app.blueprints.user.tests.factories import AdminUserFactory
from app.extensions import db


class BaseApiTest(BaseTest):
    def setUp(self):
        super(BaseApiTest, self).setUp()
        self.base_path = '/api'

    @staticmethod
    def get_active_admin_user():
        return AdminUserFactory(active=True, deleted_at=None)

    @staticmethod
    def find_random_record(model: db.Model, *args, **kwargs):
        return (
            model.query.filter(*args)
            .filter_by(**kwargs)
            .order_by(func.random())
            .first()
        )

    def build_auth_header(self, user_email: str = None):
        """Create an auth header from a given user that can be added to
        an http requests."""
        if user_email is None:
            user_email = os.getenv('TEST_USER_EMAIL')

        data = {
            'email': user_email,
            'password': os.getenv('TEST_USER_PASSWORD'),
        }

        response = self.client.post('/api/auth/login', json=data)
        json_response = response.get_json()

        assert 200 == response.status_code
        token = json_response.get('token')

        return {
            self.app.config['SECURITY_TOKEN_AUTHENTICATION_HEADER']: token,
        }
