from app.models.user import User
from app import db


class UserService(object):
    model = User

    def create_user(self, username, email):
        user = User(
            username=username,
            email=email,
        )
        db.session.add(user)
        db.session.commit()
        return user

    def get_user_by_id(self, user_id):
        return self.model.query.filter_by(id=user_id).first()
