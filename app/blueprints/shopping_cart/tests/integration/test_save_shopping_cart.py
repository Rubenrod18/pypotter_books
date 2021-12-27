import factory

from ._base_integration_test import _ShoppingCartBaseIntegrationTest
from app.blueprints.book.tests.factories import BookFactory
from app.blueprints.shopping_cart_book.tests.factories import (
    ShoppingCartBookInputFactory,
)


class TestSaveShoppingCart(_ShoppingCartBaseIntegrationTest):
    def test_is_shopping_cart_created_shopping_cart_does_not_exist_returns_shopping_cart(  # noqa
        self,
    ):
        [BookFactory() for _ in range(5)]
        data = {'units': [3, 2, 1, 4, 2], 'book_ids': [1, 2, 3, 4, 5]}

        admin_user = self.get_active_admin_user()
        auth_header = self.build_auth_header(admin_user.email)
        response = self.client.post(
            self.base_path, json=data, headers=auth_header
        )
        json_response = response.get_json()
        json_data = json_response.get('data')

        self.assertEqual(201, response.status_code, msg=json_response)
        self.assertTrue(isinstance(json_data.get('id'), int))
        self.assertEqual(admin_user.id, json_data.get('user_id'))
        self.assertEqual(86.4, json_data.get('total_price'))
        self.assertTrue(json_data.get('created_at'))
        self.assertEqual(
            json_data.get('updated_at'), json_data.get('created_at')
        )
        self.assertIsNone(json_data.get('deleted_at'))

        books = json_data.get('books')
        for index, item in enumerate(books):
            self.assertTrue(isinstance(item['id'], int))
            self.assertEqual(json_data.get('id'), item.get('shopping_cart_id'))
            self.assertEqual(data['book_ids'][index], item.get('book_id'))
            self.assertEqual(data['units'][index], item.get('units'))
            self.assertTrue(item.get('created_at'))
            self.assertEqual(item.get('updated_at'), item.get('created_at'))
            self.assertIsNone(item.get('deleted_at'))

    def test_is_shopping_cart_book_not_created_units_and_book_ids_are_invalid_returns_validation_error_response(  # noqa
        self,
    ):
        data = factory.build(
            dict,
            FACTORY_CLASS=ShoppingCartBookInputFactory,
            **{'units': [1, 2, 3, 4, 5, 6]}
        )

        admin_user = self.get_active_admin_user()
        auth_header = self.build_auth_header(admin_user.email)
        response = self.client.post(
            self.base_path, json=data, headers=auth_header
        )
        json_response = response.get_json()

        self.assertEqual(422, response.status_code, msg=json_response)
        self.assertEqual(
            ['The book ids field has not same quantity than units field'],
            json_response.get('message', {}).get('book_ids'),
        )
