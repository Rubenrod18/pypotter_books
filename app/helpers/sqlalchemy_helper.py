from flask_sqlalchemy import get_debug_queries


class SqlAlchemyHelper:
    @staticmethod
    def show_last_sql_query():
        info = get_debug_queries()[0]
        print(info.statement, info.parameters, info.duration, sep='\n')
