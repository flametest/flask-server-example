from .base import Base
import sqlalchemy as sa


class UserGroup(Base):
    __tablename__ = 'user_group'
    user_id = sa.Column(sa.Integer, sa.ForeignKey('user.id'))
    group_id = sa.Column(sa.Integer, sa.ForeignKey('group.id'))
