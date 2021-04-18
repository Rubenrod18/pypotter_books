from ._base_integration_test import _UserBaseIntegrationTest


class TestGetUser(_UserBaseIntegrationTest):
    def test_get_user_is_sending_valid_request_is_obtained(self):
        with self.app.app_context():
            user = self.get_rand_user()
            role = user.roles[0]

            admin_user = self.get_rand_admin_user()
            auth_header = self.build_auth_header(admin_user.email)
            response = self.client.get(
                f'{self.base_path}/{user.id}', json={}, headers=auth_header
            )
            json_response = response.get_json()
            json_data = json_response.get('data')

            self.assertEqual(200, response.status_code)
            self.assertEqual(user.name, json_data.get('name'))
            self.assertEqual(user.last_name, json_data.get('last_name'))
            self.assertEqual(
                user.birth_date.strftime('%Y-%m-%d'),
                json_data.get('birth_date'),
            )
            self.assertEqual(user.genre.value, json_data.get('genre'))
            self.assertEqual(
                user.created_at.strftime('%Y-%m-%dT%H:%M:%S'),
                json_data.get('created_at'),
            )
            self.assertGreater(
                json_data.get('updated_at'), json_data.get('created_at')
            )
            self.assertIsNone(json_data.get('deleted_at'))

            role_data = json_data.get('roles')[0]

            self.assertEqual(role.name, role_data.get('name'))
            self.assertEqual(role.label, role_data.get('label'))
