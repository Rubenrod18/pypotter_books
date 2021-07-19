from ._base_integration_test import _ShoppingCartBookBaseIntegrationTest


class TestSearchCurrencies(_ShoppingCartBookBaseIntegrationTest):
    def __request(self, payload):
        admin_user = self.get_rand_admin_user()
        auth_header = self.build_auth_header(admin_user.email)
        response = self.client.post(
            f'{self.base_path}/search', json=payload, headers=auth_header
        )
        json_response = response.get_json()
        self.assertEqual(200, response.status_code)

        return json_response.get('data')[0]

    def test_search_shopping_cart_book_exist_shopping_cart_book_shopping_cart_id_returns_shopping_cart_book(  # noqa
        self,
    ):
        with self.app.app_context():
            shopping_cart_book = self.get_rand_shopping_cart_book()
            payload = {
                'search': [
                    {
                        'field_name': 'shopping_cart_id',
                        'field_value': shopping_cart_book.shopping_cart_id,
                    },
                ],
            }

            json_data = self.__request(payload)
            self.assertEqual(
                shopping_cart_book.shopping_cart_id,
                json_data.get('shopping_cart_id'),
            )

    def test_search_shopping_cart_book_exist_shopping_cart_book_book_id_returns_shopping_cart_book(  # noqa
        self,
    ):
        with self.app.app_context():
            shopping_cart_book = self.get_rand_shopping_cart_book()
            payload = {
                'search': [
                    {
                        'field_name': 'book_id',
                        'field_value': shopping_cart_book.book_id,
                    },
                ],
            }

            json_data = self.__request(payload)
            self.assertEqual(
                shopping_cart_book.book_id, json_data.get('book_id')
            )

    def test_search_shopping_cart_book_exist_shopping_cart_book_discount_returns_shopping_cart_book(  # noqa
        self,
    ):
        with self.app.app_context():
            shopping_cart_book = self.get_rand_shopping_cart_book()
            payload = {
                'search': [
                    {
                        'field_name': 'discount',
                        'field_value': shopping_cart_book.discount,
                    },
                ],
            }

            json_data = self.__request(payload)
            self.assertEqual(
                shopping_cart_book.discount, json_data.get('discount')
            )
