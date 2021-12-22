from ._base_integration_test import _ShoppingCartBaseIntegrationTest


class TestGetShoppingCart(_ShoppingCartBaseIntegrationTest):
    def test_is_shopping_cart_obtained_shopping_cart_exists_returns_shopping_cart(  # noqa
        self,
    ):
        admin_user = self.get_rand_admin_user()
        auth_header = self.build_auth_header(admin_user.email)
        response = self.client.get(
            f'{self.base_path}/{self.shopping_cart.id}',
            json={},
            headers=auth_header,
        )
        json_response = response.get_json()
        json_data = json_response.get('data')

        self.assertEqual(200, response.status_code)
        self.assertEqual(self.shopping_cart.id, json_data.get('id'))
        self.assertEqual(self.shopping_cart.user_id, json_data.get('user_id'))
        self.assertEqual(
            self.shopping_cart.total_price, json_data.get('total_price')
        )
        self.assertEqual(
            self.shopping_cart.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            json_data.get('created_at'),
        )
        self.assertEqual(
            self.shopping_cart.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
            json_data.get('updated_at'),
        )
        self.assertEqual(
            self.shopping_cart.deleted_at, json_data.get('deleted_at')
        )
