from ._base_integration_test import _ShoppingCartBaseIntegrationTest


class TestSearchCurrencies(_ShoppingCartBaseIntegrationTest):
    def __request(self, payload):
        admin_user = self.get_rand_admin_user()
        auth_header = self.build_auth_header(admin_user.email)
        response = self.client.post(
            f'{self.base_path}/search', json=payload, headers=auth_header
        )
        json_response = response.get_json()
        self.assertEqual(200, response.status_code)

        return json_response.get('data')[0]

    def test_search_shopping_chart_exist_shopping_chart_user_id_returns_shopping_chart(  # noqa
        self,
    ):
        with self.app.app_context():
            shopping_chart = self.get_rand_shopping_chart()
            payload = {
                'search': [
                    {
                        'field_name': 'user_id',
                        'field_value': shopping_chart.user_id,
                    },
                ],
            }

            json_data = self.__request(payload)
            self.assertEqual(shopping_chart.user_id, json_data.get('user_id'))
