from models.graph_model import GraphModel


class GraphMapHelper(object):
    @staticmethod
    def db_entity_to_graph_model(db_entity: list):
        graph_model = GraphModel()  # create the GraphModel object
        graph_model.graph_id = db_entity[0][0]  # set the id of the GraphModel Object
        graph_model.graph_name = db_entity[0][1]  # set the name of the GraphModel Object
        return graph_model

    @staticmethod
    def graph_model_to_db_entity(graph_id, graph_name):
        graph_model = GraphModel()
        graph_model.graph_id = graph_id
        graph_model.graph_name = graph_name
        return graph_model

