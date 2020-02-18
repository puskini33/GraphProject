from database_api.node_repository import NodeRepository
from database_api.tests.test_base_repository import PrepareDatabase
import unittest
import sqlite3


class TestNodeRepository(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        self.path = 'E:\\PYTHON\\code\\GraphProject\\database_api\\tests\\test_database.db'
        self.node_repository = NodeRepository(self.path)
        self.test_database_connection = sqlite3.connect(self.path)
        self.test_cursor = self.test_database_connection.cursor()
        self.database_preparation = PrepareDatabase(self.test_database_connection, self.test_cursor)
        super().__init__(*args, **kwargs)

    def delete_values_from_database(self):
        self.database_preparation.delete_node_values()
        self.database_preparation.delete_graph_values()

    def test_insert_node(self):
        try:
            # prepare
            self.delete_values_from_database()

            # act
            # insert new graph
            graph_name = 'Mara'
            self.database_preparation.insert_graph(graph_name)

            # get id of graph
            graph_id = self.database_preparation.get_graph_id(graph_name)

            # insert_graph node via node repository
            node_name = 'A'
            node_id_from_repository = self.node_repository.insert_node(node_name, graph_id)
            self.node_repository.close_connection()

            # select id inserted node
            node_id = self.database_preparation.get_node_id(node_name, graph_id)

            # assert
            self.assertEqual(node_id_from_repository, node_id)
        finally:
            self.test_database_connection.close()

    def test_get_node(self):
        try:
            # prepare
            self.delete_values_from_database()

            # act
            node_name = 'T'
            graph_name = 'Gygy'

            # insert new graph
            self.database_preparation.insert_graph(graph_name)

            # get id of new graph
            graph_id = self.database_preparation.get_graph_id(graph_name)

            # insert new node
            self.database_preparation.insert_node(node_name, graph_id)

            # get id of inserted node
            inserted_node_id = self.database_preparation.get_node_id(node_name, graph_id)

            # get values of inserted node from node_repository
            node_values_from_repository = self.node_repository.get_node(inserted_node_id)
            self.node_repository.close_connection()

            # manually get values of inserted node
            node_values = self.database_preparation.get_node_values(inserted_node_id)

            # assert
            self.assertEqual(node_values, node_values_from_repository)
        finally:
            self.test_database_connection.close()

    def test_get_graph_nodes(self):
        try:
            # prepare
            self.delete_values_from_database()

            # act
            node_name = 'R'
            graph_name = 'Tata'

            # insert new graph
            self.database_preparation.insert_graph(graph_name)

            # get id of new graph
            graph_id = self.database_preparation.get_graph_id(graph_name)

            # insert new node
            self.database_preparation.insert_node(node_name, graph_id)

            # get nodes of graph from node repository
            node_values_from_node_repository = self.node_repository.get_graph_nodes(graph_id)
            self.node_repository.close_connection()

            # manually get nodes of graph
            sql_syntax = f"SELECT graph.id, node.id , node.name "\
                         f"FROM node "\
                         f"JOIN graph "\
                         f"ON node.graph_id = graph.id "\
                         f"WHERE graph.id = '{graph_id}';"
            self.test_cursor.execute(sql_syntax)
            self.test_database_connection.commit()
            node_values = self.test_cursor.fetchall()

            # assert
            self.assertEqual(node_values, node_values_from_node_repository)
        finally:
            self.test_database_connection.close()

    def test_update_node(self):
        try:
            # prepare
            self.delete_values_from_database()

            # act
            node_name = 'R'
            graph_name = 'Haha'

            # insert new graph
            self.database_preparation.insert_graph(graph_name)

            # get id of new graph
            graph_id = self.database_preparation.get_graph_id(graph_name)

            # insert new node
            self.database_preparation.insert_node(node_name, graph_id)

            # get id of inserted node
            node_id = self.database_preparation.get_node_id(node_name, graph_id)

            # update name of new_node
            updated_node_name = 'E'
            self.node_repository.update_node(node_id, updated_node_name, graph_id)
            self.node_repository.close_connection()

            # get updated values of new_node
            updated_node_values = self.database_preparation.get_node_values(node_id)

            # assert
            self.assertEqual(updated_node_values, [(node_id, updated_node_name, graph_id)])
        finally:
            self.test_database_connection.close()

    def test_delete_node(self):
        try:
            # prepare
            self.delete_values_from_database()

            # act
            # insert new graph
            graph_name = 'Hart'
            self.database_preparation.insert_graph(graph_name)

            # get id of new graph
            graph_id = self.database_preparation.get_graph_id(graph_name)

            # insert new node
            node_name = 'P'
            self.database_preparation.insert_node(node_name, graph_id)

            # get id of inserted node
            node_id = self.database_preparation.get_node_id(node_name, graph_id)

            # delete new_node
            self.node_repository.delete_node(node_id)
            self.node_repository.close_connection()

            # verify if id exists
            sql_verify_syntax = f"SELECT node.id FROM node WHERE node.name = '{node_name}' " \
                                f"AND node.graph_id = '{graph_id}'"
            self.test_cursor.execute(sql_verify_syntax)
            self.test_database_connection.commit()
            deleted_node_id = self.test_cursor.fetchall()

            # assert
            self.assertEqual(deleted_node_id, [])
        finally:
            self.test_database_connection.close()
