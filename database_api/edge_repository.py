from database_api.base_repository import BaseRepository


class EdgeRepository(BaseRepository):

    def __init__(self, path):
        super().__init__(path)

    def insert_edge(self, edge_name, edge_cost, node_start_id, node_end_id, graph_id):
        inserted_values = f"INSERT INTO edge (name, cost, node_start_id, node_end_id, graph_id) " \
                          f"VALUES ('{edge_name}', '{edge_cost}', '{node_start_id}', '{node_end_id}', '{graph_id}');"
        self.execute_query(inserted_values)

    def get_edge(self, edge_id):
        edge_values = f"SELECT * FROM edge WHERE edge.id = '{edge_id}';"
        self.execute_query(edge_values)
        return self.cursor.fetchall()

    def get_node_edges(self, node_id):
        node_edges_values = f"SELECT node.name AS node_name, " \
                            f"edge.name AS edge_name " \
                            f"FROM node " \
                            f"JOIN graph " \
                            f"ON node.graph_id = graph.id " \
                            f"JOIN edge " \
                            f"ON edge.node_start_id = node.id " \
                            f"WHERE node.id = '{node_id}';"
        self.execute_query(node_edges_values)

    def update(self, edge_id, edge_name, edge_cost, node_start_id, node_end_id, graph_id):
        updated_values = f"UPDATE edge " \
                         f"SET name = '{edge_name}', cost = '{edge_cost}', node_start_id = '{node_start_id}', " \
                         f" node_end_id = '{node_end_id}' graph_id = '{graph_id}'  WHERE id = '{edge_id}';"
        self.execute_query(updated_values)

    def delete(self, edge_id):
        deleted_values = f"DELETE FROM edge WHERE id = '{edge_id}';"
        self.execute_query(deleted_values)
