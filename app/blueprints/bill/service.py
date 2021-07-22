from app.blueprints.base import BaseService
from app.blueprints.bill.manager import BillManager
from app.blueprints.bill.serializers import bill_serializer
from app.extensions import db


class BillService(BaseService):
    def __init__(self):
        super(BillService, self).__init__()
        self.manager = BillManager()

    def create(self, **kwargs):
        serialized_data = bill_serializer.load(kwargs)
        bill = self.manager.create(**serialized_data)
        db.session.add(bill)
        db.session.flush()
        return bill
