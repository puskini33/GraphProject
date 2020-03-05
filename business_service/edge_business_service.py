from repository_service.contracts.edge_repository_base import EdgeRepositoryBase
from business_service.map_helpers.edge_map_helper import EdgeMapHelper
from models.edge_model import EdgeModel


class EdgeBusinessService(object):

    def __init__(self, in_edge_repository: EdgeRepositoryBase):
        self.edge_repository = in_edge_repository

    def insert_edge(self, edge_model: EdgeModel) -> EdgeModel:
        edge_id = self.edge_repository.insert_edge(edge_model.edge_name, edge_model.edge_cost, edge_model.start_node_id,
                                                   edge_model.end_node_id, edge_model.graph_id)
        edge_model.edge_id = edge_id
        return edge_model

    def get_edge_model(self, edge_id: int) -> EdgeModel:
        list_values_edge = self.edge_repository.get_edge_values(edge_id)
        return EdgeMapHelper.db_entity_to_edge_model(list_values_edge[0])

    def get_edge_models(self, node_id: int) -> list:
        list_values_edges = self.edge_repository.get_node_edges(node_id)
        return EdgeMapHelper.db_entities_to_node_models(list_values_edges)

    def update_edge(self, edge_model: EdgeModel) -> EdgeModel:
        self.edge_repository.update_edge(edge_model.edge_id, edge_model.edge_name, edge_model.edge_cost,
                                         edge_model.start_node_id, edge_model.end_node_id, edge_model.graph_id)
        return edge_model

    def delete_edge(self, edge_id: int):
        self.edge_repository.delete_edge(edge_id)