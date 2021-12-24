import factory

from ..factories import CurrencyFactory
from ._base_integration_test import _CurrencyBaseIntegrationTest


class TestSaveCurrency(_CurrencyBaseIntegrationTest):
    def test_is_currency_created_currency_does_not_exist_returns_currency(
        self,
    ):
        data = factory.build(dict, FACTORY_CLASS=CurrencyFactory)

        admin_user = self.get_active_admin_user()
        auth_header = self.build_auth_header(admin_user.email)
        response = self.client.post(
            self.base_path, json=data, headers=auth_header
        )
        json_response = response.get_json()
        json_data = json_response.get('data')

        self.assertEqual(201, response.status_code)
        self.assertEqual(data['code'], json_data.get('code'))
        self.assertEqual(data['decimals'], json_data.get('decimals'))
        self.assertEqual(data['name'], json_data.get('name'))
        self.assertEqual(data['name_plural'], json_data.get('name_plural'))
        self.assertEqual(data['num'], json_data.get('num'))
        self.assertEqual(data['symbol'], json_data.get('symbol'))
        self.assertEqual(data['symbol_native'], json_data.get('symbol_native'))
        self.assertTrue(json_data.get('created_at'))
        self.assertEqual(
            json_data.get('updated_at'), json_data.get('created_at')
        )
        self.assertIsNone(json_data.get('deleted_at'))
