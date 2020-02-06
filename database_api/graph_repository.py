# TODO: make class of connection and cursor in a separate file
# TODO: make same file for node( + function that returns all edges of the node) and edge
# TODO: make tests for each element
# TODO: redo the node(attribute edge - list), graph(attributes node), edge objects based on the updated structure of tables (placed in folder bussiness_service/models)


class GraphRepository(object):

    def insert(self, graph_name):
        inserted_values = f"INSERT INTO graph (name) VALUES ('{graph_name}')"
        return inserted_values

    def get_graph(self, graph_id):
        certain_graph = f"SELECT * FROM graph WHERE graph.id = '{graph_id}';"
        return certain_graph

    def get_graph_nodes(self, graph_id):
        graph_nodes = f"SELECT graph.id AS graph_id, node.id AS node_id, node.name AS node_name "\
                      f"FROM node "\
                      f"JOIN graph "\
                      f"ON node.graph_id = graph.id "\
                      f"WHERE graph.id = '{graph_id}';"
        return graph_nodes

    def update(self, graph_id, graph_name):
        updated_values = f"UPDATE graph SET name = '{graph_name}' WHERE id = '{graph_id}';"
        return updated_values

    def delete(self, graph_id):
        deleted_values = f"DELETE FROM graph WHERE id = '{graph_id}';"
        return deleted_values




