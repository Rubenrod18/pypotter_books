from flask_restx import fields

from app.blueprints.base import record_monitoring_sw_model
from app.blueprints.book_price.swagger import book_price_sw_model
from app.blueprints.book_stock.swagger import book_stock_sw_model
from app.extensions import api


book_sw_model = api.clone(
    'Book',
    record_monitoring_sw_model,
    {
        'title': fields.String(required=True),
        'author': fields.String(required=True),
        'description': fields.String(required=True),
        'isbn': fields.String(required=True),
        'total_pages': fields.Integer(required=True),
        'publisher': fields.String(required=True),
        'published_date': fields.String(required=True),
        'language': fields.String(required=True),
        'dimensions': fields.String(required=True),
        'book_stocks': fields.List(fields.Nested(book_stock_sw_model)),
        'book_prices': fields.List(fields.Nested(book_price_sw_model)),
    },
)

book_search_output_sw_model = api.model(
    'BookSearchOutput',
    {
        'records_total': fields.Integer,
        'records_filtered': fields.Integer,
        'data': fields.List(fields.Nested(book_sw_model)),
    },
)
