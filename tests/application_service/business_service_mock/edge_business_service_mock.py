from contracts.business_service.edge_business_service_base import EdgeBusinessServiceBase
from models.edge_model import EdgeModel


class EdgeBusinessServiceMock(EdgeBusinessServiceBase):

    def insert_edge(self, edge_model: EdgeModel) -> EdgeModel:
        pass

    def get_edge_model(self, edge_id: int) -> EdgeModel:
        pass

    def get_edge_models(self, node_id: int) -> list:
        pass

    def update_edge(self, edge_model: EdgeModel) -> EdgeModel:
        pass

    def delete_edge(self, edge_id: int):
        pass
