from sqlalchemy import func

from app.blueprints.base import BaseTest
from app.blueprints.role import Role


class TestGetRole(BaseTest):

    def setUp(self, *args, **kwargs):
        super(TestGetRole, self).setUp()
        self.base_path = '/api/roles'

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
