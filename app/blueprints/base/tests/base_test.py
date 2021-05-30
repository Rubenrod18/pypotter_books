import os
import unittest

from flask import Flask

from .custom_flask_client import CustomFlaskClient


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.app = self.__create_app()
        self.client = self.__create_test_client(self.app)
        self.base_path = '/api'

    @staticmethod
    def __create_app():
        """Create an app with testing environment."""
        from app import create_app

        return create_app('config.TestConfig')

    @staticmethod
    def __create_test_client(app: Flask):
        """Create a test client for making http requests."""
        app.test_client_class = CustomFlaskClient
        return app.test_client()

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
