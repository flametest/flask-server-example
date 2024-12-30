from app.model import User, UserProfile
from app.repository.user_repository import UserRepository
from app import db


class UserService(object):
    model = User

    def create_user(self, username: str, email: str, age: int):
        user = UserRepository().create_user(username, email)
        user.profile = UserProfile(age=age)
        db.session.add(user)
        db.session.commit()
        return user

    def get_user_by_id(self, user_id: int):
        user = UserRepository().get_user_by_id(user_id)
        return user
