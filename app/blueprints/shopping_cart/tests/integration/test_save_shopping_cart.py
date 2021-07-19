import factory

from ..factory import ShoppingCartFactory
from ._base_integration_test import _ShoppingCartBaseIntegrationTest


class TestSaveShoppingCart(_ShoppingCartBaseIntegrationTest):
    def test_is_shopping_chart_created_shopping_chart_does_not_exist_returns_shopping_chart(  # noqa
        self,
    ):
        with self.app.app_context():
            data = factory.build(dict, FACTORY_CLASS=ShoppingCartFactory)

            admin_user = self.get_rand_admin_user()
            auth_header = self.build_auth_header(admin_user.email)
            response = self.client.post(
                self.base_path, json=data, headers=auth_header
            )
            json_response = response.get_json()
            json_data = json_response.get('data')

            self.assertEqual(201, response.status_code)
            self.assertEqual(data['user_id'], json_data.get('user_id'))
            self.assertTrue(json_data.get('created_at'))
            self.assertEqual(
                json_data.get('updated_at'), json_data.get('created_at')
            )
            self.assertIsNone(json_data.get('deleted_at'))
