from typing import Type

from app.blueprints.book import Book
from app.blueprints.book.tests.factory import BookFactory
from app.blueprints.book.tests.factory import HarryPotterPartFiveBookFactory
from app.blueprints.book.tests.factory import HarryPotterPartFourBookFactory
from app.blueprints.book.tests.factory import HarryPotterPartOneBookFactory
from app.blueprints.book.tests.factory import HarryPotterPartThreeBookFactory
from app.blueprints.book.tests.factory import HarryPotterPartTwoBookFactory
from app.decorators import seed_actions


class Seeder:
    name = 'BookSeeder'

    @seed_actions
    def __init__(self):
        self.__create_book(
            HarryPotterPartOneBookFactory,
            **{'isbn': HarryPotterPartOneBookFactory.isbn}
        )
        self.__create_book(
            HarryPotterPartTwoBookFactory,
            **{'isbn': HarryPotterPartTwoBookFactory.isbn}
        )
        self.__create_book(
            HarryPotterPartThreeBookFactory,
            **{'isbn': HarryPotterPartThreeBookFactory.isbn}
        )
        self.__create_book(
            HarryPotterPartFourBookFactory,
            **{'isbn': HarryPotterPartFourBookFactory.isbn}
        )
        self.__create_book(
            HarryPotterPartFiveBookFactory,
            **{'isbn': HarryPotterPartFiveBookFactory.isbn}
        )

    @staticmethod
    def __create_book(book_factory: Type[BookFactory], **kwargs) -> None:
        if Book.query.filter_by(**kwargs).first() is None:
            book_factory.create()
