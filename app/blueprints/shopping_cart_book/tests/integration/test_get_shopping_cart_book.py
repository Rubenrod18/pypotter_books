from ._base_integration_test import _ShoppingCartBookBaseIntegrationTest


class TestGetShoppingCartBook(_ShoppingCartBookBaseIntegrationTest):
    def test_is_shopping_cart_book_obtained_shopping_cart_book_exists_returns_shopping_cart_book(  # noqa
        self,
    ):
        with self.app.app_context():
            shopping_cart_book = self.get_rand_shopping_cart_book()

            admin_user = self.get_rand_admin_user()
            auth_header = self.build_auth_header(admin_user.email)
            response = self.client.get(
                f'{self.base_path}/{shopping_cart_book.id}',
                json={},
                headers=auth_header,
            )
            json_response = response.get_json()
            json_data = json_response.get('data')

            self.assertEqual(200, response.status_code)
            self.assertEqual(shopping_cart_book.id, json_data.get('id'))
            self.assertEqual(
                shopping_cart_book.shopping_cart_id,
                json_data.get('shopping_cart_id'),
            )
            self.assertEqual(
                shopping_cart_book.book_id, json_data.get('book_id')
            )
            self.assertEqual(
                shopping_cart_book.discount, json_data.get('discount')
            )
            self.assertEqual(
                shopping_cart_book.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                json_data.get('created_at'),
            )
            self.assertEqual(
                shopping_cart_book.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
                json_data.get('updated_at'),
            )
            self.assertEqual(
                shopping_cart_book.deleted_at, json_data.get('deleted_at')
            )
