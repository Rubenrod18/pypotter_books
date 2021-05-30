"""Image column from tbl_books can be nullable

Revision ID: 9b92b7f9419b
Revises: 6237364477c5
Create Date: 2021-05-30 12:22:19.098473

"""
from alembic import op
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9b92b7f9419b'
down_revision = '6237364477c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        'tbl_books', 'image', existing_type=mysql.LONGBLOB(), nullable=True
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        'tbl_books', 'image', existing_type=mysql.LONGBLOB(), nullable=False
    )
    # ### end Alembic commands ###