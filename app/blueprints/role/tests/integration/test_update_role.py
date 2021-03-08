import factory
from sqlalchemy import func

from app.blueprints.base import BaseTest
from app.blueprints.role import RoleFactory, Role
from app.utils import ignore_keys


class TestUpdateRole(BaseTest):

    def setUp(self, *args, **kwargs):
        super(TestUpdateRole, self).setUp()
        self.base_path = '/api/roles'

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
