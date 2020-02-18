from database_api.graph_repository import GraphRepository
from database_api.tests.test_base_repository import PrepareDatabase
import unittest
import sqlite3


class TestGraphRepository(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        self.path = 'E:\\PYTHON\\code\\GraphProject\\database_api\\tests\\test_database.db'
        self.graph_repository = GraphRepository(self.path)
        self.test_database_connection = sqlite3.connect(self.path)
        with self.test_database_connection:
            self.test_cursor = self.test_database_connection.cursor()
            self.database_preparation = PrepareDatabase(self.test_database_connection, self.test_cursor)
        super().__init__(*args, **kwargs)

    def delete_values_from_database(self):
        self.database_preparation.delete_graph_values()

    def test_insert_graph(self):
        # prepare
        self.delete_values_from_database()

        # act
        graph_name = 'XcV4'

        # get graph id from graph_repository
        graph_id_from_repository = self.graph_repository.insert_graph(graph_name)
        self.graph_repository.close_connection()

        # get id of graph
        graph_id = self.database_preparation.get_graph_id(graph_name)

        # assert
        self.assertEqual(graph_id_from_repository, graph_id)

    def test_get_graph(self):
        # prepare
        self.delete_values_from_database()

        # act
        graph_name = 'gaga'

        # insert_graph new_graph
        self.database_preparation.insert_graph(graph_name)

        # get id of graph
        graph_id = self.database_preparation.get_graph_id(graph_name)

        # get graph name from graph_repository
        graph_values_from_graph_repository = self.graph_repository.get_graph(graph_id)
        self.graph_repository.close_connection()

        # manually get graph values
        graph_values = self.database_preparation.get_graph_values(graph_id)

        # assert
        self.assertEqual(graph_values, graph_values_from_graph_repository)

    def test_update_graph(self):
        # prepare
        self.delete_values_from_database()

        # act
        # insert_graph new graph
        graph_name = 'Nar'
        self.database_preparation.insert_graph(graph_name)

        # get id of graph
        graph_id = self.database_preparation.get_graph_id(graph_name)

        # update graph
        graph_updated_name = 'Updated Name'
        self.graph_repository.update_graph(graph_id, graph_updated_name)
        self.graph_repository.close_connection()

        # select updated graph
        sql_select = f"SELECT graph.name FROM graph WHERE graph.id = '{graph_id}';"
        self.test_cursor.execute(sql_select)
        self.test_database_connection.commit()
        graph_name = self.test_cursor.fetchall()

        # assert
        self.assertEqual(graph_name, [(graph_updated_name,)])

    def test_delete_graph(self):
        # prepare
        self.delete_values_from_database()

        # act
        # insert_graph new_graph
        graph_name = 'GdfeA'
        self.database_preparation.insert_graph(graph_name)

        # get id of graph
        graph_id = self.database_preparation.get_graph_id(graph_name)

        # delete new_graph
        self.graph_repository.delete_graph(graph_id)
        self.graph_repository.close_connection()

        # select graph values
        graph_values = self.database_preparation.get_graph_values(graph_id)

        # assert
        self.assertEqual(graph_values, [])
