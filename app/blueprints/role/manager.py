from app.blueprints.base import BaseManager
from .models import Role


class RoleManager(BaseManager):

    def __init__(self):
        super(BaseManager, self).__init__()
        self.model = Role
