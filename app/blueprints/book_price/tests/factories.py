import factory
from sqlalchemy import func

from app.blueprints.base.tests.base_factory import BaseFactory
from app.blueprints.base.tests.base_factory import BaseSeedFactory
from app.blueprints.book import Book
from app.blueprints.book import BookPrice
from app.blueprints.book.tests.factories import BookFactory
from app.blueprints.country import Country
from app.blueprints.country.tests.factories import CountryFactory


class BookPriceFactory(BaseFactory):
    class Meta:
        model = BookPrice

    price = 8.00

    @factory.lazy_attribute
    def country_id(self):
        country = CountryFactory(deleted_at=None)
        return country.id

    @factory.lazy_attribute
    def book_id(self):
        book = BookFactory(deleted_at=None)
        return book.id


class BookPriceSeedFactory(BaseSeedFactory):
    class Meta:
        model = BookPrice

    price = 8.00

    @factory.lazy_attribute
    def country_id(self):
        total_books = Book.query.count()

        country = (
            Country.query.with_entities(Country.id)
            .outerjoin(BookPrice)
            .filter_by(deleted_at=None)
            .group_by(Country.id)
            .having(func.count(Country.id) < total_books)
            .order_by(func.random())
            .first()
        )

        return country.id

    @factory.lazy_attribute
    def book_id(self):
        subquery = (
            Book.query.with_entities(Book.id)
            .outerjoin(BookPrice)
            .filter(BookPrice.country_id == self.country_id)
        )

        if subquery.count():
            book = (
                Book.query.outerjoin(BookPrice)
                .outerjoin(Country)
                .filter(Book.deleted_at.is_(None), ~Book.id.in_(subquery))
                .first()
            )
        else:
            book = (
                Book.query.with_entities(Book.id)
                .order_by(func.random())
                .first()
            )

        return book.id
