from contracts.business_service.graph_business_service_base import GraphBusinessServiceBase
from models.graph_model import GraphModel


class GraphBusinessServiceMock(GraphBusinessServiceBase):
    def __init__(self):
        self.graph_model_id = 1

    def insert_graph(self, graph_model: GraphModel) -> GraphModel:
        graph_model.graph_id = self.graph_model_id
        return graph_model

    def get_graph_model(self, graph_id: int) -> GraphModel:
        graph_model = GraphModel()
        graph_model.graph_id = self.graph_model_id
        return graph_model

    def update_graph(self, graph_model: GraphModel) -> GraphModel:
        pass

    def delete_graph(self, graph_id: int):
        pass
