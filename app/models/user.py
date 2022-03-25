from .base import Base
from app import db


class User(Base):
    __tablename__ = 'user'
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
