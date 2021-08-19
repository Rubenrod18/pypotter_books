import factory

from ..factory import ShoppingCartFactory
from ._base_integration_test import _ShoppingCartBaseIntegrationTest


class TestUpdateShoppingCart(_ShoppingCartBaseIntegrationTest):
    def test_is_shopping_cart_updated_shopping_cart_exist_previously_returns_shopping_cart(  # noqa
        self,
    ):
        data = factory.build(dict, FACTORY_CLASS=ShoppingCartFactory)

        admin_user = self.get_rand_admin_user()
        auth_header = self.build_auth_header(admin_user.email)
        response = self.client.put(
            f'{self.base_path}/{self.shopping_cart.id}',
            json=data,
            headers=auth_header,
        )
        json_response = response.get_json()
        json_data = json_response.get('data')

        self.assertEqual(200, response.status_code)
        self.assertEqual(self.shopping_cart.id, json_data.get('id'))
        self.assertEqual(data['user_id'], json_data.get('user_id'))
        self.assertTrue(json_data.get('created_at'))
        self.assertGreaterEqual(
            json_data.get('updated_at'), json_data.get('created_at')
        )
        self.assertIsNone(json_data.get('deleted_at'))
