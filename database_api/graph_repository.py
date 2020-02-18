from database_api.base_repository import BaseRepository


class GraphRepository(BaseRepository):

    def __init__(self, path: str):
        super().__init__(path)

    def insert_graph(self, graph_name: str) -> str:
        inserted_values = f"INSERT OR IGNORE INTO graph (name) " \
                          f"VALUES ('{graph_name}')"
        self.execute_query(inserted_values)
        self.execute_query("SELECT last_insert_rowid();")
        return self.cursor.fetchall()[0][0]

    def get_graph(self, graph_id: str) -> list or tuple:
        certain_graph = f"SELECT * FROM graph WHERE graph.id = '{graph_id}';"
        self.execute_query(certain_graph)
        return self.cursor.fetchall()

    def update_graph(self, graph_id: str, graph_name: str):
        updated_values = f"UPDATE graph SET name = '{graph_name}' WHERE id = '{graph_id}';"
        self.execute_query(updated_values)

    def delete_graph(self, graph_id: str):
        deleted_values = f"DELETE FROM graph WHERE id = '{graph_id}';"
        self.execute_query(deleted_values)
