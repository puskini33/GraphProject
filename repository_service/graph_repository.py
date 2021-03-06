from contracts.repository_service.graph_repository_base import GraphRepositoryBase
from repository_service.base_repository import BaseRepository
from typing import List, Tuple


class GraphRepository(GraphRepositoryBase, BaseRepository):

    def __init__(self, path: str = None):
        super().__init__(path)

    def insert_graph(self, graph_name: str) -> int:
        inserted_values = f"INSERT OR IGNORE INTO graph (name) " \
                          f"VALUES ('{graph_name}')"
        self.execute_query(inserted_values)
        self.execute_query("SELECT last_insert_rowid();")
        return self.cursor.fetchall()[0][0]

    def get_graph(self, graph_id: int) -> List[Tuple]:
        certain_graph = f"SELECT * FROM graph WHERE graph.id = '{graph_id}';"
        self.execute_query(certain_graph)
        return self.cursor.fetchall()

    def get_all_graphs(self) -> List[Tuple]:
        all_graphs = f"SELECT * FROM graph;"
        self.execute_query(all_graphs)
        return self.cursor.fetchall()

    def update_graph(self, graph_id: int, graph_name: str):
        updated_values = f"UPDATE graph SET name = '{graph_name}' WHERE id = '{graph_id}';"
        self.execute_query(updated_values)

    def delete_graph(self, graph_id: int):
        deleted_values = f"DELETE FROM graph WHERE id = '{graph_id}';"
        self.execute_query(deleted_values)
