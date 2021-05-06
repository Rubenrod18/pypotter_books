from typing import Type

from app.blueprints.country import Country
from app.blueprints.country.tests.factory import CountryFactory
from app.blueprints.country.tests.factory import SpainCountryFactory
from app.blueprints.country.tests.factory import UnitedKingdomsCountryFactory
from app.blueprints.country.tests.factory import UnitedStatesCountryFactory
from app.decorators import seed_actions


class Seeder:
    name = 'CountrySeeder'

    @seed_actions
    def __init__(self):
        self.__create_country(
            UnitedStatesCountryFactory, **{'name': 'United States of America'}
        )
        self.__create_country(SpainCountryFactory, **{'name': 'Spain'})
        self.__create_country(
            UnitedKingdomsCountryFactory,
            **{'name': 'United Kingdom of Great Britain and Northern Ireland'}
        )

    @staticmethod
    def __create_country(
        country_factory: Type[CountryFactory], **kwargs
    ) -> None:
        if Country.query.filter_by(**kwargs).first() is None:
            country_factory.create()
