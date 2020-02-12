from database_api.edge_repository import EdgeRepository
import unittest
import sqlite3


class TestEdgeRepository(unittest.TestCase):

    @staticmethod
    def set_database_connection():
        path = 'E:\\PYTHON\\code\\GraphProject\\database_api\\tests\\test_database.db'
        edge_repository = EdgeRepository(path)
        test_database_connection = sqlite3.connect(path)
        with test_database_connection:
            test_cursor = test_database_connection.cursor()
            test_cursor.execute("DELETE FROM edge;")
            test_database_connection.commit()
            test_cursor.execute("DELETE FROM node;")
            test_database_connection.commit()
            test_cursor.execute("DELETE FROM graph;")
            test_database_connection.commit()
        return test_database_connection, test_cursor, edge_repository

    @staticmethod
    def insert_graph(test_database_connection, test_cursor, graph_name):
        sql_insert_graph = f"INSERT OR IGNORE INTO graph (name) " \
            f"VALUES ('{graph_name}');"
        test_cursor.execute(sql_insert_graph)
        test_database_connection.commit()

    @staticmethod
    def insert_node(test_database_connection, test_cursor, node_name, graph_id):
        sql_insert_node_start = f"INSERT OR IGNORE INTO node(graph_id, name) VALUES ('{graph_id}', '{node_name}');"
        test_cursor.execute(sql_insert_node_start)
        test_database_connection.commit()

    @staticmethod
    def get_graph_id(test_database_connection, test_cursor, graph_name):
        sql_select_syntax = f"SELECT graph.id FROM graph WHERE graph.name = '{graph_name}';"
        test_cursor.execute(sql_select_syntax)
        test_database_connection.commit()
        return test_cursor.fetchall()[0][0]

    @staticmethod
    def get_node_id (test_database_connection, test_cursor, node_name, graph_id):
        sql_get_node_start_name = f"SELECT node.id FROM node WHERE node.name = '{node_name}' AND graph_id = '{graph_id}';"
        test_cursor.execute(sql_get_node_start_name)
        test_database_connection.commit()
        return test_cursor.fetchall()[0][0]

    def test_insert_edge(self):
        # prepare
        test_database_connection, test_cursor, edge_repository = self.set_database_connection()

        # act
        # insert new graph
        graph_name = 'Gaga'
        self.insert_graph(test_database_connection, test_cursor, graph_name)

        # get id of graph
        graph_id = self.get_graph_id(test_database_connection, test_cursor, graph_name)

        # insert 2 nodes
        node_start_name = 'L'
        self.insert_node(test_database_connection, test_cursor, node_start_name, graph_id)

        node_end_name = 'G'
        self.insert_node(test_database_connection, test_cursor, node_end_name, graph_id)

        # get id of nodes
        node_start_id = self.get_node_id(test_database_connection, test_cursor, node_start_name, graph_id)
        node_end_id = self.get_node_id(test_database_connection, test_cursor, node_end_name, graph_id)

        # insert new_edge via edge_repository
        edge_name = 'LG'
        edge_cost = 34
        edge_repository.insert_edge(edge_name, edge_cost, node_start_id, node_end_id, graph_id)
        edge_repository.close_connection()

        # select values of new edge
        sql_select_edge = f"SELECT name, cost FROM edge WHERE node_start_id = '{node_start_id}' AND " \
                          f"node_end_id = '{node_end_id}' AND graph_id = '{graph_id}';"
        test_cursor.execute(sql_select_edge)
        test_database_connection.commit()
        edge_values = test_cursor.fetchall()[0]

        # assert
        self.assertEqual(edge_values, (edge_name, edge_cost))

    def test_get_edge(self):
        # prepare
        test_database_connection, test_cursor, edge_repository = self.set_database_connection()

        # act
        # insert new graph
        graph_name = 'Mimo'
        self.insert_graph(test_database_connection, test_cursor, graph_name)

        # get id of graph
        graph_id = self.get_graph_id(test_database_connection, test_cursor, graph_name)

        # insert 2 nodes
        node_start_name = 'K'
        self.insert_node(test_database_connection, test_cursor, node_start_name, graph_id)

        node_end_name = 'A'
        self.insert_node(test_database_connection, test_cursor, node_end_name, graph_id)

        # get id of nodes
        node_start_id = self.get_node_id(test_database_connection, test_cursor, node_start_name, graph_id)
        node_end_id = self.get_node_id(test_database_connection, test_cursor, node_end_name, graph_id)

        # insert new edge
        edge_name = 'KA'
        edge_cost = 49
        sql_insert_new_edge = f"INSERT INTO edge (name, cost, node_start_id, node_end_id, graph_id) " \
                              f"VALUES ('{edge_name}', '{edge_cost}', '{node_start_id}', '{node_end_id}', '{graph_id}');"
        test_cursor.execute(sql_insert_new_edge)
        test_database_connection.commit()

        # manually get id of new edge
        sql_get_edge_id = f"SELECT id FROM edge WHERE name = '{edge_name}' AND cost = '{edge_cost}' AND " \
                          f"node_start_id = '{node_start_id}' AND node_end_id = '{node_end_id}' AND graph_id = '{graph_id}';"
        test_cursor.execute(sql_get_edge_id)
        test_database_connection.commit()
        edge_id = test_cursor.fetchall()[0][0]

        # get values of edge via edge_repository
        edge_values = edge_repository.get_edge(edge_id)[0]
        edge_repository.close_connection()

        # assert
        self.assertEqual(edge_values, (edge_id, edge_name, edge_cost, node_start_id, node_end_id, graph_id, ))

    def test_get_edge_nodes(self):
        # prepare
        test_database_connection, test_cursor, edge_repository = self.set_database_connection()

        # act
        # insert new graph
        graph_name = 'Cara'
        self.insert_graph(test_database_connection, test_cursor, graph_name)

        # get id of graph
        graph_id = self.get_graph_id(test_database_connection, test_cursor, graph_name)

        # insert 2 nodes
        node_start_name = 'P'
        self.insert_node(test_database_connection, test_cursor, node_start_name, graph_id)

        node_end_name = 'E'
        self.insert_node(test_database_connection, test_cursor, node_end_name, graph_id)

        # get id of nodes
        node_start_id = self.get_node_id(test_database_connection, test_cursor, node_start_name, graph_id)
        node_end_id = self.get_node_id(test_database_connection, test_cursor, node_end_name, graph_id)

        # insert new edge
        edge_name = 'PE'
        edge_cost = 56
        sql_insert_new_edge = f"INSERT INTO edge (name, cost, node_start_id, node_end_id, graph_id) " \
                              f"VALUES ('{edge_name}', '{edge_cost}', '{node_start_id}', '{node_end_id}', '{graph_id}');"
        test_cursor.execute(sql_insert_new_edge)
        test_database_connection.commit()

        # get edges of nodes from edge_repository
        node_edge_values = edge_repository.get_node_edges(node_start_id)[0]
        edge_repository.close_connection()

        # assert
        self.assertEqual(node_edge_values, (node_start_name, edge_name))

    def test_update_edge(self):
        # prepare
        test_database_connection, test_cursor, edge_repository = self.set_database_connection()

        # act
        # insert new graph
        graph_name = 'Mera'
        self.insert_graph(test_database_connection, test_cursor, graph_name)

        # get id of graph
        graph_id = self.get_graph_id(test_database_connection, test_cursor, graph_name)

        # insert 2 nodes
        node_start_name = 'V'
        self.insert_node(test_database_connection, test_cursor, node_start_name, graph_id)

        node_end_name = 'S'
        self.insert_node(test_database_connection, test_cursor, node_end_name, graph_id)

        # get id of nodes
        node_start_id = self.get_node_id(test_database_connection, test_cursor, node_start_name, graph_id)
        node_end_id = self.get_node_id(test_database_connection, test_cursor, node_end_name, graph_id)

        # insert new edge
        edge_name = 'VS'
        edge_cost = 2
        sql_insert_new_edge = f"INSERT INTO edge (name, cost, node_start_id, node_end_id, graph_id) " \
                              f"VALUES ('{edge_name}', '{edge_cost}', '{node_start_id}', '{node_end_id}', '{graph_id}');"
        test_cursor.execute(sql_insert_new_edge)
        test_database_connection.commit()

        # manually get id of new edge
        sql_get_edge_id = f"SELECT id FROM edge WHERE name = '{edge_name}' AND cost = '{edge_cost}' AND " \
                          f"node_start_id = '{node_start_id}' AND node_end_id = '{node_end_id}' AND graph_id = '{graph_id}';"
        test_cursor.execute(sql_get_edge_id)
        test_database_connection.commit()
        edge_id = test_cursor.fetchall()[0][0]

        # update edge via edge_repository
        new_edge_cost = 36
        edge_repository.update_edge(edge_id, edge_name, new_edge_cost, node_start_id, node_end_id, graph_id)
        edge_repository.close_connection()

        # get updated_cost of edge
        sql_get_edge_updated_cost = f"SELECT cost FROM edge WHERE id = '{edge_id}' AND name = '{edge_name}' AND " \
            f"node_start_id = '{node_start_id}' AND node_end_id = '{node_end_id}' AND graph_id = '{graph_id}';"
        test_cursor.execute(sql_get_edge_updated_cost)
        test_database_connection.commit()
        updated_edge_cost = test_cursor.fetchall()[0][0]

        # assert
        self.assertEqual(updated_edge_cost, new_edge_cost)

    def test_delete_edge(self):
        # prepare
        test_database_connection, test_cursor, edge_repository = self.set_database_connection()

        # act
        # insert new graph
        graph_name = 'Tare'
        self.insert_graph(test_database_connection, test_cursor, graph_name)

        # get id of graph
        graph_id = self.get_graph_id(test_database_connection, test_cursor, graph_name)

        # insert 2 nodes
        node_start_name = 'G'
        self.insert_node(test_database_connection, test_cursor, node_start_name, graph_id)

        node_end_name = 'M'
        self.insert_node(test_database_connection, test_cursor, node_end_name, graph_id)

        # get id of nodes
        node_start_id = self.get_node_id(test_database_connection, test_cursor, node_start_name, graph_id)
        node_end_id = self.get_node_id(test_database_connection, test_cursor, node_end_name, graph_id)

        # insert new edge
        edge_name = 'GM'
        edge_cost = 29
        sql_insert_new_edge = f"INSERT INTO edge (name, cost, node_start_id, node_end_id, graph_id) " \
            f"VALUES ('{edge_name}', '{edge_cost}', '{node_start_id}', '{node_end_id}', '{graph_id}');"
        test_cursor.execute(sql_insert_new_edge)
        test_database_connection.commit()

        # manually get id of new edge
        sql_get_edge_id = f"SELECT id FROM edge WHERE name = '{edge_name}' AND cost = '{edge_cost}' AND " \
            f"node_start_id = '{node_start_id}' AND node_end_id = '{node_end_id}' AND graph_id = '{graph_id}';"
        test_cursor.execute(sql_get_edge_id)
        test_database_connection.commit()
        edge_id = test_cursor.fetchall()[0][0]

        # delete edge from edge_repository
        edge_repository.delete_edge(edge_id)
        edge_repository.close_connection()

        # manually check if edge is deleted
        sql_statement_edge_id = f"SELECT id FROM edge WHERE name = '{edge_name}' AND cost = '{edge_cost}' AND " \
                                f"node_start_id = '{node_start_id}' AND node_end_id = '{node_end_id}' AND graph_id = '{graph_id}';"
        test_cursor.execute(sql_statement_edge_id)
        test_database_connection.commit()
        deleted_edge_id = test_cursor.fetchall()

        # assert
        self.assertEqual(deleted_edge_id, [])
