from .factory import BritishPoundCurrencyFactory
from .factory import DollarCurrencyFactory
from .factory import EuroCurrencyFactory
from app.decorators import seed_actions


class Seeder:
    name = 'CurrencySeeder'

    @seed_actions
    def __init__(self):
        BritishPoundCurrencyFactory.create()
        DollarCurrencyFactory.create()
        EuroCurrencyFactory.create()
