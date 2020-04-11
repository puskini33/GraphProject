from models.graph_model import GraphModel
from abc import ABC, abstractmethod
from typing import List


class GraphBusinessServiceBase(ABC):

    @abstractmethod
    def insert_graph(self, graph_model: GraphModel) -> GraphModel:
        pass

    @abstractmethod
    def get_graph_model(self, graph_id: int) -> GraphModel:
        pass

    @abstractmethod
    def get_all_graph_models(self) -> List[GraphModel]:
        pass

    @abstractmethod
    def update_graph(self, graph_model: GraphModel) -> GraphModel:
        pass

    @abstractmethod
    def delete_graph(self, graph_id: int):
        pass
