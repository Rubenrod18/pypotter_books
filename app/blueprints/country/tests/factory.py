import factory
from sqlalchemy import func

from app.blueprints.base import BaseFactory
from app.blueprints.country import Country
from app.blueprints.currency import Currency
from app.blueprints.currency.tests.factory import BritishPoundCurrencyFactory
from app.blueprints.currency.tests.factory import DollarCurrencyFactory
from app.blueprints.currency.tests.factory import EuroCurrencyFactory


class CountryFactory(BaseFactory):
    class Meta:
        model = Country

    # Normal fields
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


class UnitedStatesCountryFactory(CountryFactory):
    currency = factory.RelatedFactory(DollarCurrencyFactory)
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


class SpainCountryFactory(CountryFactory):
    currency = factory.RelatedFactory(EuroCurrencyFactory)
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


class UnitedKingdomsCountryFactory(CountryFactory):
    currency = factory.RelatedFactory(BritishPoundCurrencyFactory)
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
