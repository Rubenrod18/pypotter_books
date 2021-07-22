from app.blueprints.bill.tests.factory import BillFactory
from app.decorators import seed_actions


class Seeder:
    name = 'BillSeeder'
    priority = 8

    @seed_actions
    def __init__(self):
        BillFactory.create_batch(5)
