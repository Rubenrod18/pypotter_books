import enum

from flask_security import SQLAlchemyUserDatastore
from flask_security import UserMixin
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import Enum
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import PrimaryKeyConstraint
from sqlalchemy import String
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import backref
from sqlalchemy.orm import relationship

from app.blueprints.base.models import BaseMixin
from app.blueprints.country import Country
from app.blueprints.role.models import Role
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


class UserBase(BaseMixin, UserMixin):
    pass


class User(db.Model, UserBase):
    """User database model.

    References
    ----------
    fs_uniquier field is required by flask-security-too:
    https://flask-security-too.readthedocs.io/en/stable/changelog.html#version-4-0-0

    """

    __tablename__ = BaseMixin.tbl('users')

    created_id = Column(
        Integer,
        ForeignKey(
            f'{__tablename__}.id',
            name=BaseMixin.fk(__tablename__, __tablename__),
        ),
        nullable=True,
    )
    country_id = Column(
        Integer,
        ForeignKey(
            Country.id, name=BaseMixin.fk(__tablename__, Country.__tablename__)
        ),
        nullable=True,
    )
    fs_uniquifier = Column(String(255), nullable=False)

    name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    genre = Column(Enum(Genre), nullable=False)
    birth_date = Column(Date, nullable=False)
    active = Column(Boolean, server_default='1', nullable=False)

    created_by = relationship('User', remote_side='User.id')
    roles = relationship(
        'Role',
        secondary='tbl_user_roles',
        backref=backref('users', lazy='dynamic'),
    )

    __table_args__ = (
        PrimaryKeyConstraint('id', name=BaseMixin.pk(__tablename__)),
        UniqueConstraint('email', name=BaseMixin.uq(__tablename__, 'email')),
        UniqueConstraint(
            'fs_uniquifier', name=BaseMixin.uq(__tablename__, 'fs_uniquifier')
        ),
    )

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)


class UserRoles(db.Model, BaseMixin):
    __tablename__ = BaseMixin.tbl('user_roles')

    user_id = Column(
        Integer,
        ForeignKey(
            User.id, name=BaseMixin.fk(__tablename__, User.__tablename__)
        ),
    )
    role_id = Column(
        Integer,
        ForeignKey(
            Role.id, name=BaseMixin.fk(__tablename__, Role.__tablename__)
        ),
    )

    __table_args__ = (
        PrimaryKeyConstraint('id', name=BaseMixin.pk(__tablename__)),
    )


user_datastore = SQLAlchemyUserDatastore(db, User, Role)
