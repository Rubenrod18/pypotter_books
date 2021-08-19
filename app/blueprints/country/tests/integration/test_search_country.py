from ._base_integration_test import _CountryBaseIntegrationTest


class TestSearchCountries(_CountryBaseIntegrationTest):
    def __request(self, payload):
        admin_user = self.get_rand_admin_user()
        auth_header = self.build_auth_header(admin_user.email)
        response = self.client.post(
            f'{self.base_path}/search', json=payload, headers=auth_header
        )
        json_response = response.get_json()
        self.assertEqual(200, response.status_code)

        return json_response.get('data')[0]

    def test_search_country_exist_country_name_returns_country(self):
        payload = {
            'search': [
                {
                    'field_name': 'name',
                    'field_value': self.country.name,
                },
            ],
        }

        json_data = self.__request(payload)
        self.assertEqual(self.country.name, json_data.get('name'))

    def test_search_country_exist_country_alpha_2_code_returns_country(self):
        payload = {
            'search': [
                {
                    'field_name': 'alpha_2_code',
                    'field_value': self.country.alpha_2_code,
                },
            ],
        }

        json_data = self.__request(payload)
        self.assertEqual(
            self.country.alpha_2_code, json_data.get('alpha_2_code')
        )

    def test_search_country_exist_country_alpha_3_code_returns_country(self):
        payload = {
            'search': [
                {
                    'field_name': 'alpha_3_code',
                    'field_value': self.country.alpha_3_code,
                },
            ],
        }

        json_data = self.__request(payload)
        self.assertEqual(
            self.country.alpha_3_code, json_data.get('alpha_3_code')
        )
