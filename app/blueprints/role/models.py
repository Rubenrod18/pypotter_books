from flask_security import RoleMixin
from sqlalchemy import Column, String, Text

from app.blueprints.base.models import BaseMixin
from app.extensions import db


class Role(db.Model, BaseMixin, RoleMixin):
    __tablename__ = 'roles'

    name = Column(String(255), unique=True, nullable=False)
    description = Column(Text, nullable=True)
    label = Column(String(255), nullable=False)

    def __init__(self, *args, **kwargs):
        super(Role, self).__init__(*args, **kwargs)
