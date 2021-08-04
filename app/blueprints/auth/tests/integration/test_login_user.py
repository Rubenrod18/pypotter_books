import os

from ._base_integration_test import _AuthBaseIntegrationTest
from app.blueprints.user import UserFactory
from app.blueprints.user.tests.factory import fake
from app.wrappers import SecurityWrapper


class TestLoginUser(_AuthBaseIntegrationTest):
    def setUp(self, *args, **kwargs):
        super(TestLoginUser, self).setUp()
        self.base_path = f'{self.base_path}/login'

    def test_is_login_ok_valid_credentials_returns_token(self):
        with self.app.app_context():
            user = self.get_rand_user()
            payload = {
                'email': user.email,
                'password': os.getenv('TEST_USER_PASSWORD'),
            }
            response = self.client.post(f'{self.base_path}', json=payload)
            json_response = response.get_json()

            self.assertEqual(200, response.status_code)
            self.assertTrue(json_response.get('token'))

    def __payload_format_invalid_process(
        self, payload: dict, expect_response: dict
    ):
        response = self.client.post(f'{self.base_path}', json=payload)
        json_response = response.get_json()

        self.assertEqual(422, response.status_code)
        self.assertDictEqual(expect_response, json_response)

    def test_is_login_ko_payload_format_is_invalid_returns_validation_error(
        self,
    ):
        with self.app.app_context():
            self.__payload_format_invalid_process(
                payload={'email': ''},
                expect_response={
                    'message': {
                        'password': ['Missing data for required field.']
                    }
                },
            )
            self.__payload_format_invalid_process(
                payload={'password': ''},
                expect_response={
                    'message': {
                        'email': ['Missing data for required field.'],
                        'password': ['Length must be between 8 and 50.'],
                    }
                },
            )
            self.__payload_format_invalid_process(
                payload={},
                expect_response={
                    'message': {
                        'email': ['Missing data for required field.'],
                        'password': ['Missing data for required field.'],
                    }
                },
            )

    def __password_invalid_process(self, plain_password: str):
        ensured_password = SecurityWrapper.ensure_password(plain_password)
        user = UserFactory(
            active=True, deleted_at=None, password=ensured_password
        )

        payload = {'email': user.email, 'password': plain_password}
        response = self.client.post(f'{self.base_path}', json=payload)
        json_response = response.get_json()

        self.assertEqual(422, response.status_code)

        expect_json_response = {
            'message': {'password': ['Length must be between 8 and 50.']}
        }
        self.assertDictEqual(expect_json_response, json_response)

    def test_is_login_ko_password_length_is_invalid_returns_validation_error(
        self,
    ):
        with self.app.app_context():
            self.__password_invalid_process('_hello_')  # 7 chars
            self.__password_invalid_process(
                'f8ezuy7wbqxscjzm7fnwh83x7xpuuvbvejkhrj46znfabr49d35'  # noqa : 51 chars
            )

    def __user_invalid_process(
        self, user_data: dict, plain_password: str, expect_response: dict
    ):
        user = UserFactory(**user_data)

        payload = {'email': user.email, 'password': plain_password}
        response = self.client.post(f'{self.base_path}', json=payload)
        json_response = response.get_json()

        self.assertEqual(401, response.status_code)
        self.assertDictEqual(expect_response, json_response)

    def test_is_login_ko_user_is_not_created_returns_unauthorized_error(
        self,
    ):
        with self.app.app_context():
            payload = {
                'email': 'user_not_created@gmail.com',
                'password': '12345678',
            }
            response = self.client.post(f'{self.base_path}', json=payload)
            json_response = response.get_json()

            self.assertEqual(401, response.status_code)

            expect_json_response = {'message': 'User not found'}
            self.assertDictEqual(expect_json_response, json_response)

    def test_is_login_ko_user_is_inactive_returns_unauthorized_error(
        self,
    ):
        with self.app.app_context():
            user_data = {
                'active': False,
                'deleted_at': None,
                'password': '12345678',
            }
            self.__user_invalid_process(
                user_data=user_data,
                plain_password=user_data['password'],
                expect_response={'message': 'User is not activated'},
            )

    def test_is_login_ko_user_is_already_deleted_returns_unauthorized_error(
        self,
    ):
        with self.app.app_context():
            user_data = {
                'active': True,
                'deleted_at': fake.date_time_between(
                    start_date='-1y', end_date='now'
                ),
                'password': '12345678',
            }
            self.__user_invalid_process(
                user_data=user_data,
                plain_password=user_data['password'],
                expect_response={'message': 'User is deleted'},
            )

    def test_is_login_ko_user_password_not_matchs_returns_unauthorized_error(
        self,
    ):
        with self.app.app_context():
            user_data = {
                'active': True,
                'deleted_at': None,
                'password': '12345678',
            }
            self.__user_invalid_process(
                user_data=user_data,
                plain_password='no_match_password',
                expect_response={'message': 'Credentials invalid'},
            )
