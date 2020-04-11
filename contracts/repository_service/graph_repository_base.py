from abc import ABC, abstractmethod
from typing import List, Tuple


class GraphRepositoryBase(ABC):

    @abstractmethod
    def insert_graph(self, graph_name: str) -> int:
        pass

    @abstractmethod
    def get_graph(self, graph_id: int) -> List[Tuple]:
        pass

    @abstractmethod
    def get_all_graphs(self) -> List[Tuple]:
        pass

    @abstractmethod
    def update_graph(self, graph_id: int, graph_name: str):
        pass

    @abstractmethod
    def delete_graph(self, graph_id: int):
        pass
