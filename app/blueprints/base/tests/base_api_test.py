import os

from sqlalchemy import func

from app.blueprints.base import BaseTest
from app.blueprints.role import Role
from app.blueprints.user import User
from app.blueprints.user import UserRoles
from app.extensions import db


class BaseApiTest(BaseTest):
    def setUp(self):
        super(BaseApiTest, self).setUp()
        self.base_path = '/api'

    @staticmethod
    def get_rand_admin_user():
        return (
            db.session.query(User)
            .join(UserRoles)
            .join(Role)
            .filter(
                User.deleted_at.is_(None),
                User.active == 1,
                Role.name == 'admin',
            )
            .first()
        )

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
