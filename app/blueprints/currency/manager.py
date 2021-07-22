from .models import Currency
from app.blueprints.base import BaseManager


class CurrencyManager(BaseManager):
    def __init__(self):
        super(CurrencyManager, self).__init__()
        self.model = Currency
