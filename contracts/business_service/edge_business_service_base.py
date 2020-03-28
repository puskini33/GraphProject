from models.edge_model import EdgeModel
from abc import ABC, abstractmethod


class EdgeBusinessServiceBase(ABC):

    @abstractmethod
    def insert_edge(self, edge_model: EdgeModel) -> EdgeModel:
        pass

    @abstractmethod
    def get_edge_model(self, edge_id: int) -> EdgeModel:
        pass

    @abstractmethod
    def get_edge_models_of_node(self, node_id: int) -> list:
        pass

    @abstractmethod
    def get_edge_models_of_graph(self, graph_id: int) -> list:
        pass

    @abstractmethod
    def update_edge(self, edge_model: EdgeModel) -> EdgeModel:
        pass

    @abstractmethod
    def delete_edge(self, edge_id: int):
        pass