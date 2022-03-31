import time
from marshmallow import fields


class UnixMillis(fields.Field):
    def _serialize(self, value, attr, obj):
        if value is None:
            return 0
        microseconds = time.mktime(value.timetuple()) * 1000 + value.microsecond
        return microseconds
