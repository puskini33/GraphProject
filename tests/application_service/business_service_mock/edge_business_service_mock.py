from contracts.business_service.edge_business_service_base import EdgeBusinessServiceBase
from models.edge_model import EdgeModel


class EdgeBusinessServiceMock(EdgeBusinessServiceBase):
    def __init__(self):
        self.edge_id = 1

    def insert_edge(self, edge_model: EdgeModel) -> EdgeModel:
        edge_model.edge_id = self.edge_id
        return edge_model

    def get_edge_model(self, edge_id: int) -> EdgeModel:
        edge_model = EdgeModel()
        edge_model.edge_id = edge_id
        return edge_model

    def get_edge_models_of_node(self, node_id: int) -> list:
        edge_model = EdgeModel()
        edge_model.edge_id = self.edge_id
        edge_model.start_node_id = node_id
        return [edge_model]

    def update_edge(self, edge_model: EdgeModel) -> EdgeModel:
        pass

    def delete_edge(self, edge_id: int):
        pass
