from database_api.node_repository import NodeRepository
from business_service.map_helpers.node_map_helper import NodeMapHelper
from models.node_model import NodeModel


class NodeBusinessService(object):

    def __init__(self, in_node_repository: NodeRepository):
        self.node_repository = in_node_repository

    def insert_node(self, node_model: NodeModel) -> NodeModel:
        node_id = self.node_repository.insert_node(node_model.node_name, node_model.graph_id)
        node_model.node_id = node_id
        return node_model

    def get_node_model(self, node_id: int) -> NodeModel:
        list_values_node = self.node_repository.get_node(node_id)
        return NodeMapHelper.db_entity_to_node_model(list_values_node)

    def get_node_models(self, graph_id: int) -> list:
        list_values_nodes = self.node_repository.get_graph_nodes(graph_id)
        return NodeMapHelper.db_entities_to_node_models(list_values_nodes)

    def update_node(self, node_model: NodeModel) -> NodeModel:
        self.node_repository.update_node(node_model.node_id, node_model.node_name, node_model.graph_id)
        return node_model

    def delete_node(self, node_id: int):
        self.node_repository.delete_node(node_id)
