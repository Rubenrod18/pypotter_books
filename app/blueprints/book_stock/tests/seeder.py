from app.blueprints.book import Book
from app.blueprints.book_stock.tests.factory import BookStockFactory
from app.blueprints.country import Country
from app.decorators import seed_actions


class Seeder:
    name = 'BookStockSeeder'
    priority = 6

    @seed_actions
    def __init__(self):
        self.__create_book_stocks()

    @staticmethod
    def __create_book_stocks():
        total_books = Book.query.count()
        total_countries = Country.query.count()

        if total_countries > total_books:
            total_diff_relations = (total_countries - total_books) * 5
        else:
            total_diff_relations = (total_books - total_countries) * 5

        total_book_stocks = (
            total_books * total_countries - total_diff_relations
        )

        BookStockFactory.create_batch(total_book_stocks)
