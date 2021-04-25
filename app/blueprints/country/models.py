"""

References
----------
ISO_3166-1: https://en.wikipedia.org/wiki/ISO_3166-1

"""
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import PrimaryKeyConstraint
from sqlalchemy import String
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import relationship

from app.blueprints.base import BaseMixin
from app.blueprints.currency import Currency
from app.extensions import db


class Country(db.Model, BaseMixin):
    __tablename__ = BaseMixin.tbl('countries')

    country_id = Column(
        Integer,
        ForeignKey(
            Currency.id,
            name=BaseMixin.fk(__tablename__, Currency.__tablename__),
        ),
        nullable=False,
    )

    name = Column(String(255), nullable=False)
    alpha_2_code = Column(String(2), nullable=False)
    alpha_3_code = Column(String(3), nullable=False)
    numeric_code = Column(String(3), nullable=False)

    currencies = relationship(Currency, backref=__tablename__)

    __table_args__ = (
        PrimaryKeyConstraint('id', name=BaseMixin.pk(__tablename__)),
    )
    __local_table_args__ = (
        UniqueConstraint(
            'name',
            'alpha_2_code',
            'alpha_3_code',
            'numeric_code',
            name=BaseMixin.uq(
                __tablename__, 'name_alpha_2_code_alpha_3_code_numeric_code'
            ),
        ),
    )
