from sqlalchemy import func

from app.blueprints.base import BaseTest
from app.blueprints.role import Role


class TestDeleteRole(BaseTest):

    def setUp(self, *args, **kwargs):
        super(TestDeleteRole, self).setUp()
        self.base_path = '/api/roles'

    def test_delete_role(self):
        with self.app.app_context():
            role_id = (Role.query.filter_by(deleted_at=None)
                       .order_by(func.rand())
                       .first()
                       .id)

            response = self.client.delete(f'{self.base_path}/{role_id}',
                                          json={})
            json_response = response.get_json()
            json_data = json_response.get('data')

            self.assertEqual(200, response.status_code)
            self.assertEqual(role_id, json_data.get('id'))
            self.assertIsNotNone(json_data.get('deleted_at'))
            self.assertEqual(json_data.get('deleted_at'),
                             json_data.get('updated_at'))
