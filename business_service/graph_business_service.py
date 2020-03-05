from repository_service.contracts.graph_repository_base import GraphRepositoryBase
from business_service.map_helpers.graph_map_helper import GraphMapHelper
from models.graph_model import GraphModel


class GraphBusinessService(object):

    def __init__(self, in_graph_repository_base: GraphRepositoryBase):
        self.graph_repository = in_graph_repository_base

    def insert_graph(self, graph_model: GraphModel) -> GraphModel:
        graph_id = self.graph_repository.insert_graph(graph_model.graph_name)
        graph_model.graph_id = graph_id
        return graph_model

    def get_graph_model(self, graph_id: int) -> GraphModel:
        list_values_graph = self.graph_repository.get_graph(graph_id)
        return GraphMapHelper.db_entity_to_graph_model(list_values_graph)

    def update_graph(self, graph_model: GraphModel) -> GraphModel:
        self.graph_repository.update_graph(graph_model.graph_id, graph_model.graph_name)
        return graph_model

    def delete_graph(self, graph_id: int):
        self.graph_repository.delete_graph(graph_id)
