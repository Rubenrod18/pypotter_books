import unittest

from flask import Flask

from app.extensions import db
from .custom_flask_client import CustomFlaskClient
from .seeders import init_seed


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.app = self.__create_app()
        self.client = self.__create_test_client(self.app)

        with self.app.app_context():
            self.session = db.session()

            db.create_all()
            init_seed()

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()
            db.session.remove()

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
