from models.graph_model import GraphModel
from typing import List, Tuple


class GraphMapHelper(object):
    @staticmethod
    def db_entity_to_graph_model(db_entity: List[Tuple]) -> GraphModel:
        graph_model = GraphModel()
        graph_model.graph_id = db_entity[0][0]
        graph_model.graph_name = db_entity[0][1]
        return graph_model
