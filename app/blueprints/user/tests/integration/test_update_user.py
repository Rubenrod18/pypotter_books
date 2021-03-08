import os
from random import choice

import factory
from sqlalchemy import func

from app.blueprints.base import BaseTest
from app.blueprints.role import Role
from app.blueprints.user import User, UserFactory
from app.utils import ignore_keys


class TestUpdateUser(BaseTest):

    def setUp(self, *args, **kwargs):
        super(TestUpdateUser, self).setUp()
        self.base_path = '/api/users'

    def test_update_user_is_sending_valid_request_is_updated(self):
        with self.app.app_context():
            user_id = (User.query.filter_by(deleted_at=None)
                       .order_by(func.random())
                       .first()
                       .id)
            role = (Role.query.filter_by(deleted_at=None)
                    .order_by(func.random())
                    .first())

            exclude = ['active', 'created_at', 'updated_at', 'deleted_at',
                       'created_id', 'fs_uniquifier', 'roles', 'genre']
            data = ignore_keys(factory.build(dict, FACTORY_CLASS=UserFactory),
                               exclude)
            data['genre'] = choice(['male', 'female'])
            data['password'] = os.getenv('TEST_USER_PASSWORD')
            data['role_id'] = role.id

            response = self.client.put(f'{self.base_path}/{user_id}', json=data)
            json_response = response.get_json()
            json_data = json_response.get('data')

            self.assertEqual(200, response.status_code)
            self.assertEqual(data.get('name'), json_data.get('name'))
            self.assertEqual(data.get('last_name'), json_data.get('last_name'))
            self.assertEqual(data.get('birth_date'),
                             json_data.get('birth_date'))
            self.assertEqual(data.get('genre'), json_data.get('genre'))
            self.assertTrue(json_data.get('created_at'))
            self.assertGreater(json_data.get('updated_at'),
                               json_data.get('created_at'))
            self.assertIsNone(json_data.get('deleted_at'))

            role_data = json_data.get('roles')[0]

            self.assertEqual(role.name, role_data.get('name'))
            self.assertEqual(role.label, role_data.get('label'))
