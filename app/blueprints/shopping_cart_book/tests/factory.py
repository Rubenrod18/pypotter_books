import factory
from sqlalchemy import func

from app.blueprints.book import Book
from app.blueprints.shopping_cart import ShoppingCart
from app.blueprints.shopping_cart import ShoppingCartBook
from app.extensions import db


class ShoppingCartBookFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = ShoppingCartBook
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = 'commit'

    discount = factory.Faker(
        'pyfloat', right_digits=2, positive=True, max_value=10.0
    )

    @factory.lazy_attribute
    def shopping_cart_id(self):
        shopping_cart = (
            ShoppingCart.query.filter_by(deleted_at=None)
            .order_by(func.rand())
            .first()
        )
        return shopping_cart.id

    @factory.lazy_attribute
    def book_id(self):
        book = (
            Book.query.filter_by(deleted_at=None).order_by(func.rand()).first()
        )
        return book.id
