import factory

from ...factory import BookPriceFactory
from ._base_integration_test import _BookPriceBaseIntegrationTest


class TestUpdateBookPrice(_BookPriceBaseIntegrationTest):
    def test_is_book_updated_book_exist_previously_returns_book(
        self,
    ):
        data = factory.build(dict, FACTORY_CLASS=BookPriceFactory)

        admin_user = self.get_rand_admin_user()
        auth_header = self.build_auth_header(admin_user.email)
        response = self.client.put(
            f'{self.base_path}/{self.book_price.id}',
            json=data,
            headers=auth_header,
        )
        json_response = response.get_json()
        json_data = json_response.get('data')

        self.assertEqual(200, response.status_code)
        self.assertEqual(self.book_price.id, json_data.get('id'))
        self.assertEqual(data['country_id'], json_data.get('country_id'))
        self.assertEqual(data['book_id'], json_data.get('book_id'))
        self.assertEqual(data['price'], json_data.get('price'))
        self.assertTrue(json_data.get('created_at'))
        self.assertGreaterEqual(
            json_data.get('updated_at'), json_data.get('created_at')
        )
        self.assertIsNone(json_data.get('deleted_at'))
