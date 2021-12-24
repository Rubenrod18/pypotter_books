import factory

from ..factories import CountryFactory
from ._base_integration_test import _CountryBaseIntegrationTest
from app.helpers import DictHelper


class TestSaveCountry(_CountryBaseIntegrationTest):
    def test_is_country_created_country_does_not_exist_returns_country(
        self,
    ):
        exclude = ['currency']
        data = DictHelper.ignore_keys(
            factory.build(dict, FACTORY_CLASS=CountryFactory), exclude
        )

        admin_user = self.get_active_admin_user()
        auth_header = self.build_auth_header(admin_user.email)

        response = self.client.post(
            self.base_path, json=data, headers=auth_header
        )
        json_response = response.get_json()
        json_data = json_response.get('data')

        self.assertEqual(201, response.status_code)
        self.assertEqual(data['currency_id'], json_data['currency'].get('id'))
        self.assertEqual(data['name'], json_data.get('name'))
        self.assertEqual(data['alpha_2_code'], json_data.get('alpha_2_code'))
        self.assertEqual(data['alpha_3_code'], json_data.get('alpha_3_code'))
        self.assertTrue(json_data.get('created_at'))
        self.assertEqual(
            json_data.get('updated_at'), json_data.get('created_at')
        )
        self.assertIsNone(json_data.get('deleted_at'))
