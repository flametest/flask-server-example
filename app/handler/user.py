from flask_restful import Api, Resource, fields, marshal_with
from flask import Blueprint, request
from app.service.user import UserService
from .dto.user import UserDetail, CreateResponse, CreateUserReqeust
from .dto.group import GroupList

user_bp = Blueprint('user', __name__, url_prefix="/users")
user_api = Api(user_bp)


class UserAPI(Resource):

    def get(self, user_id):
        user = UserService().get_user_by_id(user_id)
        return UserDetail().dump(user)

    def post(self):
        req = CreateUserReqeust().load(request.json)
        user = UserService().create_user(req.username, req.email, req.age)
        return CreateResponse().dump(user)


class UserGroupAPI(Resource):

    def get(self, user_id):
        user = UserService().get_user_by_id(user_id)
        print(user.groups)
        return GroupList().dump(user)


user_api.add_resource(
    UserAPI, '', endpoint='user-create'
)
user_api.add_resource(
    UserAPI, '/<int:user_id>', endpoint='get-user-by-id'
)
user_api.add_resource(
    UserGroupAPI, '/<int:user_id>/groups', endpoint='get-user-groups'
)
