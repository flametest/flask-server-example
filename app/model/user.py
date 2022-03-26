from .base import Base
from .user_group import UserGroup
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'user'
    username = sa.Column(sa.String(80), unique=True, nullable=False)
    email = sa.Column(sa.String(120), unique=True, nullable=False)

    profile = relationship('UserProfile', back_populates='user', uselist=False)
    groups = relationship('Group', secondary=UserGroup.__tablename__, backref='User')

    def __repr__(self):
        return '<User %r>' % self.username

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
