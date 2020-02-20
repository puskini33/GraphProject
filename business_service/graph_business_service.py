from database_api.graph_repository import GraphRepository
from business_service.map_helpers.graph_map_helper import GraphMapHelper
from models.graph_model import GraphModel


class GraphBusinessService(object):

    def __init__(self, in_graph_repository: GraphRepository):
        self.graph_repository = in_graph_repository

    def insert_graph_model(self, graph_model: GraphModel, graph_name: str) -> GraphModel:
        graph_id = self.graph_repository.insert_graph(graph_name)
        return GraphMapHelper.graph_model_db_entity(graph_model, graph_id, graph_name)

    def get_graph_model(self, graph_id: int) -> GraphModel:
        list_values_graph = self.graph_repository.get_graph(graph_id)
        return GraphMapHelper.db_entity_to_graph_model(list_values_graph)

    def update_graph_model(self, graph_model: GraphModel, graph_id: int, graph_name: str):
        self.graph_repository.update_graph(graph_id, graph_name)
        return GraphMapHelper.graph_model_db_entity(graph_model, graph_id, graph_name)

    def delete_graph_model(self, graph_model: GraphModel, graph_id: int):
        self.graph_repository.delete_graph(graph_id)
        del graph_model
