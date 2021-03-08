import factory

from app.blueprints.base import BaseTest
from app.blueprints.role import RoleFactory
from app.utils import ignore_keys


class TestSaveRole(BaseTest):

    def setUp(self, *args, **kwargs):
        super(TestSaveRole, self).setUp()
        self.base_path = '/api/roles'

    def test_save_role(self):
        with self.app.app_context():
            exclude = ['name']
            data = ignore_keys(factory.build(dict, FACTORY_CLASS=RoleFactory),
                               exclude)

            response = self.client.post(self.base_path, json=data)
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
