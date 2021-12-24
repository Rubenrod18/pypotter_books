from ._base_integration_test import _BillBaseIntegrationTest
from app.blueprints.user.tests.factories import AdminUserFactory


class TestSearchCurrencies(_BillBaseIntegrationTest):
    def __request(self, payload):
        admin_user = AdminUserFactory(active=True, deleted_at=None)
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
        payload = {
            'search': [
                {
                    'field_name': 'user_id',
                    'field_value': self.bill.user_id,
                },
            ],
        }

        json_data = self.__request(payload)
        self.assertEqual(self.bill.user_id, json_data.get('user_id'))

    def test_search_bill_exist_bill_currency_id_returns_bill(
        self,
    ):
        payload = {
            'search': [
                {
                    'field_name': 'currency_id',
                    'field_value': self.bill.currency_id,
                },
            ],
        }

        json_data = self.__request(payload)
        self.assertEqual(self.bill.currency_id, json_data.get('currency_id'))

    def test_search_bill_exist_bill_shopping_cart_id_returns_bill(
        self,
    ):
        payload = {
            'search': [
                {
                    'field_name': 'shopping_cart_id',
                    'field_value': self.bill.shopping_cart_id,
                },
            ],
        }

        json_data = self.__request(payload)
        self.assertEqual(
            self.bill.shopping_cart_id, json_data.get('shopping_cart_id')
        )
