from sqlalchemy import func

from app.blueprints.base import BaseTest
from app.blueprints.book import Book
from app.blueprints.role import Role
from app.blueprints.user import User
from app.blueprints.user import UserRoles
from app.extensions import db


class _BookBaseIntegrationTest(BaseTest):
    def setUp(self):
        super(_BookBaseIntegrationTest, self).setUp()
        self.base_path = '/api/books'

    @staticmethod
    def get_rand_admin_user():
        return (
            db.session.query(User)
            .join(UserRoles)
            .join(Role)
            .filter(
                User.deleted_at.is_(None),
                User.active == 1,
                Role.name == 'admin',
            )
            .first()
        )

    @staticmethod
    def get_rand_book():
        return (
            Book.query.filter_by(deleted_at=None).order_by(func.rand()).first()
        )
