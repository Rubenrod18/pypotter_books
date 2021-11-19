import os
from random import choice

import factory

from ._base_integration_test import _UserBaseIntegrationTest
from app.blueprints.role import Role
from app.blueprints.user import UserFactory
from app.helpers import DictHelper


class TestUpdateUser(_UserBaseIntegrationTest):
    def test_update_user_is_sending_valid_request_is_updated(self):
        role = self.find_random_record(Role, **{'deleted_at': None})

        exclude = [
            'active',
            'created_at',
            'updated_at',
            'deleted_at',
            'created_id',
            'fs_uniquifier',
            'roles',
            'genre',
        ]
        data = DictHelper.ignore_keys(
            factory.build(dict, FACTORY_CLASS=UserFactory), exclude
        )
        data['genre'] = choice(['male', 'female'])
        data['password'] = os.getenv('TEST_USER_PASSWORD')
        data['role_id'] = role.id

        admin_user = self.get_rand_admin_user()
        auth_header = self.build_auth_header(admin_user.email)
        response = self.client.put(
            f'{self.base_path}/{self.user.id}', json=data, headers=auth_header
        )
        json_response = response.get_json()
        json_data = json_response.get('data')

        self.assertEqual(200, response.status_code)
        self.assertEqual(data.get('name'), json_data.get('name'))
        self.assertEqual(data.get('last_name'), json_data.get('last_name'))
        self.assertEqual(data.get('birth_date'), json_data.get('birth_date'))
        self.assertEqual(data.get('genre'), json_data.get('genre'))
        self.assertTrue(json_data.get('created_at'))
        self.assertGreaterEqual(
            json_data.get('updated_at'), json_data.get('created_at')
        )
        self.assertIsNone(json_data.get('deleted_at'))

        role_data = json_data.get('roles')[0]

        self.assertEqual(role.name, role_data.get('name'))
        self.assertEqual(role.label, role_data.get('label'))
