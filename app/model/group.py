from .base import Base
from .user_group import UserGroup
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Group(Base):
    __tablename__ = 'group'
    name = sa.Column(sa.String(32), nullable=False)

    users = relationship('User', secondary=UserGroup.__tablename__, backref='Group')

    def __repr__(self):
        return '<Group %r>' % self.name

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
