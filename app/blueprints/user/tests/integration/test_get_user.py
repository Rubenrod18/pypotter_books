from ._base_integration_test import _UserBaseIntegrationTest


class TestGetUser(_UserBaseIntegrationTest):
    def test_get_user_is_sending_valid_request_is_obtained(self):
        role = self.user.roles[0]

        admin_user = self.get_active_admin_user()
        auth_header = self.build_auth_header(admin_user.email)
        response = self.client.get(
            f'{self.base_path}/{self.user.id}', json={}, headers=auth_header
        )
        json_response = response.get_json()
        json_data = json_response.get('data')

        self.assertEqual(200, response.status_code)
        self.assertEqual(self.user.name, json_data.get('name'))
        self.assertEqual(self.user.last_name, json_data.get('last_name'))
        self.assertEqual(
            self.user.birth_date.strftime('%Y-%m-%d'),
            json_data.get('birth_date'),
        )
        self.assertEqual(self.user.genre.value, json_data.get('genre'))
        self.assertEqual(
            self.user.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            json_data.get('created_at'),
        )
        self.assertGreaterEqual(
            json_data.get('updated_at'), json_data.get('created_at')
        )
        self.assertIsNone(json_data.get('deleted_at'))

        role_data = json_data.get('roles')[0]

        self.assertEqual(role.name, role_data.get('name'))
        self.assertEqual(role.label, role_data.get('label'))
