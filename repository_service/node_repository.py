from repository_service.base_repository import BaseRepository
from repository_service.contracts.node_repository_base import NodeRepositoryBase
from typing import List, Tuple


class NodeRepository(BaseRepository, NodeRepositoryBase):

    def __init__(self, path: str = None):
        super().__init__(path)

    def insert_node(self, node_name: str, node_x_coord: int, node_y_coord: int, graph_id: int) -> int:
        inserted_values = f"INSERT OR IGNORE INTO node (name, node_x_coord, node_y_coord, graph_id) " \
                          f"VALUES ('{node_name}', '{node_x_coord}', '{node_y_coord}', '{graph_id}');"
        self.execute_query(inserted_values)
        self.execute_query("SELECT last_insert_rowid();")
        return self.cursor.fetchall()[0][0]

    def get_node(self, node_id: int) -> List[Tuple]:
        node_values = f"SELECT * FROM node WHERE node.id = '{node_id}';"
        self.execute_query(node_values)
        return self.cursor.fetchall()

    def get_graph_nodes(self, graph_id: int) -> List[Tuple]:
        graph_nodes = f"SELECT node.id AS node_id, node.name AS node_name, node.node_x_coord AS node_x_coord, " \
                      f"node.node_y_coord AS node_y_coord, graph.id AS graph_id "\
                      f"FROM node "\
                      f"JOIN graph "\
                      f"ON node.graph_id = graph.id "\
                      f"WHERE graph.id = '{graph_id}';"
        self.execute_query(graph_nodes)
        return self.cursor.fetchall()

    def update_node(self, node_id: int, node_name: str, node_x_coord: int, node_y_coord: int, graph_id: int):
        updated_values = f"UPDATE node SET name = '{node_name}', node_x_coord = '{node_x_coord}', " \
                         f"node_y_coord = '{node_y_coord}', graph_id = '{graph_id}'  WHERE id = '{node_id}';"
        self.execute_query(updated_values)

    def delete_node(self, node_id: int):
        deleted_values = f"DELETE FROM node WHERE id = '{node_id}';"
        self.execute_query(deleted_values)
