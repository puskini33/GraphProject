from abc import ABC, abstractmethod
from models.node_model import NodeModel
from typing import List


class NodeBusinessServiceBase(ABC):

    @abstractmethod
    def insert_node(self, node_model: NodeModel) -> NodeModel:
        pass

    @abstractmethod
    def get_node_model(self, node_id: int) -> NodeModel:
        pass

    @abstractmethod
    def get_node_models(self, graph_id: int) -> List[NodeModel]:
        pass

    @abstractmethod
    def update_node(self, node_model: NodeModel) -> NodeModel:
        pass

    @abstractmethod
    def delete_node(self, node_id: int):
        pass
