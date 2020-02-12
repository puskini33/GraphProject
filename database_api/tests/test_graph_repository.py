from database_api.graph_repository import GraphRepository
import unittest
import sqlite3


class TestGraphRepository(unittest.TestCase):

    def test_insert_graph(self):
        # prepare
        path = 'E:\\PYTHON\\code\\GraphProject\\database_api\\tests\\test_database.db'
        graph_repository = GraphRepository(path)
        test_database_connection = sqlite3.connect(path)
        test_cursor = test_database_connection.cursor()
        test_cursor.execute("DELETE FROM graph;")
        test_database_connection.commit()

        # act
        graph_name = 'XcV4'
        graph_repository.insert(graph_name)
        graph_repository.close_connection()

        test_cursor.execute(f"SELECT graph.name FROM graph WHERE name = '{graph_name}'")
        test_database_connection.commit()
        name_existing_graph = test_cursor.fetchall()[0][0]
        test_database_connection.close()

        # assert
        self.assertEqual(name_existing_graph, graph_name)

    def test_get_graph(self):

        # prepare
        path = 'E:\\PYTHON\\code\\GraphProject\\database_api\\tests\\test_database.db'
        graph_repository = GraphRepository(path)
        test_database_connection = sqlite3.connect(path)
        test_cursor = test_database_connection.cursor()
        test_cursor.execute("DELETE FROM graph;")
        test_database_connection.commit()

        # act
        graph_name = 'gaga'

        # insert new_graph
        sql_insert_graph = f"INSERT OR IGNORE INTO graph(name) VALUES ('{graph_name}');"
        test_cursor.execute(sql_insert_graph)
        test_database_connection.commit()

        # get id of new graph
        sql_select_graph = f"SELECT graph.id FROM graph WHERE graph.name = '{graph_name}';"
        test_cursor.execute(sql_select_graph)
        test_database_connection.commit()
        graph_id = test_cursor.fetchall()[0][0]

        # get graph name from graph_repository
        graph_values_from_graph_repository = graph_repository.get_graph(graph_id)

        # manually get graph_name
        sql_select = f"SELECT graph.id, graph.name FROM graph WHERE graph.id = '{graph_id}';"
        test_cursor.execute(sql_select)
        test_database_connection.commit()
        graph_values = test_cursor.fetchall()
        test_database_connection.close()

        # assert
        self.assertEqual(graph_values, graph_values_from_graph_repository)

    def test_update_graph(self):

        # prepare
        path = 'E:\\PYTHON\\code\\GraphProject\\database_api\\tests\\test_database.db'
        graph_repository = GraphRepository(path)
        test_database_connection = sqlite3.connect(path)
        test_cursor = test_database_connection.cursor()
        test_cursor.execute("DELETE FROM graph;")
        test_database_connection.commit()

        # act
        # insert new graph
        graph_name = 'Nar'
        sql_insert_syntax = f"INSERT OR IGNORE INTO graph (name) " \
                            f"VALUES ('{graph_name}');"
        test_cursor.execute(sql_insert_syntax)
        test_database_connection.commit()

        # get the id of new graph
        sql_select_syntax = f"SELECT graph.id FROM graph WHERE graph.name = '{graph_name}';"
        test_cursor.execute(sql_select_syntax)
        test_database_connection.commit()
        graph_id = test_cursor.fetchall()[0][0]

        # update graph
        graph_updated_name = 'Updated Name'
        graph_repository.update_graph(graph_id, graph_updated_name)
        test_database_connection.commit()

        # select updated graph
        sql_select = f"SELECT graph.name FROM graph WHERE graph.id = '{graph_id}';"
        test_cursor.execute(sql_select)
        test_database_connection.commit()
        graph_name = test_cursor.fetchall()
        test_database_connection.close()

        # assert
        self.assertEqual(graph_name, [(graph_updated_name,)])

    def test_delete_graph(self):
        # prepare
        path = 'E:\\PYTHON\\code\\GraphProject\\database_api\\tests\\test_database.db'
        graph_repository = GraphRepository(path)
        test_database_connection = sqlite3.connect(path)
        test_cursor = test_database_connection.cursor()
        test_cursor.execute("DELETE FROM graph;")
        test_database_connection.commit()

        # act
        # insert new_graph
        graph_name = 'GdfeA'
        insert_sql_syntax = f"INSERT OR IGNORE INTO graph (name) " \
                            f"VALUES ('{graph_name}');"
        test_cursor.execute(insert_sql_syntax)
        test_database_connection.commit()

        # get id of new graph
        sql_select = f"SELECT graph.id FROM graph WHERE graph.name = '{graph_name}';"
        test_cursor.execute(sql_select)
        test_database_connection.commit()
        graph_id = test_cursor.fetchall()[0][0]

        # delete new_graph
        graph_repository.delete_graph(graph_id)

        # select new_graph
        sql_query = f"SELECT * FROM graph WHERE graph.id = '{graph_id}';"
        test_cursor.execute(sql_query)
        test_database_connection.commit()
        graph_values = test_cursor.fetchall()
        test_database_connection.close()

        # assert
        self.assertEqual(graph_values, [])
