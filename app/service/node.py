from app.model import Node
from app.repository.node_repository import NodeRepository


class NodeService(object):
    model = Node

    def get_node_by_id(self, node_id):
        node = NodeRepository().get_node_by_id(node_id)
        return node

    def search_node(self, key):
        return NodeRepository().search_detail(key)
