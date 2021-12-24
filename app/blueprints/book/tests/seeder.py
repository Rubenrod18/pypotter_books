from typing import Type

from app.blueprints.book import Book
from app.blueprints.book.tests.factories import BookSeedFactory
from app.blueprints.book.tests.factories import (
    HarryPotterPartFiveBookSeedFactory,
)
from app.blueprints.book.tests.factories import (
    HarryPotterPartFourBookSeedFactory,
)
from app.blueprints.book.tests.factories import (
    HarryPotterPartOneBookSeedFactory,
)
from app.blueprints.book.tests.factories import (
    HarryPotterPartThreeBookSeedFactory,
)
from app.blueprints.book.tests.factories import (
    HarryPotterPartTwoBookSeedFactory,
)
from app.decorators import seed_actions


class Seeder:
    name = 'BookSeeder'
    priority = 4

    @seed_actions
    def __init__(self):
        self.__create_books()

    @staticmethod
    def __create_book(book_factory: Type[BookSeedFactory], **kwargs) -> None:
        if Book.query.filter_by(**kwargs).first() is None:
            book_factory.create()

    def __create_books(self) -> None:
        self.__create_book(
            HarryPotterPartOneBookSeedFactory,
            **{'isbn': HarryPotterPartOneBookSeedFactory.isbn}
        )
        self.__create_book(
            HarryPotterPartTwoBookSeedFactory,
            **{'isbn': HarryPotterPartTwoBookSeedFactory.isbn}
        )
        self.__create_book(
            HarryPotterPartThreeBookSeedFactory,
            **{'isbn': HarryPotterPartThreeBookSeedFactory.isbn}
        )
        self.__create_book(
            HarryPotterPartFourBookSeedFactory,
            **{'isbn': HarryPotterPartFourBookSeedFactory.isbn}
        )
        self.__create_book(
            HarryPotterPartFiveBookSeedFactory,
            **{'isbn': HarryPotterPartFiveBookSeedFactory.isbn}
        )
