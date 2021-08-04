from sqlalchemy import func
from werkzeug.exceptions import Forbidden
from werkzeug.exceptions import Unauthorized

from app.blueprints.base import BaseTest
from app.blueprints.user import User
from app.decorators import token_required
from app.wrappers import SecurityWrapper


class TestTokenRequired(BaseTest):
    def setUp(self):
        super(TestTokenRequired, self).setUp()
        with self.app.app_context():
            self.token_auth_header = self.app.config.get(
                'SECURITY_TOKEN_AUTHENTICATION_HEADER'
            )

    @staticmethod
    def __get_rand_user(**kwargs):
        return User.query.filter_by(**kwargs).order_by(func.random()).first()

    def test_is_token_valid_auth_header_does_not_exist_returns_user_is_not_authorized(  # noqa
        self,
    ):
        with self.app.test_request_context():

            @token_required
            def decorated():
                return True  # pragma: no cover

            try:
                decorated()
            except Unauthorized as e:
                response_exception = e

            self.assertEqual(response_exception.code, 401)
            self.assertEqual(
                response_exception.description, 'User is not authorized'
            )

    def test_is_token_valid_bearer_token_is_empty_returns_user_is_not_authorized(  # noqa
        self,
    ):
        with self.app.test_request_context(
            headers={self.token_auth_header: ''}
        ):

            @token_required
            def decorated():
                return True  # pragma: no cover

            try:
                decorated()
            except Unauthorized as e:
                response_exception = e

            self.assertEqual(response_exception.code, 401)
            self.assertEqual(
                response_exception.description, 'User is not authorized'
            )

    def test_is_token_valid_add_invalid_bearer_token_returns_token_is_invalid(
        self,
    ):
        with self.app.test_request_context(
            headers={self.token_auth_header: 'Bearer 123456789'}
        ):

            @token_required
            def decorated():
                return True  # pragma: no cover

            try:
                decorated()
            except Unauthorized as e:
                response_exception = e

            self.assertEqual(response_exception.code, 401)
            self.assertEqual(
                response_exception.description, 'Token is invalid'
            )

    def test_is_token_valid_add_expired_bearer_token_returns_token_has_expired(
        self,
    ):
        expired_token = 'Bearer WyIxIl0.YQQq9w.ohL2ObAcY04iUGifhbXyU6EUaBU'

        with self.app.test_request_context(
            headers={self.token_auth_header: expired_token}
        ):

            @token_required
            def decorated():
                return True  # pragma: no cover

            try:
                decorated()
            except Unauthorized as e:
                response_exception = e

            self.assertEqual(response_exception.code, 401)
            self.assertEqual(
                response_exception.description, 'Token has expired'
            )

    def test_is_token_valid_user_is_inactive_returns_forbidden_user_inactive(
        self,
    ):
        with self.app.app_context():
            user = self.__get_rand_user(
                **{'active': False, 'deleted_at': None}
            )
            created_token = SecurityWrapper.create_token(user)

        with self.app.test_request_context(
            headers={self.token_auth_header: f'Bearer {created_token}'}
        ):

            @token_required
            def decorated():
                return True  # pragma: no cover

            try:
                decorated()
            except Forbidden as e:
                response_exception = e

            self.assertEqual(response_exception.code, 403)
            self.assertEqual(
                response_exception.description, 'User is not active'
            )

    def test_is_token_valid_user_is_active_returns_ok(
        self,
    ):
        with self.app.app_context():
            user = self.__get_rand_user(**{'active': True, 'deleted_at': None})
            created_token = SecurityWrapper.create_token(user)

        with self.app.test_request_context(
            headers={self.token_auth_header: f'Bearer {created_token}'}
        ):

            @token_required
            def decorated():
                return True

            self.assertEqual(True, decorated())
