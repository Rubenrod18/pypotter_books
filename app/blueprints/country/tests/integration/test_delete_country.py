from ._base_integration_test import _CountryBaseIntegrationTest


class TestDeleteCountry(_CountryBaseIntegrationTest):
    def test_is_country_deleted_country_exists_returns_country_deleted(
        self,
    ):
        admin_user = self.get_rand_admin_user()
        auth_header = self.build_auth_header(admin_user.email)
        response = self.client.delete(
            f'{self.base_path}/{self.country.id}', json={}, headers=auth_header
        )
        json_response = response.get_json()
        json_data = json_response.get('data')

        self.assertEqual(200, response.status_code)
        self.assertEqual(self.country.id, json_data.get('id'))
        self.assertIsNotNone(json_data.get('deleted_at'))
        self.assertEqual(
            json_data.get('deleted_at'), json_data.get('updated_at')
        )
