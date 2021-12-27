import factory

from ...factories import BookStockFactory
from ._base_integration_test import _BookStockBaseIntegrationTest


class TestSaveBookStock(_BookStockBaseIntegrationTest):
    def test_is_book_stock_created_book_stock_does_not_exist_returns_book_stock(  # noqa
        self,
    ):
        data = factory.build(dict, FACTORY_CLASS=BookStockFactory)

        admin_user = self.get_active_admin_user()
        auth_header = self.build_auth_header(admin_user.email)

        response = self.client.post(
            self.base_path, json=data, headers=auth_header
        )
        json_response = response.get_json()
        json_data = json_response.get('data')

        self.assertEqual(201, response.status_code)
        self.assertEqual(data['country_id'], json_data.get('country_id'))
        self.assertEqual(data['book_id'], json_data.get('book_id'))
        self.assertEqual(data['stock'], json_data.get('stock'))
        self.assertTrue(json_data.get('created_at'))
        self.assertEqual(
            json_data.get('updated_at'), json_data.get('created_at')
        )
        self.assertIsNone(json_data.get('deleted_at'))
