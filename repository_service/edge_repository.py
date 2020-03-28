from repository_service.base_repository import BaseRepository
from contracts.repository_service.edge_repository_base import EdgeRepositoryBase
from typing import List, Tuple


class EdgeRepository(BaseRepository, EdgeRepositoryBase):

    def __init__(self, path: str = None):
        super().__init__(path)

    def insert_edge(self, edge_name: str, edge_cost: int, start_node_id: int, end_node_id: int, graph_id: int) -> int:
        inserted_values = f"INSERT INTO edge (name, cost, start_node_id, end_node_id, graph_id) " \
                          f"VALUES ('{edge_name}', '{edge_cost}', '{start_node_id}', '{end_node_id}', '{graph_id}');"
        self.execute_query(inserted_values)
        self.execute_query("SELECT last_insert_rowid();")
        return self.cursor.fetchall()[0][0]

    def get_edge_values(self, edge_id: int) -> List[Tuple]:
        edge_values = f"SELECT * FROM edge WHERE edge.id = '{edge_id}';"
        self.execute_query(edge_values)
        return self.cursor.fetchall()

    def get_node_edges(self, node_id: int) -> List[Tuple]:
        node_edges_values = f"SELECT edge.id, edge.name, edge.cost, edge.start_node_id, edge.end_node_id, edge.graph_id " \
                            f"FROM node " \
                            f"JOIN graph " \
                            f"ON node.graph_id = graph.id " \
                            f"JOIN edge " \
                            f"ON edge.start_node_id = node.id OR edge.end_node_id = node.id " \
                            f"WHERE node.id = '{node_id}';"
        self.execute_query(node_edges_values)
        return self.cursor.fetchall()

    def get_graph_edges(self, graph_id: int) -> List[Tuple]:
        graph_edge_values = f"SELECT edge.id, edge.name, edge.cost, edge.start_node_id, edge.end_node_id,edge.graph_id " \
                            f"FROM edge " \
                            f"JOIN node " \
                            f"ON edge.start_node_id = node.id OR edge.end_node_id = node.id " \
                            f"JOIN graph " \
                            f"ON edge.graph_id = graph.id " \
                            f"WHERE graph.id = {graph_id}; "
        self.execute_query(graph_edge_values)
        return self.cursor.fetchall()

    def update_edge(self, edge_id: int, edge_name: str, edge_cost: int, start_node_id: int, end_node_id: int,
                    graph_id: int):
        updated_values = f"UPDATE edge " \
                         f"SET name = '{edge_name}', cost = '{edge_cost}', start_node_id = '{start_node_id}', " \
                         f" end_node_id = '{end_node_id}', graph_id = '{graph_id}'  WHERE id = '{edge_id}';"
        self.execute_query(updated_values)

    def delete_edge(self, edge_id: int):
        deleted_values = f"DELETE FROM edge WHERE id = '{edge_id}';"
        self.execute_query(deleted_values)