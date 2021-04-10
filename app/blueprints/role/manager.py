from .models import Role
from app.blueprints.base import BaseManager


class RoleManager(BaseManager):
    def __init__(self):
        super(BaseManager, self).__init__()
        self.model = Role
