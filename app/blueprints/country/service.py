from app.blueprints.base import BaseService
from app.blueprints.country.manager import CountryManager
from app.blueprints.country.serializers import country_serializer
from app.extensions import db


class CountryService(BaseService):
    def __init__(self):
        super(CountryService, self).__init__()
        self.manager = CountryManager()
        self.country_serializer = country_serializer

    def create(self, **kwargs):
        serialized_data = self.country_serializer.load(kwargs)
        country = self.manager.create(**serialized_data)
        db.session.add(country)
        db.session.commit()
        return country
