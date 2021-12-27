from ._base_integration_test import _CurrencyBaseIntegrationTest


class TestSearchCurrencies(_CurrencyBaseIntegrationTest):
    def __request(self, payload):
        admin_user = self.get_active_admin_user()
        auth_header = self.build_auth_header(admin_user.email)
        response = self.client.post(
            f'{self.base_path}/search', json=payload, headers=auth_header
        )
        json_response = response.get_json()
        self.assertEqual(200, response.status_code)

        return json_response.get('data')[0]

    def test_search_currency_exist_currency_name_returns_currency(self):
        payload = {
            'search': [
                {
                    'field_name': 'name',
                    'field_value': self.currency.name,
                },
            ],
        }

        json_data = self.__request(payload)
        self.assertEqual(self.currency.name, json_data.get('name'))

    def test_search_currency_exist_currency_code_returns_currency(self):
        payload = {
            'search': [
                {
                    'field_name': 'code',
                    'field_value': self.currency.code,
                },
            ],
        }

        json_data = self.__request(payload)
        self.assertEqual(self.currency.code, json_data.get('code'))

    def test_search_currency_exist_currency_num_returns_currency(self):
        payload = {
            'search': [
                {
                    'field_name': 'num',
                    'field_value': self.currency.num,
                },
            ],
        }

        json_data = self.__request(payload)
        self.assertEqual(self.currency.num, json_data.get('num'))
