from ._base_integration_test import _CurrencyBaseIntegrationTest


class TestGetCurrency(_CurrencyBaseIntegrationTest):
    def test_is_currency_obtained_currency_exists_returns_currency(self):
        with self.app.app_context():
            currency = self.get_rand_currency()

            admin_user = self.get_rand_admin_user()
            auth_header = self.build_auth_header(admin_user.email)
            response = self.client.get(
                f'{self.base_path}/{currency.id}', json={}, headers=auth_header
            )
            json_response = response.get_json()
            json_data = json_response.get('data')

            self.assertEqual(200, response.status_code)
            self.assertEqual(currency.id, json_data.get('id'))
            self.assertEqual(currency.code, json_data.get('code'))
            self.assertEqual(currency.decimals, json_data.get('decimals'))
            self.assertEqual(currency.name, json_data.get('name'))
            self.assertEqual(
                currency.name_plural, json_data.get('name_plural')
            )
            self.assertEqual(currency.num, json_data.get('num'))
            self.assertEqual(currency.symbol, json_data.get('symbol'))
            self.assertEqual(
                currency.symbol_native, json_data.get('symbol_native')
            )
            self.assertEqual(
                currency.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                json_data.get('created_at'),
            )
            self.assertEqual(
                currency.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
                json_data.get('updated_at'),
            )
            self.assertEqual(currency.deleted_at, json_data.get('deleted_at'))
