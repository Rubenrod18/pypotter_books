from ._base_integration_test import _ShoppingCartBaseIntegrationTest


class TestGetShoppingCart(_ShoppingCartBaseIntegrationTest):
    def test_is_shopping_chart_obtained_shopping_chart_exists_returns_shopping_chart(  # noqa
        self,
    ):
        with self.app.app_context():
            shopping_chart = self.get_rand_shopping_chart()

            admin_user = self.get_rand_admin_user()
            auth_header = self.build_auth_header(admin_user.email)
            response = self.client.get(
                f'{self.base_path}/{shopping_chart.id}',
                json={},
                headers=auth_header,
            )
            json_response = response.get_json()
            json_data = json_response.get('data')

            self.assertEqual(200, response.status_code)
            self.assertEqual(shopping_chart.id, json_data.get('id'))
            self.assertEqual(shopping_chart.user_id, json_data.get('user_id'))
            self.assertEqual(
                shopping_chart.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                json_data.get('created_at'),
            )
            self.assertEqual(
                shopping_chart.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
                json_data.get('updated_at'),
            )
            self.assertEqual(
                shopping_chart.deleted_at, json_data.get('deleted_at')
            )
