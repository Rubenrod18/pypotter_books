from ._base_integration_test import _RoleBaseIntegrationTest


class TestSearchRoles(_RoleBaseIntegrationTest):
    def __request(self, payload):
        admin_user = self.get_rand_admin_user()
        auth_header = self.build_auth_header(admin_user.email)
        response = self.client.post(
            f'{self.base_path}/search', json=payload, headers=auth_header
        )
        json_response = response.get_json()
        self.assertEqual(200, response.status_code)

        return json_response.get('data')[0]

    def test_search_role_exist_role_name_returns_role(self):
        payload = {
            'search': [
                {
                    'field_name': 'name',
                    'field_value': self.role.name,
                },
            ],
        }

        json_data = self.__request(payload)
        self.assertEqual(self.role.name, json_data.get('name'))

    def test_search_role_exist_role_description_returns_role(self):
        payload = {
            'search': [
                {
                    'field_name': 'description',
                    'field_value': self.role.description,
                },
            ],
        }

        json_data = self.__request(payload)
        self.assertEqual(self.role.description, json_data.get('description'))

    def test_search_role_exist_role_label_returns_role(self):
        payload = {
            'search': [
                {
                    'field_name': 'label',
                    'field_value': self.role.label,
                },
            ],
        }

        json_data = self.__request(payload)
        self.assertEqual(self.role.label, json_data.get('label'))
