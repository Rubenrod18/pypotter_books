import random

import factory
from sqlalchemy import func

from app.blueprints.base import BaseFactory
from app.blueprints.book import Book
from app.blueprints.shopping_cart import ShoppingCart
from app.blueprints.shopping_cart import ShoppingCartBook


class ShoppingCartBookFactory(BaseFactory):
    class Meta:
        model = ShoppingCartBook

    units = factory.Faker('pyint', min_value=1, max_value=5)

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


class ShoppingCartBookInputFactory(BaseFactory):
    @factory.lazy_attribute
    def book_ids(self):
        return list(
            {
                Book.query.filter_by(deleted_at=None)
                .order_by(func.rand())
                .first()
                .id
                for _ in range(5)
            }
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
    def units(self):
        return [random.randint(1, 5) for _ in range(5)]
