from models.node_model import NodeModel
from contracts.business_service.node_business_service_base import NodeBusinessServiceBase
from typing import List


class NodeBusinessServiceMock(NodeBusinessServiceBase):
    def __init__(self):
        self.node_id = 1

    def insert_node(self, node_model: NodeModel) -> NodeModel:
        node_model.node_id = self.node_id
        return node_model

    def get_node_model(self, node_id: int) -> NodeModel:
        pass

    def get_node_models(self, graph_id: int) -> List[NodeModel]:
        node_model = NodeModel()
        node_model.node_id = self.node_id
        node_model.graph_id = graph_id
        return [node_model]

    def update_node(self, node_model: NodeModel) -> NodeModel:
        pass

    def delete_node(self, node_id: int):
        pass
