from ._base_integration_test import _BookPriceBaseIntegrationTest


class TestSearchBookPrices(_BookPriceBaseIntegrationTest):
    def __request(self, payload):
        admin_user = self.get_active_admin_user()
        auth_header = self.build_auth_header(admin_user.email)
        response = self.client.post(
            f'{self.base_path}/search', json=payload, headers=auth_header
        )
        json_response = response.get_json()
        self.assertEqual(200, response.status_code)

        return json_response.get('data')[0]

    def test_search_book_price_exist_book_price_country_id_returns_book_price(
        self,
    ):
        payload = {
            'search': [
                {
                    'field_name': 'country_id',
                    'field_value': self.book_price.country_id,
                },
            ],
        }

        json_data = self.__request(payload)
        self.assertEqual(
            self.book_price.country_id, json_data.get('country_id')
        )

    def test_search_book_price_exist_book_price_book_id_returns_book_price(
        self,
    ):
        payload = {
            'search': [
                {
                    'field_name': 'book_id',
                    'field_value': self.book_price.book_id,
                },
            ],
        }

        json_data = self.__request(payload)
        self.assertEqual(self.book_price.book_id, json_data.get('book_id'))
