import factory
from sqlalchemy import func

from app.blueprints.base import BaseFactory
from app.blueprints.bill import Bill
from app.blueprints.currency import Currency
from app.blueprints.shopping_cart import ShoppingCart


class BillFactory(BaseFactory):
    class Meta:
        model = Bill

    @factory.lazy_attribute
    def currency_id(self):
        currency = (
            Currency.query.filter_by(deleted_at=None)
            .order_by(func.rand())
            .first()
        )
        return currency.id

    @factory.lazy_attribute
    def shopping_cart_id(self):
        shopping_cart = (
            ShoppingCart.query.filter_by(deleted_at=None)
            .order_by(func.rand())
            .first()
        )
        return shopping_cart.id

    @factory.lazy_attribute
    def user_id(self):
        shopping_cart = ShoppingCart.query.filter_by(
            id=self.shopping_cart_id
        ).first()

        return shopping_cart.user_id
