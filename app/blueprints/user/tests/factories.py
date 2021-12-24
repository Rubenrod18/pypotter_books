import os
import random
from datetime import timedelta
from random import choice
from random import randint

import factory
from sqlalchemy import func

from app.blueprints.base import BaseFactory
from app.blueprints.base import BaseSeedFactory
from app.blueprints.base.tests.base_test import faker
from app.blueprints.role import Role
from app.blueprints.role.tests.factories import AdminRoleFactory
from app.blueprints.role.tests.factories import ClientRoleFactory
from app.blueprints.user import User
from app.blueprints.user import UserManager
from app.wrappers import SecurityWrapper

_user_manager = UserManager()


class UserFactory(BaseFactory):
    class Meta:
        model = User

    name = factory.Faker('name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    # TODO: use Genre model
    genre = factory.Iterator(['m', 'f'])
    birth_date = faker.date_time_between(
        start_date='-30y', end_date='-5y'
    ).strftime('%Y-%m-%d')
    active = factory.Faker('boolean')

    @factory.lazy_attribute
    def password(self):
        return SecurityWrapper.ensure_password(os.getenv('TEST_USER_PASSWORD'))

    @factory.lazy_attribute
    def created_id(self):
        # TODO: study the way to define an user without circular imports
        return None

    @factory.lazy_attribute
    def fs_uniquifier(self):
        user = _user_manager.get_last_record()
        return 1 if user is None else user.id + 1

    @factory.lazy_attribute
    def roles(self):
        return [random.choice([AdminRoleFactory(), ClientRoleFactory()])]

    @factory.lazy_attribute
    def created_at(self):
        return faker.date_time_between(start_date='-3y', end_date='now')

    @factory.lazy_attribute
    def deleted_at(self):
        return choice(
            [faker.date_time_between(start_date='-1y', end_date='now'), None]
        )

    @factory.lazy_attribute
    def updated_at(self):
        if self.deleted_at:
            updated_at = self.deleted_at
        else:
            updated_at = self.created_at + timedelta(
                days=randint(1, 30), minutes=randint(0, 60)
            )
        return updated_at


class AdminUserFactory(UserFactory):
    @factory.lazy_attribute
    def roles(self):
        return [AdminRoleFactory()]


class UserSeedFactory(BaseSeedFactory):
    class Meta:
        model = User

    name = factory.Faker('name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    # TODO: use Genre model
    genre = factory.Iterator(['m', 'f'])
    birth_date = faker.date_time_between(
        start_date='-30y', end_date='-5y'
    ).strftime('%Y-%m-%d')
    active = factory.Faker('boolean')

    @factory.lazy_attribute
    def password(self):
        return SecurityWrapper.ensure_password(os.getenv('TEST_USER_PASSWORD'))

    @factory.lazy_attribute
    def created_id(self):
        user = (
            User.query.filter(User.roles.any(Role.name == 'admin'))
            .filter_by(**{'deleted_at': None})
            .order_by(func.rand())
            .first()
        )
        if user:
            user = user.id
        return user

    @factory.lazy_attribute
    def fs_uniquifier(self):
        user = _user_manager.get_last_record()
        return 1 if user is None else user.id + 1

    @factory.lazy_attribute
    def roles(self):
        role = (
            Role.query.filter_by(deleted_at=None).order_by(func.rand()).first()
        )
        return [role]

    @factory.lazy_attribute
    def created_at(self):
        return faker.date_time_between(start_date='-3y', end_date='now')

    @factory.lazy_attribute
    def deleted_at(self):
        return choice(
            [faker.date_time_between(start_date='-1y', end_date='now'), None]
        )

    @factory.lazy_attribute
    def updated_at(self):
        if self.deleted_at:
            updated_at = self.deleted_at
        else:
            updated_at = self.created_at + timedelta(
                days=randint(1, 30), minutes=randint(0, 60)
            )
        return updated_at
