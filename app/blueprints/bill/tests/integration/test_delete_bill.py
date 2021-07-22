from ._base_integration_test import _BillBaseIntegrationTest


class TestDeleteBill(_BillBaseIntegrationTest):
    def test_is_bill_deleted_bill_exists_returns_bill_deleted(
        self,
    ):
        with self.app.app_context():
            bill_id = self.get_rand_bill().id

            admin_user = self.get_rand_admin_user()
            auth_header = self.build_auth_header(admin_user.email)
            response = self.client.delete(
                f'{self.base_path}/{bill_id}',
                json={},
                headers=auth_header,
            )
            json_response = response.get_json()
            json_data = json_response.get('data')

            self.assertEqual(200, response.status_code)
            self.assertEqual(bill_id, json_data.get('id'))
            self.assertIsNotNone(json_data.get('deleted_at'))
            self.assertGreaterEqual(
                json_data.get('deleted_at'), json_data.get('updated_at')
            )
