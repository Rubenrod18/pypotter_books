from ._base_integration_test import _BillBaseIntegrationTest


class TestGetBill(_BillBaseIntegrationTest):
    def test_is_bill_obtained_bill_exists_returns_bill(
        self,
    ):
        admin_user = self.get_rand_admin_user()
        auth_header = self.build_auth_header(admin_user.email)
        response = self.client.get(
            f'{self.base_path}/{self.bill.id}',
            json={},
            headers=auth_header,
        )
        json_response = response.get_json()
        json_data = json_response.get('data')

        self.assertEqual(200, response.status_code)
        self.assertEqual(self.bill.id, json_data.get('id'))
        self.assertEqual(self.bill.user_id, json_data.get('user_id'))
        self.assertEqual(self.bill.currency_id, json_data.get('currency_id'))
        self.assertEqual(
            self.bill.shopping_cart_id, json_data.get('shopping_cart_id')
        )
        self.assertEqual(
            self.bill.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            json_data.get('created_at'),
        )
        self.assertEqual(
            self.bill.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
            json_data.get('updated_at'),
        )
        self.assertEqual(self.bill.deleted_at, json_data.get('deleted_at'))
