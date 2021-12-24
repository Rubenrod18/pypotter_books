from ._base_integration_test import _BookPriceBaseIntegrationTest


class TestGetBookPrice(_BookPriceBaseIntegrationTest):
    def test_is_book_price_obtained_book_price_exists_returns_book_price(
        self,
    ):
        admin_user = self.get_active_admin_user()
        auth_header = self.build_auth_header(admin_user.email)
        response = self.client.get(
            f'{self.base_path}/{self.book_price.id}',
            json={},
            headers=auth_header,
        )
        json_response = response.get_json()
        json_data = json_response.get('data')

        self.assertEqual(200, response.status_code)
        self.assertEqual(self.book_price.id, json_data.get('id'))
        self.assertEqual(
            self.book_price.country_id, json_data.get('country_id')
        )
        self.assertEqual(self.book_price.book_id, json_data.get('book_id'))
        self.assertEqual(self.book_price.price, json_data.get('price'))
        self.assertEqual(
            self.book_price.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            json_data.get('created_at'),
        )
        self.assertEqual(
            self.book_price.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
            json_data.get('updated_at'),
        )
        self.assertEqual(
            self.book_price.deleted_at, json_data.get('deleted_at')
        )
