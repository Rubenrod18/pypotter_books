"""

References
----------
Naming Conventions in SQL:
https://www.c-sharpcorner.com/UploadFile/f0b2ed/what-is-naming-convention/

"""
from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import TIMESTAMP


class _DatabaseMixin:
    @staticmethod
    def tbl(name: str) -> str:
        """Build table name."""
        return f'tbl_{name}'

    @staticmethod
    def vw(result_set: str) -> str:
        """Build view name."""
        return f'vw_{result_set}'

    @staticmethod
    def pk(table_name: str) -> str:
        """Build primary key constraint name."""
        return f'pk_{table_name}'

    @staticmethod
    def fk(target_table: str, source_table: str) -> str:
        """Build foreign key constraint name."""
        return f'fk_{target_table}_{source_table}'

    @staticmethod
    def df(table_name: str, column_name: str) -> str:
        """Build default constraint name."""
        return f'df_{table_name}_{column_name}'

    @staticmethod
    def uq(table_name: str, column_name: str) -> str:
        """Build unique constraint name."""
        return f'uq_{table_name}_{column_name}'

    @staticmethod
    def chk(table_name: str, column_name: str) -> str:
        """Build unique constraint name."""
        return f'chk_{table_name}_{column_name}'

    @staticmethod
    def fn(action_name: str) -> str:
        """Build user defined function name."""
        return f'fn_{action_name}'

    @staticmethod
    def usp(table_name: str, action_name: str) -> str:
        """Build user defined stored procedure name."""
        return f'usp_{table_name}_{action_name}'

    @staticmethod
    def tr(table_name: str, column_name: str) -> str:
        """Build trigger name."""
        return f'tr_{table_name}_{column_name}'


class BaseMixin(_DatabaseMixin):
    id = Column(Integer)

    created_at = Column(
        TIMESTAMP, default=datetime.utcnow, server_default=None, nullable=False
    )
    updated_at = Column(
        TIMESTAMP,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )
    deleted_at = Column(TIMESTAMP, server_default=None, nullable=True)
