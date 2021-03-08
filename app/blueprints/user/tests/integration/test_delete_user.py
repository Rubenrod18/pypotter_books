from sqlalchemy import func

from app.blueprints.base import BaseTest
from app.blueprints.user import User


class TestDeleteUser(BaseTest):

    def setUp(self, *args, **kwargs):
        super(TestDeleteUser, self).setUp()
        self.base_path = '/api/users'

    def test_delete_user_is_sending_valid_request_is_deleted(self):
        with self.app.app_context():
            user_id = (User.query.filter_by(deleted_at=None)
                       .order_by(func.random())
                       .first()
                       .id)

            response = self.client.delete(f'{self.base_path}/{user_id}',
                                          json={})
            json_response = response.get_json()
            json_data = json_response.get('data')

            self.assertEqual(200, response.status_code)
            self.assertEqual(user_id, json_data.get('id'))
            self.assertIsNotNone(json_data.get('deleted_at'))
            self.assertEqual(json_data.get('deleted_at'),
                             json_data.get('updated_at'))
