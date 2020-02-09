from database_api.base_repository import BaseRepository


class GraphRepository(BaseRepository):

    def __init__(self):
        super().__init__()

    def insert(self, graph_name):
        inserted_values = f"INSERT OR IGNORE INTO graph (name) " \
                          f"VALUES ('{graph_name}')"
        self.execute_query(inserted_values)

    def get_graph(self, graph_id):
        certain_graph = f"SELECT * FROM graph WHERE graph.id = '{graph_id}';"
        self.execute_query(certain_graph)
        return self.cursor.fetchall()

    def update_graph(self, graph_id, graph_name):
        updated_values = f"UPDATE graph SET name = '{graph_name}' WHERE id = '{graph_id}';"
        self.execute_query(updated_values)

    def delete_graph(self, graph_id):
        deleted_values = f"DELETE FROM graph WHERE id = '{graph_id}';"
        self.execute_query(deleted_values)
