from sqlalchemy import func

from app.blueprints.base import BaseTest
from app.blueprints.role import Role
from app.blueprints.user import User, UserRoles
from app.extensions import db


class _RoleBaseIntegrationTest(BaseTest):

    def setUp(self):
        super(_RoleBaseIntegrationTest, self).setUp()
        self.base_path = '/api/roles'

    @staticmethod
    def get_rand_admin_user():
        return (db.session.query(User)
                .join(UserRoles)
                .join(Role)
                .filter(User.deleted_at.is_(None),
                        User.active == 1,
                        Role.name == 'admin')
                .first())

    @staticmethod
    def get_rand_role():
        return (Role.query.filter_by(deleted_at=None)
                .order_by(func.rand())
                .first())
