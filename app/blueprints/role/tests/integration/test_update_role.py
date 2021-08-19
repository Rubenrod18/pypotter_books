import factory

from ...models import ROLE_NAME_DELIMITER
from ._base_integration_test import _RoleBaseIntegrationTest
from app.blueprints.role import RoleFactory
from app.helpers import DictHelper


class TestUpdateRole(_RoleBaseIntegrationTest):
    def test_update_role(self):
        exclude = ['name']
        data = DictHelper.ignore_keys(
            factory.build(dict, FACTORY_CLASS=RoleFactory), exclude
        )

        admin_user = self.get_rand_admin_user()
        auth_header = self.build_auth_header(admin_user.email)
        response = self.client.put(
            f'{self.base_path}/{self.role.id}', json=data, headers=auth_header
        )
        json_response = response.get_json()
        json_data = json_response.get('data')

        self.assertEqual(200, response.status_code)
        self.assertEqual(self.role.id, json_data.get('id'))
        self.assertEqual(
            data.get('label').lower().replace(' ', ROLE_NAME_DELIMITER),
            json_data.get('name'),
        )
        self.assertEqual(data.get('label'), json_data.get('label'))
        self.assertTrue(json_data.get('created_at'))
        self.assertGreaterEqual(
            json_data.get('updated_at'), json_data.get('created_at')
        )
        self.assertIsNone(json_data.get('deleted_at'))
