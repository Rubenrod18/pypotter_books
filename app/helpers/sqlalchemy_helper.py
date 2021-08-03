from flask_sqlalchemy import get_debug_queries
from flask_sqlalchemy import SQLAlchemy


class SqlAlchemyHelper:
    @staticmethod
    def show_last_sql_query() -> None:
        info = get_debug_queries()[-1]
        print(info.statement, info.parameters, info.duration, sep='\n')

    @staticmethod
    def get_all_db_models(db: SQLAlchemy) -> dict:
        return {
            mapper.class_.__name__: mapper.class_
            for mapper in db.Model.registry.mappers
        }
