from models.edge_model import EdgeModel
from typing import List, Tuple


class EdgeMapHelper(object):
    @staticmethod
    def db_entity_to_edge_model(db_entity: tuple) -> EdgeModel:
        edge_model = EdgeModel()
        edge_model.edge_id = db_entity[0]
        edge_model.edge_name = db_entity[1]
        edge_model.edge_cost = db_entity[2]
        edge_model.start_node_id = db_entity[3]
        edge_model.end_node_id = db_entity[4]
        edge_model.graph_id = db_entity[5]
        return edge_model

    @staticmethod
    def db_entities_to_edge_models(db_entity: List[Tuple]) -> list:
        list_edge_models = []
        for edge_values in db_entity:
            edge_model = EdgeMapHelper.db_entity_to_edge_model(edge_values)
            list_edge_models.append(edge_model)
        return list_edge_models
