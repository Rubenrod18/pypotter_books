from ._base_integration_test import _AuthBaseIntegrationTest
from app.blueprints.user import User


class TestLogoutUser(_AuthBaseIntegrationTest):
    def test_is_logout_ok_user_is_logged_user_is_not_logged(self):
        with self.app.app_context():
            user = self.find_random_record(
                User, **{'deleted_at': None, 'active': True}
            )
            auth_header = self.build_auth_header(user.email)

            response = self.client.post(
                f'{self.base_path}/logout', json={}, headers=auth_header
            )
            self.assertEqual(204, response.status_code)

    def test_is_logout_ko_user_is_not_logged_unauthorized_response(self):
        with self.app.app_context():
            response = self.client.post(f'{self.base_path}/logout', json={})

            self.assertEqual(401, response.status_code)
            self.assertDictEqual(
                {'message': 'User is not authorized'}, response.get_json()
            )
