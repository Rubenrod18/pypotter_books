from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import PrimaryKeyConstraint
from sqlalchemy.orm import relationship

from app.blueprints.base import BaseMixin
from app.blueprints.book.models import Book
from app.blueprints.user import User
from app.extensions import db


class ShoppingCart(db.Model, BaseMixin):
    __tablename__ = BaseMixin.tbl('shopping_carts')

    user_id = Column(
        Integer,
        ForeignKey(
            User.id, name=BaseMixin.fk(__tablename__, User.__tablename__)
        ),
        nullable=False,
    )

    client = relationship(User, backref='shopping_carts')

    __table_args__ = (
        PrimaryKeyConstraint('id', name=BaseMixin.pk(__tablename__)),
    )


class ShoppingCartBook(db.Model, BaseMixin):
    __tablename__ = BaseMixin.tbl('shopping_cart_books')

    shopping_cart_id = Column(
        Integer,
        ForeignKey(
            ShoppingCart.id,
            name=BaseMixin.fk(__tablename__, ShoppingCart.__tablename__),
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
    discount = Column(Float, nullable=False)

    shopping_cart = relationship(ShoppingCart, backref='shopping_cart_books')
    book = relationship(Book, backref='shopping_cart_books')

    __table_args__ = (
        PrimaryKeyConstraint('id', name=BaseMixin.pk(__tablename__)),
    )
