from app.blueprints.base import BaseService
from app.blueprints.currency.manager import CurrencyManager
from app.blueprints.currency.serializers import currency_serializer
from app.extensions import db


class CurrencyService(BaseService):
    def __init__(self):
        super(CurrencyService, self).__init__()
        self.manager = CurrencyManager()
        self.serializer = currency_serializer

    def create(self, **kwargs):
        serialized_data = self.serializer.load(kwargs)
        currency = self.manager.create(**serialized_data)
        db.session.add(currency)
        db.session.flush()
        return currency
