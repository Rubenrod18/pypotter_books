import os
from random import choice

import factory
from sqlalchemy import func

from app.blueprints.base import BaseTest
from app.blueprints.role import Role
from app.blueprints.user import UserFactory
from app.utils import ignore_keys


class TestSaveUser(BaseTest):

    def setUp(self, *args, **kwargs):
        super(TestSaveUser, self).setUp()
        self.base_path = '/api/users'

    def test_save_user_is_sending_valid_request_is_created(self):
        with self.app.app_context():
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

            response = self.client.post(self.base_path, json=data)
            json_response = response.get_json()
            json_data = json_response.get('data')

            self.assertEqual(201, response.status_code)
            self.assertEqual(data.get('name'), json_data.get('name'))
            self.assertEqual(data.get('last_name'), json_data.get('last_name'))
            self.assertEqual(data.get('birth_date'),
                             json_data.get('birth_date'))
            self.assertEqual(data.get('genre'), json_data.get('genre'))
            self.assertTrue(json_data.get('created_at'))
            self.assertEqual(json_data.get('updated_at'),
                             json_data.get('created_at'))
            self.assertIsNone(json_data.get('deleted_at'))

            role_data = json_data.get('roles')[0]

            self.assertEqual(role.name, role_data.get('name'))
            self.assertEqual(role.label, role_data.get('label'))
