import factory
from sqlalchemy import func

from app.blueprints.base import BaseFactory
from app.blueprints.base import BaseSeedFactory
from app.blueprints.country import Country
from app.blueprints.currency import Currency
from app.blueprints.currency.tests.factories import (
    BritishPoundCurrencySeedFactory,
)
from app.blueprints.currency.tests.factories import CurrencyFactory
from app.blueprints.currency.tests.factories import DollarCurrencySeedFactory
from app.blueprints.currency.tests.factories import EuroCurrencySeedFactory


class CountryFactory(BaseFactory):
    class Meta:
        model = Country

    name = factory.Faker('country')
    alpha_2_code = factory.Faker('country_code', representation='alpha-2')
    alpha_3_code = factory.Faker('country_code', representation='alpha-3')

    @factory.lazy_attribute
    def currency_id(self):
        currency = CurrencyFactory()
        return currency.id


class CountrySeedFactory(BaseSeedFactory):
    class Meta:
        model = Country

    name = factory.Faker('country')
    alpha_2_code = factory.Faker('country_code', representation='alpha-2')
    alpha_3_code = factory.Faker('country_code', representation='alpha-3')

    @factory.lazy_attribute
    def currency(self):
        return (
            Currency.query.filter_by(deleted_at=None)
            .order_by(func.rand())
            .first()
        )

    @factory.lazy_attribute
    def currency_id(self):
        return self.currency.id


class UnitedStatesCountrySeedFactory(CountrySeedFactory):
    currency = factory.RelatedFactory(DollarCurrencySeedFactory)
    name = 'United States of America'
    alpha_2_code = 'US'
    alpha_3_code = 'USA'

    @factory.lazy_attribute
    def currency(self):
        return (
            Currency.query.filter_by(name='US Dollar', deleted_at=None)
            .order_by(func.rand())
            .first()
        )


class SpainCountrySeedFactory(CountrySeedFactory):
    currency = factory.RelatedFactory(EuroCurrencySeedFactory)
    name = 'Spain'
    alpha_2_code = 'ES'
    alpha_3_code = 'ESP'

    @factory.lazy_attribute
    def currency(self):
        return (
            Currency.query.filter_by(name='Euro', deleted_at=None)
            .order_by(func.rand())
            .first()
        )


class UnitedKingdomsCountrySeedFactory(CountrySeedFactory):
    currency = factory.RelatedFactory(BritishPoundCurrencySeedFactory)
    name = 'United Kingdom of Great Britain and Northern Ireland'
    alpha_2_code = 'GB'
    alpha_3_code = 'GBR'

    @factory.lazy_attribute
    def currency(self):
        return (
            Currency.query.filter_by(
                name='British Pound Sterling', deleted_at=None
            )
            .order_by(func.rand())
            .first()
        )
