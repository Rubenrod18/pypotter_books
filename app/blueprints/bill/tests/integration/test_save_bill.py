import factory

from ..factory import BillFactory
from ._base_integration_test import _BillBaseIntegrationTest


class TestSaveBill(_BillBaseIntegrationTest):
    def test_is_bill_created_bill_does_not_exist_returns_bill(
        self,
    ):
        with self.app.app_context():
            data = factory.build(dict, FACTORY_CLASS=BillFactory)

            admin_user = self.get_rand_admin_user()
            auth_header = self.build_auth_header(admin_user.email)
            response = self.client.post(
                self.base_path, json=data, headers=auth_header
            )
            json_response = response.get_json()
            json_data = json_response.get('data')

            self.assertEqual(201, response.status_code)
            self.assertEqual(data['user_id'], json_data.get('user_id'))
            self.assertEqual(data['currency_id'], json_data.get('currency_id'))
            self.assertEqual(
                data['shopping_cart_id'], json_data.get('shopping_cart_id')
            )
            self.assertTrue(json_data.get('created_at'))
            self.assertEqual(
                json_data.get('updated_at'), json_data.get('created_at')
            )
            self.assertIsNone(json_data.get('deleted_at'))
