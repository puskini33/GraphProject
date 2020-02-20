from database_api.graph_repository import GraphRepository
from business_service.map_helpers.graph_map_helper import GraphMapHelper


class GraphBusinessService(object):

    def __init__(self, in_graph_repository: GraphRepository):
        self.graph_repository = in_graph_repository  # initialize graph_repository

    def insert_graph_model(self, graph_id, graph_name):
        self.graph_repository.insert_graph(graph_id)
        return GraphMapHelper.graph_model_to_db_entity(graph_id, graph_name)

    def get_graph_model(self, graph_id: str):
        list_values_graph = self.graph_repository.get_graph(graph_id)  # a list of graph_values is returned
        return GraphMapHelper.db_entity_to_graph_model(list_values_graph)  # create the new GraphModel object with the values

    def update_graph_model(self, graph_id, graph_name):
        self.graph_repository.update_graph(graph_id, graph_name)
        list_values_graph = self.graph_repository.get_graph(graph_id)
        return GraphMapHelper.db_entity_to_graph_model(list_values_graph)

    def delete_graph_model(self, graph_id):
        self.graph_repository.delete_graph(graph_id)
