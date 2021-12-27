from ._base_integration_test import _AuthBaseIntegrationTest
from app.blueprints.user import UserFactory


class TestLogoutUser(_AuthBaseIntegrationTest):
    def test_is_logout_ok_user_is_logged_user_is_not_logged(self):
        user = UserFactory(active=True, deleted_at=None)
        auth_header = self.build_auth_header(user.email)

        response = self.client.post(
            f'{self.base_path}/logout', json={}, headers=auth_header
        )
        self.assertEqual(204, response.status_code)

    def test_is_logout_ko_user_is_not_logged_unauthorized_response(self):
        response = self.client.post(f'{self.base_path}/logout', json={})

        self.assertEqual(401, response.status_code)
        self.assertDictEqual(
            {'message': 'User is not authorized'}, response.get_json()
        )
