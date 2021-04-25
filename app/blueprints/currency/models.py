"""

References
----------
ISO 4217: https://en.wikipedia.org/wiki/ISO_4217#Active_codes

"""
from sqlalchemy import CheckConstraint
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import PrimaryKeyConstraint
from sqlalchemy import String
from sqlalchemy import UniqueConstraint

from app.blueprints.base import BaseMixin
from app.extensions import db


class Currency(db.Model, BaseMixin):
    __tablename__ = BaseMixin.tbl('currencies')

    name = Column(String(255), nullable=False)
    code = Column(String(3), nullable=False)
    num = Column(String(3), nullable=False)
    decimals = Column(
        Integer, doc='The number of digits after the decimal separator'
    )

    __table_args__ = (
        PrimaryKeyConstraint('id', name=BaseMixin.pk(__tablename__)),
    )
    __local_table_args__ = (
        CheckConstraint(
            decimals >= 0, name=BaseMixin.chk(__tablename__, 'decimals')
        ),
        UniqueConstraint('name', name=BaseMixin.uq(__tablename__, 'name')),
        UniqueConstraint('code', name=BaseMixin.uq(__tablename__, 'code')),
    )
