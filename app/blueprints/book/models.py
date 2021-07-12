from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import PrimaryKeyConstraint
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import UniqueConstraint
from sqlalchemy.dialects.mysql import LONGBLOB
from sqlalchemy.orm import relationship

from app.blueprints.base import BaseMixin
from app.blueprints.country.models import Country
from app.extensions import db


_BOOK_TBL = BaseMixin.tbl('books')


class BookPrice(db.Model, BaseMixin):
    __tablename__ = BaseMixin.tbl('book_prices')

    book_id = Column(
        Integer,
        ForeignKey(
            f'{_BOOK_TBL}.id', name=BaseMixin.fk(__tablename__, _BOOK_TBL)
        ),
        nullable=False,
    )
    country_id = Column(
        Integer,
        ForeignKey(
            f'{Country.__tablename__}.id',
            name=BaseMixin.fk(__tablename__, Country.__tablename__),
        ),
        nullable=False,
    )
    vat = Column(Float, nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('id', name=BaseMixin.pk(__tablename__)),
        UniqueConstraint(
            'country_id',
            'book_id',
            name=BaseMixin.uq(__tablename__, 'country_id_book_id'),
        ),
    )


class BookStock(db.Model, BaseMixin):
    __tablename__ = BaseMixin.tbl('book_stocks')

    book_id = Column(
        Integer,
        ForeignKey(
            f'{_BOOK_TBL}.id', name=BaseMixin.fk(__tablename__, _BOOK_TBL)
        ),
        nullable=False,
    )
    country_id = Column(
        Integer,
        ForeignKey(
            f'{Country.__tablename__}.id',
            name=BaseMixin.fk(__tablename__, Country.__tablename__),
        ),
        nullable=False,
    )

    quantity = Column(Integer, nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('id', name=BaseMixin.pk(__tablename__)),
        UniqueConstraint(
            'country_id',
            'book_id',
            name=BaseMixin.uq(__tablename__, 'book_id_country_id'),
        ),
    )


class Book(db.Model, BaseMixin):
    __tablename__ = _BOOK_TBL

    title = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    isbn = Column(String(255), nullable=False)
    total_pages = Column(Integer, nullable=False)
    publisher = Column(String(255), nullable=False)
    published_date = Column(Date, nullable=False)
    language = Column(String(255), nullable=False)
    dimensions = Column(String(255), nullable=False)
    image = Column(LONGBLOB, nullable=True)

    book_stocks = relationship('BookStock', backref=__tablename__)
    book_prices = relationship('BookPrice', backref=__tablename__)

    __table_args__ = (
        PrimaryKeyConstraint('id', name=BaseMixin.pk(__tablename__)),
        UniqueConstraint('isbn', name=BaseMixin.uq(__tablename__, 'isbn')),
    )
