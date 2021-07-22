from app.blueprints.book import Book
from app.blueprints.book_price.tests.factory import BookPriceFactory
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
        total_countries_without_relations_with_book_prices = 15
        total_books = Book.query.count()
        total_countries = Country.query.count()
        total_book_prices = (
            total_books * total_countries
            - total_countries_without_relations_with_book_prices
        )

        BookPriceFactory.create_batch(total_book_prices)
