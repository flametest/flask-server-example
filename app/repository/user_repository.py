from app.model.user import User


class UserRepository(object):
    model = User

    def create_user(self, username, email):
        user = User(
            username=username,
            email=email,
        )
        return user

    def get_user_by_id(self, user_id):
        return self.model.query.filter_by(id=user_id).first()
