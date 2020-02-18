from database_api.base_repository import BaseRepository


class NodeRepository(BaseRepository):

    def __init__(self, path):
        super().__init__(path)

    def insert_node(self, node_name: str, graph_id: int):
        inserted_values = f"INSERT OR IGNORE INTO node (name, graph_id) VALUES ('{node_name}', '{graph_id}');"
        self.execute_query(inserted_values)
        self.execute_query("SELECT last_insert_rowid();")
        return self.cursor.fetchall()[0][0]

    def get_node(self, node_id: int) -> list:
        node_values = f"SELECT * FROM node WHERE node.id = '{node_id}';"
        self.execute_query(node_values)
        return self.cursor.fetchall()

    def get_graph_nodes(self, graph_id: int) -> list:
        graph_nodes = f"SELECT graph.id AS graph_id, node.id AS node_id, node.name AS node_name "\
                      f"FROM node "\
                      f"JOIN graph "\
                      f"ON node.graph_id = graph.id "\
                      f"WHERE graph.id = '{graph_id}';"
        self.execute_query(graph_nodes)
        return self.cursor.fetchall()

    def update_node(self, node_id: int, node_name: str, graph_id: int):
        updated_values = f"UPDATE node SET name = '{node_name}', graph_id = '{graph_id}'  WHERE id = '{node_id}';"
        self.execute_query(updated_values)

    def delete_node(self, node_id: int):
        deleted_values = f"DELETE FROM node WHERE id = '{node_id}';"
        self.execute_query(deleted_values)
