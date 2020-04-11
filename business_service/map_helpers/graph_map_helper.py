from models.graph_model import GraphModel
from typing import List, Tuple


class GraphMapHelper(object):
    @staticmethod
    def db_entity_to_graph_model(db_entity: tuple) -> GraphModel:
        graph_model = GraphModel()
        graph_model.graph_id = db_entity[0]
        graph_model.graph_name = db_entity[1]
        return graph_model

    @staticmethod
    def db_entities_to_graph_models(db_entities: List[Tuple]) -> List[GraphModel]:
        list_graph_models: List[GraphModel] = []
        for list_of_graph_values in db_entities:
            node_model: GraphModel = GraphMapHelper.db_entity_to_graph_model(list_of_graph_values)
            list_graph_models.append(node_model)
        return list_graph_models
