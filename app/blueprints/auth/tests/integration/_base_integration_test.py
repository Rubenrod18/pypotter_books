from sqlalchemy import func

from app.blueprints.base import BaseTest
from app.blueprints.user import User


class _AuthBaseIntegrationTest(BaseTest):

    def setUp(self):
        super(_AuthBaseIntegrationTest, self).setUp()
        self.base_path = '/api/auth'

    @staticmethod
    def get_rand_user():
        return (User.query.filter_by(deleted_at=None, active=True)
                .order_by(func.random())
                .first())
