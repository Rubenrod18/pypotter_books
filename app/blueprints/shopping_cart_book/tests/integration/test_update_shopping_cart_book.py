import factory

from ..factory import ShoppingCartBookFactory
from ._base_integration_test import _ShoppingCartBookBaseIntegrationTest


class TestUpdateShoppingCartBook(_ShoppingCartBookBaseIntegrationTest):
    def test_is_shopping_cart_book_updated_shopping_cart_book_exist_previously_returns_shopping_cart_book(  # noqa
        self,
    ):
        data = factory.build(dict, FACTORY_CLASS=ShoppingCartBookFactory)

        admin_user = self.get_rand_admin_user()
        auth_header = self.build_auth_header(admin_user.email)
        response = self.client.put(
            f'{self.base_path}/{self.shopping_cart_book.id}',
            json=data,
            headers=auth_header,
        )
        json_response = response.get_json()
        json_data = json_response.get('data')

        self.assertEqual(200, response.status_code)
        self.assertEqual(self.shopping_cart_book.id, json_data.get('id'))
        self.assertEqual(
            data['shopping_cart_id'], json_data.get('shopping_cart_id')
        )
        self.assertEqual(data['book_id'], json_data.get('book_id'))
        self.assertEqual(data['discount'], json_data.get('discount'))
        self.assertTrue(json_data.get('created_at'))
        self.assertGreaterEqual(
            json_data.get('updated_at'), json_data.get('created_at')
        )
        self.assertIsNone(json_data.get('deleted_at'))
