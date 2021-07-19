from app.blueprints.base import BaseManager
from app.blueprints.bill import Bill


class BillManager(BaseManager):
    def __init__(self):
        super(BillManager, self).__init__()
        self.model = Bill
