from ._base_integration_test import _AuthBaseIntegrationTest


class TestLogoutUser(_AuthBaseIntegrationTest):

    def test_is_logout_ok_user_is_logged_user_is_not_logged(self):
        with self.app.app_context():
            user = self.get_rand_user()
            auth_header = self.build_auth_header(user.email)

            response = self.client.post(f'{self.base_path}/logout',
                                        json={},
                                        headers=auth_header)
            self.assertEqual(204, response.status_code)
