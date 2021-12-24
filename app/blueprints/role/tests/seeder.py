from .factories import AdminRoleSeedFactory
from .factories import ClientRoleSeedFactory
from .factories import Role
from app.decorators import seed_actions


class Seeder:
    name = 'RoleSeeder'
    priority = 0

    @staticmethod
    def __create_admin_role() -> None:
        admin_role = Role.query.filter_by(name='admin').first()

        if admin_role is None:
            AdminRoleSeedFactory()

    @staticmethod
    def __create_client_role() -> None:
        client_role = Role.query.filter_by(name='client').first()

        if client_role is None:
            ClientRoleSeedFactory()

    @seed_actions
    def __init__(self):
        self.__create_admin_role()
        self.__create_client_role()
