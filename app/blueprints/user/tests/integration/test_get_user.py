from sqlalchemy import func

from app.blueprints.base import BaseTest
from app.blueprints.user import User


class TestGetUser(BaseTest):

    def setUp(self, *args, **kwargs):
        super(TestGetUser, self).setUp()
        self.base_path = '/api/users'

    def test_get_user_is_sending_valid_request_is_obtained(self):
        with self.app.app_context():
            user = (User.query.filter_by(deleted_at=None)
                    .order_by(func.random())
                    .first())
            role = user.roles[0]

            response = self.client.get(f'{self.base_path}/{user.id}', json={})
            json_response = response.get_json()
            json_data = json_response.get('data')

            self.assertEqual(200, response.status_code)
            self.assertEqual(user.name, json_data.get('name'))
            self.assertEqual(user.last_name, json_data.get('last_name'))
            self.assertEqual(user.birth_date.strftime('%Y-%m-%d'),
                             json_data.get('birth_date'))
            self.assertEqual(user.genre.value, json_data.get('genre'))
            self.assertEqual(user.created_at.strftime('%Y-%m-%dT%H:%M:%S'),
                             json_data.get('created_at'))
            self.assertGreater(json_data.get('updated_at'),
                               json_data.get('created_at'))
            self.assertIsNone(json_data.get('deleted_at'))

            role_data = json_data.get('roles')[0]

            self.assertEqual(role.name, role_data.get('name'))
            self.assertEqual(role.label, role_data.get('label'))
