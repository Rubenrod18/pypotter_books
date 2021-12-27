from app.blueprints.bill.tests.factories import BillSeedFactory
from app.decorators import seed_actions


class Seeder:
    name = 'BillSeeder'
    priority = 8

    @seed_actions
    def __init__(self):
        BillSeedFactory.create_batch(5)
