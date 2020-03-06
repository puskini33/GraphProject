from abc import ABC, abstractmethod
from typing import List, Tuple


class EdgeRepositoryBase(ABC):

    @abstractmethod
    def insert_edge(self, edge_name: str, edge_cost: int, start_node_id: int, end_node_id: int, graph_id: int) -> int:
        pass

    @abstractmethod
    def get_edge_values(self, edge_id: int) -> List[Tuple]:
        pass

    @abstractmethod
    def get_node_edges(self, node_id: int) -> List[Tuple]:
        pass

    @abstractmethod
    def update_edge(self, edge_id: int, edge_name: str, edge_cost: int, start_node_id: int, end_node_id: int,
                    graph_id: int):
        pass

    @abstractmethod
    def delete_edge(self, edge_id: int):
        pass
