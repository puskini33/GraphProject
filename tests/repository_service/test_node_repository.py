from repository_service.node_repository import NodeRepository
from tests.repository_service.test_base_repository import PrepareDatabase
import unittest
import sqlite3


class TestNodeRepository(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        self.path = 'test_database.db'
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
            node_x_coord = 123
            node_y_coord = 234
            node_id_from_repository = self.node_repository.insert_node(node_name, node_x_coord, node_y_coord, graph_id)
            self.node_repository.close_connection()

            # select id inserted node
            node_id = self.database_preparation.get_node_id(node_name, node_x_coord, node_y_coord, graph_id)

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
            node_x_coord = 234
            node_y_coord = 734
            graph_name = 'Gygy'

            # insert new graph
            self.database_preparation.insert_graph(graph_name)

            # get id of new graph
            graph_id = self.database_preparation.get_graph_id(graph_name)

            # insert new node
            self.database_preparation.insert_node(node_name, node_x_coord, node_y_coord, graph_id)

            # get id of inserted node
            inserted_node_id = self.database_preparation.get_node_id(node_name, node_x_coord, node_y_coord, graph_id)

            # get values of inserted node from node_repository
            node_values_from_repository = self.node_repository.get_node(inserted_node_id)
            self.node_repository.close_connection()

            # manually get values of inserted node
            node_values = self.database_preparation.get_node_values(inserted_node_id)

            # assert
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            for index in range(len(node_values_from_repository)):
                self.assertEqual(node_values[index], node_values_from_repository[index])
=======
            for value_index in range(len(node_values_from_repository)):
                self.assertEqual(node_values[value_index], node_values_from_repository[value_index])
>>>>>>> add_line_widget
=======
            for value_index in range(len(node_values_from_repository)):
                self.assertEqual(node_values[value_index], node_values_from_repository[value_index])
>>>>>>> add_line_widget
=======
            for value_index in range(len(node_values_from_repository)):
                self.assertEqual(node_values[value_index], node_values_from_repository[value_index])
>>>>>>> add_line_widget
=======
            for value_index in range(len(node_values_from_repository)):
                self.assertEqual(node_values[value_index], node_values_from_repository[value_index])
>>>>>>> add_line_widget
        finally:
            self.test_database_connection.close()

    def test_get_graph_nodes(self):
        try:
            # prepare
            self.delete_values_from_database()

            # act
            node_name = 'R'
            node_x_coord = 278
            node_y_coord = 412
            graph_name = 'Tata'

            # insert new graph
            self.database_preparation.insert_graph(graph_name)

            # get id of new graph
            graph_id = self.database_preparation.get_graph_id(graph_name)

            # insert new node
            self.database_preparation.insert_node(node_name, node_x_coord, node_y_coord, graph_id)

            # get nodes of graph from node repository
            node_values_from_node_repository = self.node_repository.get_graph_nodes(graph_id)
            self.node_repository.close_connection()

            # manually get nodes of graph
            sql_syntax = f"SELECT node.id , node.name, node.node_x_coord AS node_x_coord, " \
                         f"node.node_y_coord AS node_y_coord, graph.id "\
                         f"FROM node "\
                         f"JOIN graph "\
                         f"ON node.graph_id = graph.id "\
                         f"WHERE graph.id = '{graph_id}';"
            self.test_cursor.execute(sql_syntax)
            self.test_database_connection.commit()
            node_values = self.test_cursor.fetchall()

            # assert
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            for index in range(len(node_values_from_node_repository)):
                self.assertEqual(node_values[0][index], node_values_from_node_repository[0][index])
=======
            for value_index in range(len(node_values_from_node_repository)):
                self.assertEqual(node_values[value_index], node_values_from_node_repository[value_index])
>>>>>>> add_line_widget
=======
            for value_index in range(len(node_values_from_node_repository)):
                self.assertEqual(node_values[value_index], node_values_from_node_repository[value_index])
>>>>>>> add_line_widget
=======
            for value_index in range(len(node_values_from_node_repository)):
                self.assertEqual(node_values[value_index], node_values_from_node_repository[value_index])
>>>>>>> add_line_widget
=======
            for value_index in range(len(node_values_from_node_repository)):
                self.assertEqual(node_values[value_index], node_values_from_node_repository[value_index])
>>>>>>> add_line_widget
        finally:
            self.test_database_connection.close()

    def test_update_node(self):
        try:
            # prepare
            self.delete_values_from_database()

            # act
            node_name = 'R'
            node_x_coord = 248
            node_y_coord = 312
            graph_name = 'Haha'

            # insert new graph
            self.database_preparation.insert_graph(graph_name)

            # get id of new graph
            graph_id = self.database_preparation.get_graph_id(graph_name)

            # insert new node
            self.database_preparation.insert_node(node_name, node_x_coord, node_y_coord, graph_id)

            # get id of inserted node
            node_id = self.database_preparation.get_node_id(node_name, node_x_coord, node_y_coord, graph_id)

            # update name of new_node
            updated_node_name = 'E'
            node_values = [(node_id, updated_node_name, node_x_coord, node_y_coord, graph_id)]

            self.node_repository.update_node(node_id, updated_node_name, node_x_coord, node_y_coord, graph_id)
            updated_node_values_from_repository = [(node_id, updated_node_name, node_x_coord, node_y_coord, graph_id)]
            self.node_repository.close_connection()

            # get updated values of new_node
            updated_node_values = self.database_preparation.get_node_values(node_id)

            # assert
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            for index in range(len(updated_node_values)):
                self.assertEqual(updated_node_values[index], node_values[index])
=======
            for value_index in range(len(updated_node_values_from_repository)):
                self.assertEqual(updated_node_values[value_index], updated_node_values_from_repository[value_index])
>>>>>>> add_line_widget
=======
            for value_index in range(len(updated_node_values_from_repository)):
                self.assertEqual(updated_node_values[value_index], updated_node_values_from_repository[value_index])
>>>>>>> add_line_widget
=======
            for value_index in range(len(updated_node_values_from_repository)):
                self.assertEqual(updated_node_values[value_index], updated_node_values_from_repository[value_index])
>>>>>>> add_line_widget
=======
            for value_index in range(len(updated_node_values_from_repository)):
                self.assertEqual(updated_node_values[value_index], updated_node_values_from_repository[value_index])
>>>>>>> add_line_widget
        finally:
            self.test_database_connection.close()

    def test_delete_node(self):
        try:
            # prepare
            self.delete_values_from_database()

            # act
            # insert new graph
            graph_name = 'Hart'
            node_x_coord = 134
            node_y_coord = 342
            self.database_preparation.insert_graph(graph_name)

            # get id of new graph
            graph_id = self.database_preparation.get_graph_id(graph_name)

            # insert new node
            node_name = 'P'
            self.database_preparation.insert_node(node_name, node_x_coord, node_y_coord, graph_id)

            # get id of inserted node
            node_id = self.database_preparation.get_node_id(node_name, node_x_coord, node_y_coord, graph_id)

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
