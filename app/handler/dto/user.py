from app import ma
from .common import UnixMillis
from marshmallow import fields, validate, post_load


class CreateUserReqeust(ma.Schema):
    username = fields.String()
    email = fields.Email()
    age = fields.Integer(validate=validate.Range(min=0, max=200))

    @post_load
    def make_user(self, data, **kwargs):
        e = CreateUserReqeust()
        e.username = data['username']
        e.email = data['email']
        e.age = data['age']
        return e


class CreateResponse(ma.Schema):
    id = fields.Integer()


class UserProfile(ma.Schema):
    age = fields.Integer()


class UserDetail(ma.Schema):
    id = fields.Integer()
    username = fields.String()
    email = fields.Email()
    created_at = UnixMillis()
    profile = fields.Nested(UserProfile)
