from contracts.repository_service.node_repository_base import NodeRepositoryBase
from typing import List, Tuple


class NodeRepositoryMock(NodeRepositoryBase):
    def __init__(self):
        self.first_node_id = 16
        self.first_node_name = 'TestNodeName0'
        self.first_x_coord = 100
        self.first_y_coord = 87
        self.graph_id = 1
        self.second_node_id = 17
        self.second_node_name = 'TestNodeName1'
        self.second_x_coord = 134
        self.second_y_coord = 187

    def insert_node(self, node_name: str, node_x_coord: int, node_y_coord: int, graph_id: int) -> int:
        return self.first_node_id

    def get_node(self, node_id: int) -> List[Tuple]:
        return [(self.first_node_id, self.first_node_name, self.first_x_coord, self.first_y_coord, self.graph_id)]

    def get_graph_nodes(self, graph_id: int) -> List[Tuple]:
        return [(self.first_node_id, self.first_node_name, self.first_x_coord, self.first_y_coord, self.graph_id),
                (self.second_node_id, self.second_node_name, self.second_x_coord, self.second_y_coord, self.graph_id)]

    def update_node(self, node_id: int, node_name: str, node_x_coord: int, node_y_coord: int, graph_id: int):
        return

    def delete_node(self, node_id: int):
        pass
