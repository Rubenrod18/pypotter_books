from .factory import Role
from .factory import RoleFactory
from app.decorators import seed_actions


class Seeder:
    name = 'RoleSeeder'

    @staticmethod
    def __create_admin_role() -> None:
        admin_role = Role.query.filter_by(name='admin').first()

        if admin_role is None:
            params = {
                'name': 'admin',
                'description': 'Administrator',
                'label': 'Admin',
                'deleted_at': None,
            }
            RoleFactory.create(**params)

    @staticmethod
    def __create_client_role() -> None:
        client_role = Role.query.filter_by(name='client').first()

        if client_role is None:
            params = {
                'name': 'client',
                'description': 'Client',
                'label': 'Client',
                'deleted_at': None,
            }
            RoleFactory.create(**params)

    @seed_actions
    def __init__(self):
        self.__create_admin_role()
        self.__create_client_role()
