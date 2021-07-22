from flask_security import RoleMixin
from sqlalchemy import Column
from sqlalchemy import PrimaryKeyConstraint
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import UniqueConstraint

from app.blueprints.base.models import BaseMixin
from app.extensions import db

ROLE_NAME_DELIMITER = '_'


class RoleBase(BaseMixin, RoleMixin):
    pass


class Role(db.Model, RoleBase):
    __tablename__ = BaseMixin.tbl('roles')

    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    label = Column(String(255), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('id', name=BaseMixin.pk(__tablename__)),
    )
    __local_table_args__ = (
        UniqueConstraint('name', name=BaseMixin.uq(__tablename__, 'name')),
    )

    def __init__(self, *args, **kwargs):
        super(Role, self).__init__(*args, **kwargs)
