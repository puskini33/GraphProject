from database_api.config_database import ConfigDatabase
from database_api.base_repository import BaseRepository


class GraphRepository(BaseRepository):

    def __init__(self, path='E:\\PYTHON\\code\\GraphProject\\SQL'):
        self.path = path
        super().__init__()

    @staticmethod
    def insert(graph_id, graph_name):
        inserted_values = f"INSERT OR IGNORE INTO graph (id, name) " \
                          f"VALUES ('{graph_id}', '{graph_name}')"
        # +IGNORE Syntax: That there is no error if the same values are to be inserted
        # or if a value is inserted where already another value exists
        return inserted_values

    @staticmethod
    def get_graph(graph_id):
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
