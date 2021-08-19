import factory

from ..factory import CountryFactory
from ._base_integration_test import _CountryBaseIntegrationTest
from app.helpers import DictHelper


class TestUpdateCountry(_CountryBaseIntegrationTest):
    def test_is_country_updated_country_exist_previously_returns_country(
        self,
    ):
        exclude = ['currency']
        data = DictHelper.ignore_keys(
            factory.build(dict, FACTORY_CLASS=CountryFactory), exclude
        )

        admin_user = self.get_rand_admin_user()
        auth_header = self.build_auth_header(admin_user.email)
        response = self.client.put(
            f'{self.base_path}/{self.country.id}',
            json=data,
            headers=auth_header,
        )
        json_response = response.get_json()
        json_data = json_response.get('data')

        self.assertEqual(200, response.status_code)
        self.assertEqual(self.country.id, json_data.get('id'))
        self.assertEqual(data['currency_id'], json_data['currency'].get('id'))
        self.assertEqual(data['name'], json_data.get('name'))
        self.assertEqual(data['alpha_2_code'], json_data.get('alpha_2_code'))
        self.assertEqual(data['alpha_3_code'], json_data.get('alpha_3_code'))
        self.assertTrue(json_data.get('created_at'))
        self.assertGreaterEqual(
            json_data.get('updated_at'), json_data.get('created_at')
        )
        self.assertIsNone(json_data.get('deleted_at'))
