"""Add new price column to tbl_book_prices table

Revision ID: d7d4c9e6d6b7
Revises: b54058e21e09
Create Date: 2021-11-19 17:55:22.932201

"""
import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = 'd7d4c9e6d6b7'
down_revision = 'b54058e21e09'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        'tbl_book_prices', sa.Column('price', sa.Float(), nullable=False)
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tbl_book_prices', 'price')
    # ### end Alembic commands ###
