from ._base_integration_test import _CountryBaseIntegrationTest


class TestGetcountry(_CountryBaseIntegrationTest):
    def test_is_country_obtained_country_exists_returns_country(self):
        with self.app.app_context():
            country = self.get_rand_country()

            admin_user = self.get_rand_admin_user()
            auth_header = self.build_auth_header(admin_user.email)
            response = self.client.get(
                f'{self.base_path}/{country.id}', json={}, headers=auth_header
            )
            json_response = response.get_json()
            json_data = json_response.get('data')

            self.assertEqual(200, response.status_code)
            self.assertEqual(country.id, json_data.get('id'))
            self.assertEqual(
                country.currency_id, json_data['currency'].get('id')
            )
            self.assertEqual(country.name, json_data.get('name'))
            self.assertEqual(
                country.alpha_2_code, json_data.get('alpha_2_code')
            )
            self.assertEqual(
                country.alpha_3_code, json_data.get('alpha_3_code')
            )
            self.assertEqual(
                country.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                json_data.get('created_at'),
            )
            self.assertEqual(
                country.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
                json_data.get('updated_at'),
            )
            self.assertEqual(country.deleted_at, json_data.get('deleted_at'))
