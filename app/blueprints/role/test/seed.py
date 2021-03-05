from app.blueprints.role.model import Role
from app.blueprints.role.test.factories import RoleFactory
from app.utils.decorators import seed_actions


class RoleSeeder:
    name = 'RoleSeeder'

    @staticmethod
    def _create_admin_role() -> None:
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
    def _create_team_leader() -> None:
        team_leader_role = Role.query.filter_by(name='team_leader').first()

        if team_leader_role is None:
            params = {
                'name': 'team_leader',
                'description': 'Team leader',
                'label': 'Team leader',
                'deleted_at': None,
            }
            RoleFactory.create(**params)

    @staticmethod
    def _create_worker_role() -> None:
        worker_role = Role.query.filter_by(name='worker').first()

        if worker_role is None:
            params = {
                'name': 'worker',
                'description': 'Worker',
                'label': 'Worker',
                'deleted_at': None,
            }
            RoleFactory.create(**params)

    @seed_actions
    def __init__(self):
        self._create_admin_role()
        self._create_team_leader()
        self._create_worker_role()
