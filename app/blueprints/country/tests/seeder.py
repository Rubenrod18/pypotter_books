from typing import Type

from app.blueprints.country import Country
from app.blueprints.country.tests.factories import CountrySeedFactory
from app.blueprints.country.tests.factories import SpainCountrySeedFactory
from app.blueprints.country.tests.factories import (
    UnitedKingdomsCountrySeedFactory,
)
from app.blueprints.country.tests.factories import (
    UnitedStatesCountrySeedFactory,
)
from app.decorators import seed_actions


class Seeder:
    name = 'CountrySeeder'
    priority = 3

    @seed_actions
    def __init__(self, rows: int = 10):
        self.__create_country(
            UnitedStatesCountrySeedFactory,
            **{'name': 'United States of America'}
        )
        self.__create_country(SpainCountrySeedFactory, **{'name': 'Spain'})
        self.__create_country(
            UnitedKingdomsCountrySeedFactory,
            **{'name': 'United Kingdom of Great Britain and Northern Ireland'}
        )
        CountrySeedFactory.create_batch(rows)

    @staticmethod
    def __create_country(
        country_factory: Type[CountrySeedFactory], **kwargs
    ) -> None:
        if Country.query.filter_by(**kwargs).first() is None:
            country_factory.create()
