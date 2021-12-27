import logging

from marshmallow import fields
from marshmallow import validates
from werkzeug.exceptions import NotFound

from app.blueprints.base import TimestampField
from app.blueprints.country import Country
from app.blueprints.currency.manager import CurrencyManager
from app.blueprints.currency.serializers import CurrencySerializer
from app.extensions import ma

logger = logging.getLogger(__name__)
currency_manager = CurrencyManager()


class CountrySerializer(ma.SQLAlchemySchema):
    class Meta:
        model = Country
        ordered = True

    # Primary and foreign keys
    id = ma.auto_field()

    # Normal fields
    name = ma.auto_field()
    alpha_2_code = ma.auto_field()
    alpha_3_code = ma.auto_field()

    # Input fields
    currency_id = ma.auto_field(load_only=True)

    # Output fields
    currency = fields.Nested(lambda: CurrencySerializer(), dump_only=True)
    created_at = TimestampField(dump_only=True)
    updated_at = TimestampField(dump_only=True)
    deleted_at = TimestampField(dump_only=True)

    @validates('currency_id')
    def validate_currency_id(self, currency_id: int):
        kwargs = {'deleted_at': None}
        currency = currency_manager.find_by_id(currency_id, **kwargs)

        if currency is None:
            logger.debug(f'Currency "{currency_id}" not found')
            raise NotFound('Currency not found')

        if currency.deleted_at is not None:
            logger.debug(f'Currency "{currency_id}" deleted')
            raise NotFound('Currency not found')


country_serializer = CountrySerializer()
countries_serializer = CountrySerializer(many=True)
