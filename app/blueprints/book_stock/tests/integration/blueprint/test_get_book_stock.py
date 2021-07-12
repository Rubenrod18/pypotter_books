from ._base_integration_test import _BookStockBaseIntegrationTest


class TestGetBookStock(_BookStockBaseIntegrationTest):
    def test_is_book_stock_obtained_book_stock_exists_returns_book_stock(
        self,
    ):
        with self.app.app_context():
            book_stock = self.get_rand_book_stock()

            admin_user = self.get_rand_admin_user()
            auth_header = self.build_auth_header(admin_user.email)
            response = self.client.get(
                f'{self.base_path}/{book_stock.id}',
                json={},
                headers=auth_header,
            )
            json_response = response.get_json()
            json_data = json_response.get('data')

            self.assertEqual(200, response.status_code)
            self.assertEqual(book_stock.id, json_data.get('id'))
            self.assertEqual(
                book_stock.country_id, json_data.get('country_id')
            )
            self.assertEqual(book_stock.book_id, json_data.get('book_id'))
            self.assertEqual(book_stock.quantity, json_data.get('quantity'))
            self.assertEqual(
                book_stock.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                json_data.get('created_at'),
            )
            self.assertEqual(
                book_stock.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
                json_data.get('updated_at'),
            )
            self.assertEqual(
                book_stock.deleted_at, json_data.get('deleted_at')
            )
