from .base import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship, backref


class Node(Base):
    __tablename__ = 'node'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255), nullable=False)
    parent_id = sa.Column(sa.Integer, sa.ForeignKey("node.id"))

    children = relationship("Node", backref=backref('parent', remote_side=[id]))

    def __repr__(self):
        return '<Node %r>' % self.name

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
