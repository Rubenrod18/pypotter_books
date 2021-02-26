import enum

from flask_security import UserMixin
from sqlalchemy import (Enum, Column, String, Boolean, Date, Integer,
                        ForeignKey)
from sqlalchemy.orm import relationship, backref

from app.blueprints.base.model import BaseMixin
from app.extensions import db


class _Genre(enum.Enum):
    m = 'male'
    f = 'female'


class User(db.Model, BaseMixin, UserMixin):
    """User database model.

    References
    ----------
    fs_uniquier field is required by flask-security-too:
    https://flask-security-too.readthedocs.io/en/stable/changelog.html#version-4-0-0

    """
    __tablename__ = 'users'

    created_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    # TODO: pending to define
    # created_by = relationship('User', remote_side=['User.id'])
    roles = relationship('Role', secondary='user_roles',
                         backref=backref('users', lazy='dynamic'))

    fs_uniquifier = Column(String(255), unique=True, nullable=False)
    name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    genre = Column(Enum(_Genre), nullable=False)
    birth_date = Column(Date, nullable=False)
    active = Column(Boolean, server_default='1', nullable=False)

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)


class UserRoles(db.Model):
    __tablename__ = 'user_roles'

    id = Column(Integer, primary_key=True)
    user_id = Column('user_id', Integer, ForeignKey('users.id'))
    role_id = Column('role_id', Integer, ForeignKey('roles.id'))
