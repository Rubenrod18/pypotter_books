from ._base_integration_test import _BookStockBaseIntegrationTest


class TestSearchBookStocks(_BookStockBaseIntegrationTest):
    def __request(self, payload):
        admin_user = self.get_rand_admin_user()
        auth_header = self.build_auth_header(admin_user.email)
        response = self.client.post(
            f'{self.base_path}/search', json=payload, headers=auth_header
        )
        json_response = response.get_json()
        self.assertEqual(200, response.status_code)

        return json_response.get('data')[0]

    def test_search_book_stock_exist_book_stock_country_id_returns_book_stock(
        self,
    ):
        with self.app.app_context():
            book_stock = self.get_rand_book_stock()
            payload = {
                'search': [
                    {
                        'field_name': 'country_id',
                        'field_value': book_stock.country_id,
                    },
                ],
            }

            json_data = self.__request(payload)
            self.assertEqual(
                book_stock.country_id, json_data.get('country_id')
            )

    def test_search_book_stock_exist_book_stock_book_id_returns_book_stock(
        self,
    ):
        with self.app.app_context():
            book_stock = self.get_rand_book_stock()
            payload = {
                'search': [
                    {
                        'field_name': 'book_id',
                        'field_value': book_stock.book_id,
                    },
                ],
            }

            json_data = self.__request(payload)
            self.assertEqual(book_stock.book_id, json_data.get('book_id'))

    def test_search_book_stock_exist_book_stock_quantity_returns_book_stock(
        self,
    ):
        with self.app.app_context():
            book_stock = self.get_rand_book_stock()
            payload = {
                'search': [
                    {
                        'field_name': 'quantity',
                        'field_value': book_stock.quantity,
                    },
                ],
            }

            json_data = self.__request(payload)
            self.assertEqual(book_stock.quantity, json_data.get('quantity'))
