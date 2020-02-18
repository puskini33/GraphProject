from database_api.base_repository import BaseRepository


class EdgeRepository(BaseRepository):

    def __init__(self, path: str):
        super().__init__(path)

    def insert_edge(self, edge_name: str, edge_cost: int, node_start_id: str, node_end_id: str, graph_id: str) -> str:
        inserted_values = f"INSERT INTO edge (name, cost, node_start_id, node_end_id, graph_id) " \
                          f"VALUES ('{edge_name}', '{edge_cost}', '{node_start_id}', '{node_end_id}', '{graph_id}');"
        self.execute_query(inserted_values)
        self.execute_query("SELECT last_insert_rowid();")
        return self.cursor.fetchall()[0][0]

    def get_edge_values(self, edge_id: str) -> list or tuple:
        edge_values = f"SELECT * FROM edge WHERE edge.id = '{edge_id}';"
        self.execute_query(edge_values)
        return self.cursor.fetchall()

    def get_node_edges(self, node_id: str) -> list or tuple:
        node_edges_values = f"SELECT node.name AS node_name, " \
                            f"edge.name AS edge_name " \
                            f"FROM node " \
                            f"JOIN graph " \
                            f"ON node.graph_id = graph.id " \
                            f"JOIN edge " \
                            f"ON edge.node_start_id = node.id " \
                            f"WHERE node.id = '{node_id}';"
        self.execute_query(node_edges_values)
        return self.cursor.fetchall()

    def update_edge(self, edge_id: str, edge_name: str, edge_cost: int, node_start_id: str, node_end_id: str,
                    graph_id: str):
        updated_values = f"UPDATE edge " \
                         f"SET name = '{edge_name}', cost = '{edge_cost}', node_start_id = '{node_start_id}', " \
                         f" node_end_id = '{node_end_id}', graph_id = '{graph_id}'  WHERE id = '{edge_id}';"
        self.execute_query(updated_values)

    def delete_edge(self, edge_id: str):
        deleted_values = f"DELETE FROM edge WHERE id = '{edge_id}';"
        self.execute_query(deleted_values)
