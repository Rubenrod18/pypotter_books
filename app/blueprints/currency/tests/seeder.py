from typing import Type

from .. import Currency
from .factories import BritishPoundCurrencySeedFactory
from .factories import CurrencyFactory
from .factories import DollarCurrencySeedFactory
from .factories import EuroCurrencySeedFactory
from app.decorators import seed_actions


class Seeder:
    name = 'CurrencySeeder'
    priority = 2

    @seed_actions
    def __init__(self):
        self.__create_currency(
            BritishPoundCurrencySeedFactory,
            **{'name': 'British Pound Sterling'}
        )
        self.__create_currency(
            DollarCurrencySeedFactory, **{'name': 'US Dollar'}
        )
        self.__create_currency(EuroCurrencySeedFactory, **{'name': 'Euro'})

    @staticmethod
    def __create_currency(
        currency_factory: Type[CurrencyFactory], **kwargs
    ) -> None:
        if Currency.query.filter_by(**kwargs).first() is None:
            currency_factory.create()
