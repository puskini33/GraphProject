class NodeRepository(object):

    def insert(self, name, graph_id):
        inserted_values = f"INSERT INTO node (name, graph_id) VALUES ('{name}', '{graph_id}');"
        return inserted_values

    def get_node(self, node_id):
        node_values = f"SELECT * FROM node WHERE node.id = '{node_id}';"
        return node_values

    def get_node_edges(self, node_id):
        node_edges_values = f"SELECT node.name AS node_name, " \
                            f"edge.name AS edge_name " \
                            f"FROM node " \
                            f"JOIN graph " \
                            f"ON node.graph_id = graph.id " \
                            f"JOIN edge " \
                            f"ON edge.node_start_id = node.id " \
                            f"WHERE node.id = '{node_id}';"
        return node_edges_values

    def update(self, node_id, node_name, graph_id):
        updated_values = f"UPDATE node SET name = '{node_name}', graph_id = '{graph_id}'  WHERE id = '{node_id}';"
        return updated_values

    def delete(self, node_id):
        deleted_values = f"DELETE FROM node WHERE id = '{node_id}';"
        return deleted_values
