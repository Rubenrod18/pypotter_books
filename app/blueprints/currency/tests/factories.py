from random import randint

import factory

from ..models import Currency
from app.blueprints.base import BaseFactory
from app.blueprints.base import BaseSeedFactory


class CurrencyFactory(BaseFactory):
    class Meta:
        model = Currency

    code = factory.Faker('currency_code')
    decimals = 2
    name = factory.Faker('currency_name')
    symbol = factory.Faker('currency_symbol')
    symbol_native = '$'

    @factory.lazy_attribute
    def name_plural(self):
        return self.name

    @factory.lazy_attribute
    def num(self):
        rand_num = randint(1, 999)
        return f'{rand_num:03d}'

    @factory.lazy_attribute
    def symbol_native(self):
        return self.symbol


class CurrencySeedFactory(BaseSeedFactory):
    class Meta:
        model = Currency

    code = factory.Faker('currency_code')
    decimals = 2
    name = factory.Faker('currency_name')
    symbol = factory.Faker('currency_symbol')
    symbol_native = '$'

    @factory.lazy_attribute
    def name_plural(self):
        return self.name

    @factory.lazy_attribute
    def num(self):
        rand_num = randint(1, 999)
        return f'{rand_num:03d}'

    @factory.lazy_attribute
    def symbol_native(self):
        return self.symbol


class BritishPoundCurrencySeedFactory(CurrencySeedFactory):
    code = 'GBP'
    decimals = 2
    name = 'British Pound Sterling'
    name_plural = 'British pounds sterling'
    num = '826'
    symbol = '£'
    symbol_native = '£'


class DollarCurrencySeedFactory(CurrencySeedFactory):
    code = 'USD'
    decimals = 2
    name = 'US Dollar'
    name_plural = 'US dollars'
    num = '840'
    symbol = '$'
    symbol_native = '$'


class EuroCurrencySeedFactory(CurrencySeedFactory):
    code = 'EUR'
    decimals = 2
    name = 'Euro'
    name_plural = 'euros'
    num = '978'
    symbol = '€'
    symbol_native = '€'
