import unicodedata

import factory

from ..models import Role
from ..models import ROLE_NAME_DELIMITER
from app.extensions import db


def _slugify(role):
    return role.name.capitalize().replace('_', ' ')


class RoleFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Role
        # Use the not-so-global scoped_session
        # Warning: DO NOT USE common.Session()!
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = 'commit'

    name = factory.Faker('name')
    description = factory.Faker('sentence')

    @factory.lazy_attribute
    def label(self):
        clean_name = (
            unicodedata.normalize('NFKD', self.name)
            .encode('ascii', 'ignore')
            .decode('utf8')
        )
        return clean_name.capitalize().replace(ROLE_NAME_DELIMITER, ' ')
