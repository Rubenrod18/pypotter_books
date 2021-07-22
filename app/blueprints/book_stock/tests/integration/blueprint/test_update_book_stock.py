import factory

from ...factory import BookStockFactory
from ._base_integration_test import _BookStockBaseIntegrationTest


class TestUpdateBookPrice(_BookStockBaseIntegrationTest):
    def test_is_book_updated_book_exist_previously_returns_book(
        self,
    ):
        with self.app.app_context():
            book_id = self.get_rand_book_stock().id
            data = factory.build(dict, FACTORY_CLASS=BookStockFactory)

            admin_user = self.get_rand_admin_user()
            auth_header = self.build_auth_header(admin_user.email)
            response = self.client.put(
                f'{self.base_path}/{book_id}',
                json=data,
                headers=auth_header,
            )
            json_response = response.get_json()
            json_data = json_response.get('data')

            self.assertEqual(200, response.status_code)
            self.assertEqual(book_id, json_data.get('id'))
            self.assertEqual(data['country_id'], json_data.get('country_id'))
            self.assertEqual(data['book_id'], json_data.get('book_id'))
            self.assertEqual(data['quantity'], json_data.get('quantity'))
            self.assertTrue(json_data.get('created_at'))
            self.assertGreaterEqual(
                json_data.get('updated_at'), json_data.get('created_at')
            )
            self.assertIsNone(json_data.get('deleted_at'))
