from ._base_integration_test import _BookPriceBaseIntegrationTest


class TestDeleteBookPrice(_BookPriceBaseIntegrationTest):
    def test_is_book_price_deleted_book_price_exists_returns_book_price_deleted(  # noqa
        self,
    ):
        admin_user = self.get_active_admin_user()
        auth_header = self.build_auth_header(admin_user.email)
        response = self.client.delete(
            f'{self.base_path}/{self.book_price.id}',
            json={},
            headers=auth_header,
        )
        json_response = response.get_json()
        json_data = json_response.get('data')

        self.assertEqual(200, response.status_code)
        self.assertEqual(self.book_price.id, json_data.get('id'))
        self.assertIsNotNone(json_data.get('deleted_at'))
        self.assertGreaterEqual(
            json_data.get('deleted_at'), json_data.get('updated_at')
        )
