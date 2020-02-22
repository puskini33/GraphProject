from models.node_model import NodeModel


class NodeMapHelper(object):
    @staticmethod
    def db_entity_to_node_model(db_entity: list) -> NodeModel:
        node_model = NodeModel()
        node_model.node_id = db_entity[0][0]
        node_model.node_name = db_entity[0][1]
        node_model.graph_id = db_entity[0][2]
        return node_model

    @staticmethod
    def db_entities_to_node_models(db_entity: list) -> list:
        list_node_models = []
        for node_values in db_entity:
            node_model = NodeModel()
            node_model.node_id = node_values[0]
            node_model.node_name = node_values[1]
            node_model.graph_id = node_values[2]
            list_node_models.append(node_model)
        return list_node_models
