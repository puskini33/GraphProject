from contracts.repository_service.edge_repository_base import EdgeRepositoryBase
from typing import List, Tuple


class EdgeRepositoryMock(EdgeRepositoryBase):
    def __init__(self):
        self.first_edge_id = 9
        self.first_edge_name = 'TestEdgeName0'
        self.first_edge_cost = 13
        self.first_start_node_id = 3
        self.first_end_node_id = 5
        self.second_edge_id = 10
        self.second_edge_name = 'TestEdgeName1'
        self.second_edge_cost = 17
        self.second_start_node_id = 2
        self.graph_id = 1

    def insert_edge(self, edge_name: str, edge_cost: int, start_node_id: int, end_node_id: int, graph_id: int) -> int:
        return self.first_edge_id

    def get_edge_values(self, edge_id: int) -> List[Tuple]:
        return [(self.first_edge_id, self.first_edge_name, self.first_edge_cost,
                 self.first_start_node_id, self.first_end_node_id, self.graph_id)]

    def get_node_edges(self, node_id: int) -> List[Tuple]:
        return [(self.first_edge_id, self.first_edge_name, self.first_edge_cost,
                 self.first_start_node_id, self.first_end_node_id, self.graph_id),
                (self.second_edge_id, self.second_edge_name, self.second_edge_cost,
                 self.second_start_node_id, self.first_end_node_id, self.graph_id)
                ]

    def get_graph_edges(self, graph_id: int) -> List[Tuple]:
        return [(self.first_edge_id, self.first_edge_name, self.first_edge_cost,
                 self.first_start_node_id, self.first_end_node_id, self.graph_id),
                (self.second_edge_id, self.second_edge_name, self.second_edge_cost,
                 self.second_start_node_id, self.first_end_node_id, self.graph_id)
                ]

    def update_edge(self, edge_id: int, edge_name: str, edge_cost: int, start_node_id: int, end_node_id: int,
                    graph_id: int):
        return

    def delete_edge(self, edge_id: int):
        pass
