"""Initial migration

Revision ID: 70f517aedf18
Revises:
Create Date: 2021-04-25 11:03:25.026775

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.mysql import LONGBLOB


# revision identifiers, used by Alembic.
revision = '70f517aedf18'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'tbl_books',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
        sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
        sa.Column('deleted_at', sa.TIMESTAMP(), nullable=True),
        sa.Column('title', sa.String(length=255), nullable=False),
        sa.Column('author', sa.String(length=255), nullable=False),
        sa.Column('description', sa.Text(), nullable=False),
        sa.Column('isbn', sa.String(length=255), nullable=False),
        sa.Column('total_pages', sa.Integer(), nullable=False),
        sa.Column('publisher', sa.String(length=255), nullable=False),
        sa.Column('published_date', sa.Date(), nullable=False),
        sa.Column('language', sa.String(length=255), nullable=False),
        sa.Column('dimensions', sa.String(length=255), nullable=False),
        sa.Column('image', LONGBLOB(), nullable=False),
        sa.PrimaryKeyConstraint('id', name='pk_tbl_books'),
    )
    op.create_table(
        'tbl_currencies',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
        sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
        sa.Column('deleted_at', sa.TIMESTAMP(), nullable=True),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('code', sa.String(length=3), nullable=False),
        sa.Column('num', sa.String(length=3), nullable=False),
        sa.Column('decimals', sa.Integer(), nullable=True),
        sa.CheckConstraint(
            'decimals >= 0', name='chk_tbl_currencies_decimals'
        ),
        sa.PrimaryKeyConstraint('id', name='pk_tbl_currencies'),
    )
    op.create_table(
        'tbl_roles',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
        sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
        sa.Column('deleted_at', sa.TIMESTAMP(), nullable=True),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('label', sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint('id', name='pk_tbl_roles'),
    )
    op.create_table(
        'tbl_countries',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
        sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
        sa.Column('deleted_at', sa.TIMESTAMP(), nullable=True),
        sa.Column('country_id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('alpha_2_code', sa.String(length=2), nullable=False),
        sa.Column('alpha_3_code', sa.String(length=3), nullable=False),
        sa.Column('numeric_code', sa.String(length=3), nullable=False),
        sa.ForeignKeyConstraint(
            ['country_id'],
            ['tbl_currencies.id'],
            name='fk_tbl_countries_tbl_currencies',
        ),
        sa.PrimaryKeyConstraint('id', name='pk_tbl_countries'),
    )
    op.create_table(
        'tbl_book_prices',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
        sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
        sa.Column('deleted_at', sa.TIMESTAMP(), nullable=True),
        sa.Column('book_id', sa.Integer(), nullable=False),
        sa.Column('country_id', sa.Integer(), nullable=False),
        sa.Column('vat', sa.Float(), nullable=False),
        sa.ForeignKeyConstraint(
            ['book_id'], ['tbl_books.id'], name='fk_tbl_book_prices_tbl_books'
        ),
        sa.ForeignKeyConstraint(
            ['country_id'],
            ['tbl_countries.id'],
            name='fk_tbl_book_prices_tbl_countries',
        ),
        sa.PrimaryKeyConstraint('id', name='pk_tbl_book_prices'),
    )
    op.create_table(
        'tbl_book_stocks',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
        sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
        sa.Column('deleted_at', sa.TIMESTAMP(), nullable=True),
        sa.Column('country_id', sa.Integer(), nullable=False),
        sa.Column('book_id', sa.Integer(), nullable=False),
        sa.Column('quantity', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ['book_id'], ['tbl_books.id'], name='fk_tbl_book_stocks_tbl_books'
        ),
        sa.ForeignKeyConstraint(
            ['country_id'],
            ['tbl_countries.id'],
            name='fk_tbl_book_stocks_tbl_countries',
        ),
        sa.PrimaryKeyConstraint('id', name='pk_tbl_book_stocks'),
    )
    op.create_table(
        'tbl_users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
        sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
        sa.Column('deleted_at', sa.TIMESTAMP(), nullable=True),
        sa.Column('created_id', sa.Integer(), nullable=True),
        sa.Column('country_id', sa.Integer(), nullable=True),
        sa.Column('fs_uniquifier', sa.String(length=255), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('last_name', sa.String(length=255), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=False),
        sa.Column('password', sa.String(length=255), nullable=False),
        sa.Column('genre', sa.Enum('m', 'f', name='genre'), nullable=False),
        sa.Column('birth_date', sa.Date(), nullable=False),
        sa.Column('active', sa.Boolean(), server_default='1', nullable=False),
        sa.ForeignKeyConstraint(
            ['country_id'],
            ['tbl_countries.id'],
            name='fk_tbl_users_tbl_countries',
        ),
        sa.ForeignKeyConstraint(
            ['created_id'], ['tbl_users.id'], name='fk_tbl_users_tbl_users'
        ),
        sa.PrimaryKeyConstraint('id', name='pk_tbl_users'),
        sa.UniqueConstraint('email', name='uq_tbl_users_email'),
        sa.UniqueConstraint(
            'fs_uniquifier', name='uq_tbl_users_fs_uniquifier'
        ),
    )
    op.create_table(
        'tbl_shopping_carts',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
        sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
        sa.Column('deleted_at', sa.TIMESTAMP(), nullable=True),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ['user_id'],
            ['tbl_users.id'],
            name='fk_tbl_shopping_carts_tbl_users',
        ),
        sa.PrimaryKeyConstraint('id', name='pk_tbl_shopping_carts'),
    )
    op.create_table(
        'tbl_user_roles',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
        sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
        sa.Column('deleted_at', sa.TIMESTAMP(), nullable=True),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.Column('role_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ['role_id'], ['tbl_roles.id'], name='fk_tbl_user_roles_tbl_roles'
        ),
        sa.ForeignKeyConstraint(
            ['user_id'], ['tbl_users.id'], name='fk_tbl_user_roles_tbl_users'
        ),
        sa.PrimaryKeyConstraint('id', name='pk_tbl_user_roles'),
    )
    op.create_table(
        'tbl_bills',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
        sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
        sa.Column('deleted_at', sa.TIMESTAMP(), nullable=True),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('currency_id', sa.Integer(), nullable=False),
        sa.Column('shopping_cart_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ['currency_id'],
            ['tbl_currencies.id'],
            name='fk_tbl_bills_tbl_currencies',
        ),
        sa.ForeignKeyConstraint(
            ['shopping_cart_id'],
            ['tbl_shopping_carts.id'],
            name='fk_tbl_bills_tbl_shopping_carts',
        ),
        sa.ForeignKeyConstraint(
            ['user_id'], ['tbl_users.id'], name='fk_tbl_bills_tbl_users'
        ),
        sa.PrimaryKeyConstraint('id', name='pk_tbl_bills'),
    )
    op.create_table(
        'tbl_shopping_cart_books',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
        sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
        sa.Column('deleted_at', sa.TIMESTAMP(), nullable=True),
        sa.Column('shopping_cart_id', sa.Integer(), nullable=False),
        sa.Column('book_id', sa.Integer(), nullable=False),
        sa.Column('discount', sa.Float(), nullable=False),
        sa.ForeignKeyConstraint(
            ['book_id'],
            ['tbl_books.id'],
            name='fk_tbl_shopping_cart_books_tbl_books',
        ),
        sa.ForeignKeyConstraint(
            ['shopping_cart_id'],
            ['tbl_shopping_carts.id'],
            name='fk_tbl_shopping_cart_books_tbl_shopping_carts',
        ),
        sa.PrimaryKeyConstraint('id', name='pk_tbl_shopping_cart_books'),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tbl_shopping_cart_books')
    op.drop_table('tbl_bills')
    op.drop_table('tbl_user_roles')
    op.drop_table('tbl_shopping_carts')
    op.drop_table('tbl_users')
    op.drop_table('tbl_book_stocks')
    op.drop_table('tbl_book_prices')
    op.drop_table('tbl_countries')
    op.drop_table('tbl_roles')
    op.drop_table('tbl_currencies')
    op.drop_table('tbl_books')
    # ### end Alembic commands ###
