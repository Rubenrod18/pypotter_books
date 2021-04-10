from datetime import datetime

from marshmallow import fields


class TimestampField(fields.Field):
    """Field that serializes to timestamp integer and deserializes to a
    datetime.datetime class."""

    def _serialize(self, value, attr, obj, **kwargs):
        if not isinstance(value, datetime):
            return None
        return datetime.fromtimestamp(value.timestamp()).strftime(
            '%Y-%m-%d %H:%M:%S'
        )

    def _deserialize(self, value, attr, data, **kwargs):
        return datetime.timestamp(value)
