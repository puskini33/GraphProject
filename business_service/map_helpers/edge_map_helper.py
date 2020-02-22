from models.edge_model import EdgeModel


class EdgeMapHelper(object):
    @staticmethod
    def db_entity_to_edge_model(db_entity: list) -> EdgeModel:
        edge_model = EdgeModel()
        edge_model.edge_id = db_entity[0][0]
        edge_model.edge_name = db_entity[0][1]
        edge_model.edge_cost = db_entity[0][2]
        edge_model.start_node_id = db_entity[0][3]
        edge_model.end_node_id = db_entity[0][4]
        edge_model.graph_id = db_entity[0][5]
        return edge_model

    @staticmethod
    def db_entities_to_node_models(db_entity: list) -> list:
        list_edge_models = []
        for edge_values in db_entity:
            edge_model = EdgeModel()
            edge_model.edge_id = edge_values[0]
            edge_model.edge_name = edge_values[1]
            edge_model.edge_cost = edge_values[2]
            edge_model.start_node_id = edge_values[3]
            edge_model.end_node_id = edge_values[4]
            edge_model.graph_id = edge_values[5]
            list_edge_models.append(edge_model)
        return list_edge_models
