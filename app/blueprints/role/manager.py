from app.blueprints.base import BaseManager
from .model import Role as RoleModel


class RoleManager(BaseManager):

    def __init__(self):
        super(BaseManager, self).__init__()
        self.model = RoleModel
