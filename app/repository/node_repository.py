from app.model.node import Node


class NodeRepository(object):
    model = Node

    def get_node_by_id(self, node_id):
        return self.model.query.filter_by(id=node_id).first()
