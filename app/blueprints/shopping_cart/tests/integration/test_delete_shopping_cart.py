from ._base_integration_test import _ShoppingCartBaseIntegrationTest


class TestDeleteShoppingCart(_ShoppingCartBaseIntegrationTest):
    def test_is_shopping_chart_deleted_shopping_chart_exists_returns_shopping_chart_deleted(  # noqa
        self,
    ):
        with self.app.app_context():
            shopping_chart_id = self.get_rand_shopping_chart().id

            admin_user = self.get_rand_admin_user()
            auth_header = self.build_auth_header(admin_user.email)
            response = self.client.delete(
                f'{self.base_path}/{shopping_chart_id}',
                json={},
                headers=auth_header,
            )
            json_response = response.get_json()
            json_data = json_response.get('data')

            self.assertEqual(200, response.status_code)
            self.assertEqual(shopping_chart_id, json_data.get('id'))
            self.assertIsNotNone(json_data.get('deleted_at'))
            self.assertGreaterEqual(
                json_data.get('deleted_at'), json_data.get('updated_at')
            )
