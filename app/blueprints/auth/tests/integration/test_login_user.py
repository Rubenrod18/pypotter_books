import os

from ._base_integration_test import _AuthBaseIntegrationTest


class TestLoginUser(_AuthBaseIntegrationTest):

    def setUp(self, *args, **kwargs):
        super(TestLoginUser, self).setUp()
        self.base_path = f'{self.base_path}/login'

    def test_is_login_ok_valid_credentials_returns_token(self):
        with self.app.app_context():
            user = self.get_rand_user()
            payload = {
                'email': user.email,
                'password': os.getenv('TEST_USER_PASSWORD')
            }
            response = self.client.post(f'{self.base_path}', json=payload)
            json_response = response.get_json()

            self.assertEqual(200, response.status_code)
            self.assertTrue(json_response.get('token'))
