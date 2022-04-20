from app.model.node import Node
from sqlalchemy import desc
from app import db


class NodeRepository(object):
    model = Node

    def get_node_by_id(self, node_id):
        return self.model.query.filter_by(id=node_id).first()

    def search_detail(self, keyword):
        # return self.model.query.filter(self.model.detail.match(keyword)).all()
        # return select(self.model, self.model.detail.match(keyword).label("score")).where(
        #     self.model.detail.match(keyword)).order_by("score")
        return db.session.query(self.model, self.model.detail.match(keyword).label("score")).filter(
            self.model.detail.match(keyword)).order_by(desc("score")).all()
