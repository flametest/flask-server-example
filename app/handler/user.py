from flask_restful import Api, Resource, reqparse, fields, marshal_with
from flask import Blueprint
from app.service.user import UserService

user_bp = Blueprint('user', __name__, url_prefix="/users")
user_api = Api(user_bp)

create_fields = {
    'id': fields.Integer,
}
user_profile = {
    'age': fields.Integer,
}
user_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'email': fields.String,
    'created_at': fields.DateTime(dt_format='iso8601'),
    'profile': fields.Nested(user_profile)
}


class UserAPI(Resource):

    def __init__(self):
        self.post_parser = reqparse.RequestParser()
        self.post_parser.add_argument(
            'username', type=str, location='json', required=True,
        )
        self.post_parser.add_argument(
            'email', type=str, location='json', required=True,
        )
        self.post_parser.add_argument(
            'age', type=int, location='json', required=True,
        )

    @marshal_with(user_fields)
    def get(self, user_id):
        user = UserService().get_user_by_id(user_id)
        return user

    @marshal_with(create_fields)
    def post(self):
        args = self.post_parser.parse_args()
        user = UserService().create_user(args.username, args.email, args.age)
        return user


user_api.add_resource(
    UserAPI, '', endpoint='user-create'
)
user_api.add_resource(
    UserAPI, '/<int:user_id>', endpoint='get-user-by-id'
)
