import enum

from flask_security import UserMixin, SQLAlchemyUserDatastore
from sqlalchemy import (Enum, Column, String, Boolean, Date, Integer,
                        ForeignKey)
from sqlalchemy.orm import relationship, backref

from app.blueprints.base.model import BaseMixin
from app.blueprints.role.model import Role as RoleModel
from app.extensions import db


class Genre(enum.Enum):
    m = 'male'
    f = 'female'

    def __str__(self):
        """Returns str instead Genre object.

        References
        ----------
        how to serialise a enum property in sqlalchemy using marshmallow
        https://stackoverflow.com/questions/44717768/how-to-serialise-a-enum-property-in-sqlalchemy-using-marshmallow

        """
        return self.value

    @classmethod
    def to_list(cls, get_values=True):
        attr = 'name'
        if get_values:
            attr = 'value'
        return [getattr(_, attr) for _ in list(cls)]

    @classmethod
    def find_by_value(cls, value):
        found_name = None
        attrs = cls.to_list(False)

        for attr in attrs:
            genre = getattr(cls, attr)
            if genre.value == value:
                found_name = genre.name
                break
        return found_name


class User(db.Model, BaseMixin, UserMixin):
    """User database model.

    References
    ----------
    fs_uniquier field is required by flask-security-too:
    https://flask-security-too.readthedocs.io/en/stable/changelog.html#version-4-0-0

    """
    __tablename__ = 'users'

    created_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    created_by = relationship('User', remote_side='User.id')
    roles = relationship('Role', secondary='user_roles',
                         backref=backref('users', lazy='dynamic'))

    fs_uniquifier = Column(String(255), unique=True, nullable=False)
    name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    genre = Column(Enum(Genre), nullable=False)
    birth_date = Column(Date, nullable=False)
    active = Column(Boolean, server_default='1', nullable=False)

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)


class UserRoles(db.Model):
    __tablename__ = 'user_roles'

    id = Column(Integer, primary_key=True)
    user_id = Column('user_id', Integer, ForeignKey('users.id'))
    role_id = Column('role_id', Integer, ForeignKey('roles.id'))


user_datastore = SQLAlchemyUserDatastore(db, User, RoleModel)
