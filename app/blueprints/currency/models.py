"""

References
----------
ISO 4217: https://en.wikipedia.org/wiki/ISO_4217#Active_codes

"""
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import PrimaryKeyConstraint
from sqlalchemy import String
from sqlalchemy import UniqueConstraint

from app.blueprints.base import BaseMixin
from app.extensions import db


class Currency(db.Model, BaseMixin):
    __tablename__ = BaseMixin.tbl('currencies')

    code = Column(String(3), nullable=False)
    decimals = Column(
        Integer, doc='The number of digits after the decimal separator'
    )
    name = Column(String(255), nullable=False)
    name_plural = Column(String(255), nullable=False)
    num = Column(String(3), nullable=False)
    symbol = Column(String(10), nullable=False)
    symbol_native = Column(String(10), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('id', name=BaseMixin.pk(__tablename__)),
        UniqueConstraint('name', name=BaseMixin.uq(__tablename__, 'name')),
        UniqueConstraint('code', name=BaseMixin.uq(__tablename__, 'code')),
    )
