from abc import ABC, abstractmethod


class NodeRepositoryBase(ABC):

    @abstractmethod
    def insert_node(self, node_name: str, node_x_coord: int, node_y_coord: int, graph_id: int) -> int:
        pass

    @abstractmethod
    def get_node(self, node_id: int) -> list:
        pass

    @abstractmethod
    def get_graph_nodes(self, graph_id: int) -> list:
        pass

    @abstractmethod
    def update_node(self, node_id: int, node_name: str, node_x_coord: int, node_y_coord: int, graph_id: int):
        pass

    @abstractmethod
    def delete_node(self, node_id: int):
        pass
