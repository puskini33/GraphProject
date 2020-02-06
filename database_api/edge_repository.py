class EdgeRepository(object):

    def insert(self, edge_name, edge_cost, node_start_id, node_end_id, graph_id):
        inserted_values = f"INSERT INTO edge (name, cost, node_start_id, node_end_id, graph_id) VALUES ('{edge_name}', '{edge_cost}', '{node_start_id}', '{node_end_id}', '{graph_id}');"
        return inserted_values

    def get_edge(self, edge_id):
        edge_values = f"SELECT * FROM edge WHERE edge.id = '{edge_id}';"
        return edge_values

    def update(self, edge_id, edge_name, edge_cost, node_start_id, node_end_id, graph_id):
        updated_values = f"UPDATE edge SET name = '{edge_name}', cost = '{edge_cost}', node_start_id = '{node_start_id}', " \
                         f" node_end_id = '{node_end_id}' graph_id = '{graph_id}'  WHERE id = '{edge_id}';"
        return updated_values

    def delete(self, edge_id):
        deleted_values = f"DELETE FROM edge WHERE id = '{edge_id}';"
        return deleted_values
