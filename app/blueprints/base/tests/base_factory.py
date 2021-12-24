import factory

from app.extensions import db


class BaseFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        abstract = True
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = 'commit'


class BaseSeedFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        abstract = True
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = None

    @classmethod
    def get_db_session(cls):
        return cls._meta.sqlalchemy_session
