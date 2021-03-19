import factory

from app.blueprints.role import RoleFactory
from app.utils import ignore_keys
from ._base_integration_test import _RoleBaseIntegrationTest


class TestSaveRole(_RoleBaseIntegrationTest):

    def test_save_role(self):
        with self.app.app_context():
            exclude = ['name']
            data = ignore_keys(factory.build(dict, FACTORY_CLASS=RoleFactory),
                               exclude)

            admin_user = self.get_rand_admin_user()
            auth_header = self.build_auth_header(admin_user.email)
            response = self.client.post(self.base_path, json=data,
                                        headers=auth_header)
            json_response = response.get_json()
            json_data = json_response.get('data')

            self.assertEqual(201, response.status_code)
            self.assertEqual(data['label'], json_data.get('label'))
            self.assertEqual(data['label'].lower().replace(' ', '-'),
                             json_data.get('name'))
            self.assertTrue(json_data.get('created_at'))
            self.assertEqual(json_data.get('updated_at'),
                             json_data.get('created_at'))
            self.assertIsNone(json_data.get('deleted_at'))
