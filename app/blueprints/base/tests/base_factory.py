import factory

from app.extensions import db


class BaseFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        sqlalchemy_session = db.session

    @classmethod
    def get_db_session(cls):
        return cls._meta.sqlalchemy_session
