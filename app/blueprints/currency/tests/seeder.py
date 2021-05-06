from typing import Type

from .. import Currency
from .factory import BritishPoundCurrencyFactory
from .factory import CurrencyFactory
from .factory import DollarCurrencyFactory
from .factory import EuroCurrencyFactory
from app.decorators import seed_actions


class Seeder:
    name = 'CurrencySeeder'

    @seed_actions
    def __init__(self):
        self.__create_currency(
            BritishPoundCurrencyFactory, **{'name': 'British Pound Sterling'}
        )
        self.__create_currency(DollarCurrencyFactory, **{'name': 'US Dollar'})
        self.__create_currency(EuroCurrencyFactory, **{'name': 'Euro'})

    @staticmethod
    def __create_currency(
        currency_factory: Type[CurrencyFactory], **kwargs
    ) -> None:
        if Currency.query.filter_by(**kwargs).first() is None:
            currency_factory.create()
