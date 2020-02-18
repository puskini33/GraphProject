class PrepareDatabase(object):

    def __init__(self, test_database_connection, test_cursor):
        self.test_database_connection = test_database_connection
        self.test_cursor = test_cursor

    def delete_graph_values(self):
        self.test_cursor.execute("DELETE FROM graph;")
        self.test_database_connection.commit()

    def delete_node_values(self):
        self.test_cursor.execute("DELETE FROM node;")
        self.test_database_connection.commit()

    def delete_edge_values(self):
        self.test_cursor.execute("DELETE FROM edge;")
        self.test_database_connection.commit()

    def insert_graph(self, graph_name):
        sql_insert_graph = f"INSERT OR IGNORE INTO graph (name) " \
            f"VALUES ('{graph_name}');"
        self.test_cursor.execute(sql_insert_graph)
        self.test_database_connection.commit()

    def insert_node(self, node_name, graph_id):
        sql_insert_node_start = f"INSERT OR IGNORE INTO node(graph_id, name) VALUES ('{graph_id}', '{node_name}');"
        self.test_cursor.execute(sql_insert_node_start)
        self.test_database_connection.commit()

    def insert_edge(self, edge_name, edge_cost, node_start_id, node_end_id, graph_id):
        sql_insert_new_edge = f"INSERT INTO edge (name, cost, node_start_id, node_end_id, graph_id) " \
            f"VALUES ('{edge_name}', '{edge_cost}', '{node_start_id}', '{node_end_id}', '{graph_id}');"
        self.test_cursor.execute(sql_insert_new_edge)
        self.test_database_connection.commit()

    def get_graph_id(self, graph_name):
        sql_select_syntax = f"SELECT graph.id FROM graph WHERE graph.name = '{graph_name}';"
        self.test_cursor.execute(sql_select_syntax)
        self.test_database_connection.commit()
        return self.test_cursor.fetchall()[0][0]

    def get_node_id(self, node_name, graph_id):
        sql_get_node_start_name = f"SELECT node.id FROM node WHERE node.name = '{node_name}' AND graph_id = '{graph_id}';"
        self.test_cursor.execute(sql_get_node_start_name)
        self.test_database_connection.commit()
        return self.test_cursor.fetchall()[0][0]

    def get_edge_id(self, edge_name, edge_cost, node_start_id, node_end_id, graph_id):
        sql_get_edge_id = f"SELECT id FROM edge WHERE name = '{edge_name}' AND cost = '{edge_cost}' AND " \
            f"node_start_id = '{node_start_id}' AND node_end_id = '{node_end_id}' AND graph_id = '{graph_id}';"
        self.test_cursor.execute(sql_get_edge_id)
        self.test_database_connection.commit()
        return self.test_cursor.fetchall()[0][0]



