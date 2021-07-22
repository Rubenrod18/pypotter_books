from sqlalchemy import func

from app.blueprints.base import BaseTest
from app.blueprints.role import Role
from app.blueprints.shopping_cart import ShoppingCart
from app.blueprints.user import User
from app.blueprints.user import UserRoles
from app.extensions import db


class _ShoppingCartBaseIntegrationTest(BaseTest):
    def setUp(self):
        super(_ShoppingCartBaseIntegrationTest, self).setUp()
        self.base_path = '/api/shopping_carts'

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
    def get_rand_shopping_chart():
        return (
            ShoppingCart.query.filter_by(deleted_at=None)
            .order_by(func.rand())
            .first()
        )
