from ._base_integration_test import _BillBaseIntegrationTest


class TestSearchCurrencies(_BillBaseIntegrationTest):
    def __request(self, payload):
        admin_user = self.get_rand_admin_user()
        auth_header = self.build_auth_header(admin_user.email)
        response = self.client.post(
            f'{self.base_path}/search', json=payload, headers=auth_header
        )
        json_response = response.get_json()
        self.assertEqual(200, response.status_code)

        return json_response.get('data')[0]

    def test_search_bill_exist_bill_user_id_returns_bill(
        self,
    ):
        with self.app.app_context():
            bill = self.get_rand_bill()
            payload = {
                'search': [
                    {
                        'field_name': 'user_id',
                        'field_value': bill.user_id,
                    },
                ],
            }

            json_data = self.__request(payload)
            self.assertEqual(bill.user_id, json_data.get('user_id'))

    def test_search_bill_exist_bill_currency_id_returns_bill(
        self,
    ):
        with self.app.app_context():
            bill = self.get_rand_bill()
            payload = {
                'search': [
                    {
                        'field_name': 'currency_id',
                        'field_value': bill.currency_id,
                    },
                ],
            }

            json_data = self.__request(payload)
            self.assertEqual(bill.currency_id, json_data.get('currency_id'))

    def test_search_bill_exist_bill_shopping_cart_id_returns_bill(
        self,
    ):
        with self.app.app_context():
            bill = self.get_rand_bill()
            payload = {
                'search': [
                    {
                        'field_name': 'shopping_cart_id',
                        'field_value': bill.shopping_cart_id,
                    },
                ],
            }

            json_data = self.__request(payload)
            self.assertEqual(
                bill.shopping_cart_id, json_data.get('shopping_cart_id')
            )
