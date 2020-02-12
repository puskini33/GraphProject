from database_api.node_repository import NodeRepository
import unittest
import sqlite3


class TestNodeRepository(unittest.TestCase):

    @staticmethod
    def set_database_connection():
        path = 'E:\\PYTHON\\code\\GraphProject\\database_api\\tests\\test_database.db'
        node_repository = NodeRepository(path)
        test_database_connection = sqlite3.connect(path)
        with test_database_connection:
            test_cursor = test_database_connection.cursor()
            test_cursor.execute("DELETE FROM node;")
            test_database_connection.commit()
            test_cursor.execute("DELETE FROM graph;")
            test_database_connection.commit()
        return test_database_connection, test_cursor, node_repository

    def test_insert_node(self):
        # prepare
        test_database_connection, test_cursor, node_repository = self.set_database_connection()

        # act
        node_name = 'A'
        graph_id = 1

        # insert node via node repository
        node_repository.insert_node(node_name, graph_id)
        node_repository.close_connection()

        # select name inserted node
        sql_select = f"SELECT node.name FROM node WHERE node.name = '{node_name}';"
        test_cursor.execute(sql_select)
        test_database_connection.commit()
        selected_node_name = test_cursor.fetchall()[0][0]

        # assert
        self.assertEqual(selected_node_name, node_name)

    def test_get_node(self):
        # prepare
        test_database_connection, test_cursor, node_repository = self.set_database_connection()

        # act
        node_name = 'T'
        graph_id = 1
        graph_name = 'Gygy'

        # insert new graph
        sql_insert_graph = f"INSERT OR IGNORE INTO graph VALUES ('{graph_id}', '{graph_name}');"
        test_cursor.execute(sql_insert_graph)
        test_database_connection.commit()

        # insert new node
        sql_insert_node = f"INSERT OR IGNORE INTO node (name, graph_id) VALUES ('{node_name}', '{graph_id}');"
        test_cursor.execute(sql_insert_node)
        test_database_connection.commit()

        # get id of inserted node
        sql_get_query = f"SELECT node.id FROM node WHERE node.name = '{node_name}' AND graph_id = '{graph_id}';"
        test_cursor.execute(sql_get_query)
        test_database_connection.commit()
        inserted_node_id = test_cursor.fetchall()[0][0]

        # get values of inserted node from node_repository
        node_values_from_repository = node_repository.get_node(inserted_node_id)
        node_repository.close_connection()

        # manually get values of inserted node
        sql_syntax = f"SELECT * FROM node WHERE node.id = '{inserted_node_id}';"
        test_cursor.execute(sql_syntax)
        test_database_connection.commit()
        node_values = test_cursor.fetchall()

        # assert
        self.assertEqual(node_values, node_values_from_repository)

    def test_get_graph_nodes(self):
        # prepare
        test_database_connection, test_cursor, node_repository = self.set_database_connection()

        # act
        node_name = 'R'
        graph_id = 1
        graph_name = 'Tata'
        
        # manually insert new_graph
        sql_insert_graph = f"INSERT OR IGNORE INTO graph (id, name) VALUES ('{graph_id}', '{graph_name}');"
        test_cursor.execute(sql_insert_graph)
        test_database_connection.commit()

        # manually insert new_node
        sql_insert_node = f"INSERT OR IGNORE INTO node (name, graph_id) VALUES ('{node_name}', '{graph_id}');"
        test_cursor.execute(sql_insert_node)
        test_database_connection.commit()

        # get nodes of graph from node repository
        node_values_from_node_repository = node_repository.get_graph_nodes(graph_id)
        node_repository.close_connection()

        # manually get nodes of graph
        sql_syntax = f"SELECT graph.id, node.id , node.name "\
                     f"FROM node "\
                     f"JOIN graph "\
                     f"ON node.graph_id = graph.id "\
                     f"WHERE graph.id = '{graph_id}';"
        test_cursor.execute(sql_syntax)
        test_database_connection.commit()
        node_values = test_cursor.fetchall()

        # assert
        self.assertEqual(node_values, node_values_from_node_repository)

    def test_update_node(self):
        # prepare
        test_database_connection, test_cursor, node_repository = self.set_database_connection()

        # act
        node_name = 'R'
        graph_id = 1
        graph_name = 'Haha'

        # manually insert new_graph
        sql_insert_graph = f"INSERT OR IGNORE INTO graph (id, name) VALUES ('{graph_id}', '{graph_name}');"
        test_cursor.execute(sql_insert_graph)
        test_database_connection.commit()

        # manually insert new_node
        sql_insert_statement = f"INSERT OR IGNORE INTO node (name, graph_id) VALUES ('{node_name}', '{graph_id}');"
        test_cursor.execute(sql_insert_statement)
        test_database_connection.commit()

        # get new_node id
        sql_get_query = f"SELECT node.id FROM node WHERE node.name = '{node_name}' AND graph_id = '{graph_id}';"
        test_cursor.execute(sql_get_query)
        test_database_connection.commit()
        node_id = test_cursor.fetchall()[0][0]

        # update name of new_node
        updated_node_name = 'E'
        node_repository.update_node(node_id, updated_node_name, graph_id)
        node_repository.close_connection()

        # get updated values of new_node
        sql_syntax = f"SELECT * FROM node WHERE node.id = '{node_id}';"
        test_cursor.execute(sql_syntax)
        test_database_connection.commit()
        updated_node_values = test_cursor.fetchall()

        # assert
        self.assertEqual(updated_node_values, [(node_id, updated_node_name, graph_id)])

    def test_delete_node(self):
        # prepare
        test_database_connection, test_cursor, node_repository = self.set_database_connection()

        # act
        # insert new_node
        node_name = 'D'
        graph_id = 1
        sql_insert_query = f"INSERT OR IGNORE INTO node (name, graph_id) VALUES ('{node_name}', '{graph_id}');"
        test_cursor.execute(sql_insert_query)
        test_database_connection.commit()

        # get id of new_node
        sql_syntax = f"SELECT node.id FROM node WHERE node.name = '{node_name}' AND node.graph_id = '{graph_id}'"
        test_cursor.execute(sql_syntax)
        test_database_connection.commit()
        node_id = test_cursor.fetchall()[0][0]

        # delete new_node
        node_repository.delete_node(node_id)
        node_repository.close_connection()

        # verify if id exists
        sql_verify_syntax = f"SELECT node.id FROM node WHERE node.name = '{node_name}' AND node.graph_id = '{graph_id}'"
        test_cursor.execute(sql_verify_syntax)
        test_database_connection.commit()
        deleted_node_id = test_cursor.fetchall()

        # assert
        self.assertEqual(deleted_node_id, [])
