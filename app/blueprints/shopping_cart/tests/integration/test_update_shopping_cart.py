from ._base_integration_test import _ShoppingCartBaseIntegrationTest


class TestUpdateShoppingCart(_ShoppingCartBaseIntegrationTest):
    def test_is_shopping_cart_updated_shopping_cart_exist_previously_returns_shopping_cart(  # noqa
        self,
    ):
        def create_shopping_cart():
            response = self.client.post(
                self.base_path,
                json={'units': [3, 2, 1, 4, 2], 'book_ids': [1, 2, 3, 4, 5]},
                headers=self.build_auth_header(
                    self.get_rand_admin_user().email
                ),
            )
            return response.get_json().get('data')['id']

        shopping_cart_id = create_shopping_cart()
        data = {'units': [3], 'book_ids': [1]}

        admin_user = self.get_rand_admin_user()
        auth_header = self.build_auth_header(admin_user.email)
        response = self.client.put(
            f'{self.base_path}/{shopping_cart_id}',
            json=data,
            headers=auth_header,
        )
        json_response = response.get_json()
        json_data = json_response.get('data')

        self.assertEqual(200, response.status_code, msg=json_response)
        self.assertEqual(shopping_cart_id, json_data.get('id'))
        self.assertEqual(admin_user.id, json_data.get('user_id'))
        self.assertEqual(24, json_data.get('total_price'))
        self.assertTrue(json_data.get('created_at'))
        self.assertGreaterEqual(
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

    def test_is_shopping_cart_not_updated_shopping_cart_doesnt_exist_returns_validation_error_response(  # noqa
        self,
    ):
        data = {'units': [3], 'book_ids': [1]}
        shopping_cart_id = 999

        admin_user = self.get_rand_admin_user()
        auth_header = self.build_auth_header(admin_user.email)
        response = self.client.put(
            f'{self.base_path}/{shopping_cart_id}',
            json=data,
            headers=auth_header,
        )
        json_response = response.get_json()

        self.assertEqual(422, response.status_code, msg=json_response)
        self.assertEqual(
            json_response.get('message'),
            'The record doesn\'t exist',
            msg=json_response,
        )
