import math

from sqlalchemy import func

from app.blueprints.book import Book
from app.blueprints.book import BookPrice
from app.blueprints.book_price.tests.factories import BookPriceSeedFactory
from app.blueprints.country import Country
from app.decorators import seed_actions


class Seeder:
    name = 'BookPriceSeeder'
    priority = 5

    @seed_actions
    def __init__(self):
        self.__create_book_prices()

    @staticmethod
    def __create_book_prices():
        total_books = Book.query.count()
        total_countries = (
            Country.query.with_entities(Country.id)
            .outerjoin(BookPrice)
            .filter_by(deleted_at=None)
            .group_by(Country.id)
            .having(func.count(Country.id) < total_books)
            .count()
        )
        total_book_prices = math.ceil(total_books * total_countries / 3)
        BookPriceSeedFactory.create_batch(total_book_prices)
