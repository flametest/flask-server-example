from app import ma
from marshmallow import fields


class GroupDetail(ma.Schema):
    id = fields.Integer()
    name = fields.String()


class GroupList(ma.Schema):
    groups = fields.List(fields.Nested(GroupDetail))
