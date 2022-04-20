from app import ma
from marshmallow import fields


class Node(ma.Schema):
    id = fields.Integer()
    name = fields.String()


class NodeDetail(ma.Schema):
    id = fields.Integer()
    name = fields.String()
    children = fields.List(fields.Nested(Node))
