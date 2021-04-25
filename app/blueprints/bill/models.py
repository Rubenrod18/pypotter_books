from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import PrimaryKeyConstraint
from sqlalchemy.orm import relationship

from app.blueprints.base import BaseMixin
from app.blueprints.currency.models import Currency
from app.blueprints.shopping_cart.models import ShoppingCart
from app.blueprints.user import User
from app.extensions import db


class Bill(db.Model, BaseMixin):
    __tablename__ = BaseMixin.tbl('bills')

    user_id = Column(
        Integer,
        ForeignKey(
            User.id, name=BaseMixin.fk(__tablename__, User.__tablename__)
        ),
        nullable=False,
    )
    currency_id = Column(
        Integer,
        ForeignKey(
            Currency.id,
            name=BaseMixin.fk(__tablename__, Currency.__tablename__),
        ),
        nullable=False,
    )
    shopping_cart_id = Column(
        Integer,
        ForeignKey(
            ShoppingCart.id,
            name=BaseMixin.fk(__tablename__, ShoppingCart.__tablename__),
        ),
        nullable=False,
    )

    client = relationship(User, backref=__tablename__)
    currency = relationship(Currency, backref=__tablename__)
    shopping_cart = relationship(ShoppingCart, backref=__tablename__)

    __table_args__ = (
        PrimaryKeyConstraint('id', name=BaseMixin.pk(__tablename__)),
    )
