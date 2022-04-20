from flask_restful import Api, Resource
from flask import Blueprint
from app.service.node import NodeService
from .dto.node import NodeDetail

node_bp = Blueprint('node', __name__, url_prefix="/nodes")
node_api = Api(node_bp)


class NodeAPI(Resource):

    def get(self, node_id):
        node = NodeService().get_node_by_id(node_id)
        print(node)
        print(node.children)
        for i in node.children:
            print(i.parent)
            print(i.children)
        return NodeDetail().dump(node)


node_api.add_resource(
    NodeAPI, '/<int:node_id>', endpoint='get-node-by-id'
)
