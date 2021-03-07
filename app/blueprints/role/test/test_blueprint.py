import factory
from sqlalchemy import func

from app.blueprints.base.test.common import BaseTest
from app.blueprints.role.model import Role
from app.blueprints.role.test.factories import RoleFactory
from app.utils import ignore_keys


class TestBlueprint(BaseTest):

    def setUp(self, *args, **kwargs):
        super(TestBlueprint, self).setUp()
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

    def test_update_role(self):
        with self.app.app_context():
            role_id = (Role.query.filter_by(deleted_at=None)
                       .order_by(func.rand())
                       .first()
                       .id)

            exclude = ['name']
            data = ignore_keys(factory.build(dict, FACTORY_CLASS=RoleFactory),
                               exclude)

            response = self.client.put(f'{self.base_path}/{role_id}', json=data)
            json_response = response.get_json()
            json_data = json_response.get('data')

            self.assertEqual(200, response.status_code)
            self.assertEqual(role_id, json_data.get('id'))
            self.assertEqual(data.get('label').lower().replace(' ', '-'),
                             json_data.get('name'))
            self.assertEqual(data.get('label'), json_data.get('label'))
            self.assertTrue(json_data.get('created_at'))
            self.assertGreaterEqual(json_data.get('updated_at'),
                                    json_data.get('created_at'))
            self.assertIsNone(json_data.get('deleted_at'))

    def test_get_role(self):
        with self.app.app_context():
            role = (Role.query.filter_by(deleted_at=None)
                    .order_by(func.rand())
                    .first())

            response = self.client.get(f'{self.base_path}/{role.id}', json={})
            json_response = response.get_json()
            json_data = json_response.get('data')

            self.assertEqual(200, response.status_code)
            self.assertEqual(role.id, json_data.get('id'))
            self.assertEqual(role.label.lower().replace(' ', '_'),
                             json_data.get('name'))
            self.assertEqual(role.label, json_data.get('label'))
            self.assertEqual(role.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                             json_data.get('created_at'))
            self.assertEqual(role.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
                             json_data.get('updated_at'))
            self.assertEqual(role.deleted_at, json_data.get('deleted_at'))

    def test_delete_role(self):
        with self.app.app_context():
            role_id = (Role.query.filter_by(deleted_at=None)
                       .order_by(func.rand())
                       .first()
                       .id)

            response = self.client.delete(f'{self.base_path}/{role_id}', json={})
            json_response = response.get_json()
            json_data = json_response.get('data')

            self.assertEqual(200, response.status_code)
            self.assertEqual(role_id, json_data.get('id'))
            self.assertIsNotNone(json_data.get('deleted_at'))
            self.assertEqual(json_data.get('deleted_at'),
                             json_data.get('updated_at'))
