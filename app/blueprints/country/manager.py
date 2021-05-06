from .models import Country
from app.blueprints.base import BaseManager


class CountryManager(BaseManager):
    def __init__(self):
        super(CountryManager, self).__init__()
        self.model = Country
