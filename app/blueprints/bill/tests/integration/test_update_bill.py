import factory

from ..factories import BillFactory
from ._base_integration_test import _BillBaseIntegrationTest
from app.blueprints.currency.tests.factories import CurrencyFactory
from app.blueprints.shopping_cart.tests.factories import ShoppingCartFactory
from app.blueprints.user.tests.factories import AdminUserFactory


class TestUpdateBill(_BillBaseIntegrationTest):
    def test_is_bill_updated_bill_exist_previously_returns_bill(
        self,
    ):
        currency = CurrencyFactory()
        shopping_cart = ShoppingCartFactory()
        data = factory.build(
            dict,
            FACTORY_CLASS=BillFactory,
            **{
                'currency_id': currency.id,
                'shopping_cart_id': shopping_cart.id,
                'user_id': shopping_cart.user_id,
            },
        )

        admin_user = AdminUserFactory(active=True, deleted_at=None)
        auth_header = self.build_auth_header(admin_user.email)
        response = self.client.put(
            f'{self.base_path}/{self.bill.id}',
            json=data,
            headers=auth_header,
        )
        json_response = response.get_json()
        json_data = json_response.get('data')

        self.assertEqual(200, response.status_code)
        self.assertEqual(self.bill.id, json_data.get('id'))
        self.assertEqual(data['user_id'], json_data.get('user_id'))
        self.assertTrue(json_data.get('created_at'))
        self.assertGreaterEqual(
            json_data.get('updated_at'), json_data.get('created_at')
        )
        self.assertIsNone(json_data.get('deleted_at'))
