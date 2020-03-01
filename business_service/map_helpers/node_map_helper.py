from models.node_model import NodeModel
from typing import List


class NodeMapHelper(object):
    @staticmethod
    def db_entity_to_node_model(db_entity: list) -> NodeModel:
        node_model = NodeModel()
        node_model.node_id = db_entity[0]
        node_model.node_name = db_entity[1]
        node_model.x_coord = db_entity[2]
        node_model.y_coord = db_entity[3]
        node_model.graph_id = db_entity[4]
        return node_model

    @staticmethod
    def db_entities_to_node_models(db_entities: List[List]) -> List[NodeModel]:
        list_node_models: List[NodeModel] = []
        for list_of_node_values in db_entities:
            node_model: NodeModel = NodeMapHelper.db_entity_to_node_model(list_of_node_values)
            list_node_models.append(node_model)
        return list_node_models
