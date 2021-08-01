import unittest

from flask import Flask

from .custom_flask_client import CustomFlaskClient


class _BaseTest(unittest.TestCase):
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
