import unicodedata

import factory

from ..models import Role
from ..models import ROLE_NAME_DELIMITER
from app.blueprints.base import BaseFactory
from app.blueprints.base import BaseSeedFactory


def _slugify(role):
    return role.name.capitalize().replace('_', ' ')


class RoleFactory(BaseFactory):
    class Meta:
        model = Role

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


class RoleSeedFactory(BaseSeedFactory):
    class Meta:
        model = Role

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


class AdminRoleSeedFactory(RoleSeedFactory):
    name = 'admin'
    description = 'Administrator'
    label = 'Admin'


class ClientRoleSeedFactory(RoleSeedFactory):
    name = 'client'
    description = 'Client'
    label = 'Client'


class AdminRoleFactory(RoleSeedFactory):
    name = 'admin'
    description = 'Administrator'
    label = 'Admin'


class ClientRoleFactory(RoleSeedFactory):
    name = 'client'
    description = 'Client'
    label = 'Client'
