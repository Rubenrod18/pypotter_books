import os
from datetime import timedelta
from random import randint, choice

import factory
from faker import Faker
from faker.providers import person, date_time
from flask_security import hash_password
from sqlalchemy import func

from app.extensions import db
from .. import UserManager
from ..models import User
from ...role.models import Role

user_manager = UserManager()

# TODO: move to common.py
fake = Faker()
fake.add_provider(person)
fake.add_provider(date_time)


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = 'commit'

    name = factory.Faker('name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    # TODO: use Genre model
    genre = factory.Iterator(['m', 'f'])
    birth_date = (fake.date_time_between(start_date='-30y', end_date='-5y')
                  .strftime('%Y-%m-%d'))
    active = factory.Faker('boolean')

    @factory.lazy_attribute
    def password(self):
        return hash_password(os.getenv('TEST_USER_PASSWORD'))

    @factory.lazy_attribute
    def created_id(self):
        user = (User.query.filter(User.roles.any(Role.name == 'admin'))
                .filter_by(**{'deleted_at': None})
                .order_by(func.rand())
                .first())
        if user:
            user = user.id
        return user

    @factory.lazy_attribute
    def fs_uniquifier(self):
        user = user_manager.get_last_record()
        return 1 if user is None else user.id + 1

    @factory.lazy_attribute
    def roles(self):
        role = (Role.query.filter_by(deleted_at=None)
                .order_by(func.rand())
                .first())
        return [role]

    @factory.lazy_attribute
    def created_at(self):
        return fake.date_time_between(start_date='-3y', end_date='now')

    @factory.lazy_attribute
    def deleted_at(self):
        return choice([
            fake.date_time_between(start_date='-1y', end_date='now'),
            None
        ])

    @factory.lazy_attribute
    def updated_at(self):
        if self.deleted_at:
            updated_at = self.deleted_at
        else:
            updated_at = self.created_at + timedelta(days=randint(1, 30),
                                                     minutes=randint(0, 60))
        return updated_at
