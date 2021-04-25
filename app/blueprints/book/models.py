from sqlalchemy import BLOB
from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import PrimaryKeyConstraint
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import relationship

from app.blueprints.base import BaseMixin
from app.blueprints.country.models import Country
from app.extensions import db


class Book(db.Model, BaseMixin):
    __tablename__ = BaseMixin.tbl('books')

    title = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    isbn = Column(String(255), nullable=False)
    total_pages = Column(Integer, nullable=False)
    publisher = Column(String(255), nullable=False)
    published_date = Column(Date, nullable=False)
    language = Column(String(255), nullable=False)
    dimensions = Column(String(255), nullable=False)
    image = Column(BLOB, nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('id', name=BaseMixin.pk(__tablename__)),
    )
    __local_table_args__ = (
        UniqueConstraint('isbn', name=BaseMixin.uq(__tablename__, 'isbn')),
    )


class BookPrice(db.Model, BaseMixin):
    __tablename__ = BaseMixin.tbl('book_prices')

    book_id = Column(
        Integer,
        ForeignKey(
            Book.id, name=BaseMixin.fk(__tablename__, Book.__tablename__)
        ),
        nullable=False,
    )
    country_id = Column(
        Integer,
        ForeignKey(
            Country.id, name=BaseMixin.fk(__tablename__, Country.__tablename__)
        ),
        nullable=False,
    )
    vat = Column(Float, nullable=False)

    book = relationship(Book, backref=__tablename__)
    country = relationship(Country, backref=__tablename__)

    __table_args__ = (
        PrimaryKeyConstraint('id', name=BaseMixin.pk(__tablename__)),
    )


class BookStock(db.Model, BaseMixin):
    __tablename__ = BaseMixin.tbl('book_stocks')

    country_id = Column(
        Integer,
        ForeignKey(
            Country.id, name=BaseMixin.fk(__tablename__, Country.__tablename__)
        ),
        nullable=False,
    )
    book_id = Column(
        Integer,
        ForeignKey(
            Book.id, name=BaseMixin.fk(__tablename__, Book.__tablename__)
        ),
        nullable=False,
    )

    quantity = Column(Integer, nullable=False)

    book = relationship(Book, backref=__tablename__)
    country = relationship(Country, backref=__tablename__)

    __table_args__ = (
        PrimaryKeyConstraint('id', name=BaseMixin.pk(__tablename__)),
    )
