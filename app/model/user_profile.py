from .base import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class UserProfile(Base):
    __tablename__ = 'user_profile'
    user_id = sa.Column(sa.Integer, sa.ForeignKey('user.id'), nullable=False)
    age = sa.Column(sa.Integer, nullable=False)
    id_number = sa.Column(sa.String(20), nullable=True)

    user = relationship('User', back_populates='profile')

    def __repr__(self):
        return '<UserProfile %d>' % self.user_id

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
