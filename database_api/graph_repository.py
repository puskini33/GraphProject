from database_api.config_database import ConfigDatabase
from database_api.base_repository import BaseRepository


class GraphRepository(BaseRepository):

    def __init__(self, path='E:\\PYTHON\\code\\GraphProject\\SQL'):
        self.path = path
        super().__init__()

    def insert(self, graph_id, graph_name):
        inserted_values = f"INSERT OR IGNORE INTO graph (id, name) " \
                          f"VALUES ('{graph_id}', '{graph_name}')"

        return

    # Question: Why does it not work when i try to call the execute_commit_fetch method in the insert method?

    def close_database(self):
        return self.connection.close()

    def get_graph(self, graph_id):
        certain_graph = f"SELECT * FROM graph WHERE graph.id = '{graph_id}';"
        return certain_graph

    @staticmethod
    def get_graph_nodes(graph_id):
        graph_nodes = f"SELECT graph.id AS graph_id, node.id AS node_id, node.name AS node_name "\
                      f"FROM node "\
                      f"JOIN graph "\
                      f"ON node.graph_id = graph.id "\
                      f"WHERE graph.id = '{graph_id}';"
        return graph_nodes

    @staticmethod
    def update_graph(graph_id, graph_name):
        updated_values = f"UPDATE graph SET name = '{graph_name}' WHERE id = '{graph_id}';"
        return updated_values

    @staticmethod
    def delete_graph(graph_id):
        deleted_values = f"DELETE FROM graph WHERE id = '{graph_id}';"
        return deleted_values

    def execute_commit_fetch(self, syntax):
        self.cursor.execute(syntax)
        self.connection.commit()
        return self.cursor.fetchall()
