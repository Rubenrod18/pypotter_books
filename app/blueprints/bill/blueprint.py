from flask import Blueprint

from app.blueprints.base import BaseResource
from app.blueprints.bill.serializers import bill_serializer
from app.blueprints.bill.serializers import bills_serializer
from app.blueprints.bill.service import BillService
from app.blueprints.bill.swagger import bill_search_output_sw_model
from app.blueprints.bill.swagger import bill_sw_model
from app.decorators import token_required
from app.extensions import api as root_api

blueprint = Blueprint('bills', __name__)
_api = root_api.namespace('bills', description='Bills endpoints.')


class _BillBaseResource(BaseResource):
    def __init__(self, *args, **kwargs):
        super(_BillBaseResource, self).__init__(*args, **kwargs)
        self._bill_service = BillService()


@_api.route('')
class NewBillResource(_BillBaseResource):
    @_api.doc(
        responses={
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    @_api.expect(bill_sw_model)
    @_api.marshal_with(bill_sw_model, envelope='data', code=201)
    @token_required
    def post(self) -> tuple:
        bill = self._bill_service.create(**self._request_payload())
        return bill_serializer.dump(bill), 201


@_api.route('/<int:bill_id>')
class BillResource(_BillBaseResource):
    @_api.doc(
        responses={
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    @_api.marshal_with(bill_sw_model, envelope='data')
    @token_required
    def get(self, bill_id: int) -> tuple:
        bill = self._bill_service.find_by_id(bill_id)
        return bill_serializer.dump(bill), 200

    @_api.doc(
        responses={
            400: 'Bad Request',
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    @_api.expect(bill_sw_model)
    @_api.marshal_with(bill_sw_model, envelope='data')
    @token_required
    def put(self, bill_id: int) -> tuple:
        bill = self._bill_service.save(bill_id, **self._request_payload())
        return bill_serializer.dump(bill), 200

    @_api.doc(
        responses={
            400: 'Bad Request',
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    @_api.marshal_with(bill_sw_model, envelope='data')
    @token_required
    def delete(self, bill_id: int) -> tuple:
        bill = self._bill_service.delete(bill_id)
        return bill_serializer.dump(bill), 200


@_api.route('/search')
class BillsSearchResource(_BillBaseResource):
    @_api.doc(
        responses={
            200: 'Success',
            401: 'Unauthorized',
            403: 'Forbidden',
            422: 'Unprocessable Entity',
        },
        security='auth_token',
    )
    @_api.marshal_with(bill_search_output_sw_model)
    @token_required
    def post(self) -> tuple:
        bill_data = self._bill_service.get(**self._request_payload())
        bill_data_lst = list(bill_data['query'].items)
        return {
            'data': bills_serializer.dump(bill_data_lst),
            'records_total': bill_data['records_total'],
            'records_filtered': bill_data['records_filtered'],
        }, 200
