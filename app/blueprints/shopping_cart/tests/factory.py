import factory

from app.blueprints.shopping_cart import ShoppingCart
from app.blueprints.user import User
from app.extensions import db


class ShoppingCartFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = ShoppingCart
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = 'commit'

    @factory.lazy_attribute
    def user_id(self):
        rand_user = (
            User.query.with_entities(User.id)
            .filter_by(deleted_at=None)
            .order_by(db.func.random())
            .first()
        )
        return rand_user.id


class UserWithShoppingCartFactory(ShoppingCartFactory):
    @factory.lazy_attribute
    def user_id(self):
        rand_user = (
            User.query.with_entities(User.id)
            .outerjoin(ShoppingCart)
            .filter_by(deleted_at=None)
            .order_by(db.func.random())
            .first()
        )
        return rand_user.id


class UserWithoutShoppingCartFactory(ShoppingCartFactory):
    @factory.lazy_attribute
    def user_id(self):
        subquery = ShoppingCart.query.with_entities(ShoppingCart.user_id)

        user = (
            User.query.filter(
                User.deleted_at.is_(None), ~User.id.in_(subquery)
            )
            .order_by(db.func.random())
            .first()
        )

        return user.id
