from app.blueprints.base import BaseManager
from .models import User


class UserManager(BaseManager):

    def __init__(self):
        super(BaseManager, self).__init__()
        self.model = User

    def find_by_email(self, email: str, **kwargs):
        query = {'email': email}
        if kwargs:
            query.update(kwargs)
        return self.model.query.filter_by(**query).first()

    def get_last_record(self):
        return (self.model.query
                .order_by(self.model.id.desc())
                .limit(1)
                .first())
