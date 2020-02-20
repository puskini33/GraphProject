from database_api.graph_repository import GraphRepository
from models.graph_model import GraphModel


class GraphMapHelper(object):
    @staticmethod
    def db_entity_to_graph_model(db_entity: list):
        graph_model = GraphModel()  # create the GraphModel object
        graph_model.graph_id = db_entity[0][0]  # set the id of the GraphModel Object
        graph_model.graph_name = db_entity[0][1]  # set the name of the GraphModel Object
        return graph_model


class GraphBusinessService(object):

    def __init__(self, in_graph_repository: GraphRepository):
        self.graph_repository = in_graph_repository  # initialize graph_repository

    def get_graph_model(self, graph_id: str):
        list_values_graph = self.graph_repository.get_graph(graph_id)  # a list of graph_values is returned
        return GraphMapHelper.db_entity_to_graph_model(list_values_graph)  # create the new GraphModel object with the values
