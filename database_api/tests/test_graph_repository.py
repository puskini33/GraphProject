from database_api.graph_repository import GraphRepository
import unittest
import sqlite3


# TODO: Figure it out why only one test is run instead of all 4 when I run from Pycharm in comparison to command line.
class TestGraphRepository(unittest.TestCase):

    def test_insert_graph(self):

        # prepare
        insert_to_graph_repository = GraphRepository()
        database_connection = sqlite3.connect(insert_to_graph_repository.path)
        cursor = database_connection.cursor()

        # act
        graph_name = 'XcV4 Graph'
        insert_to_graph_repository.insert(graph_name)

        sql_select = f"SELECT graph.id, graph.name FROM graph WHERE graph.name = '{graph_name}';"
        cursor.execute(sql_select)
        values_existing_graph = cursor.fetchall()

        # assert
        self.assertEqual(values_existing_graph[0][1], graph_name)
        database_connection.commit()
        database_connection.close()

    def test_get_graph(self):

        # prepare
        get_graph_repository = GraphRepository()
        database_connection = sqlite3.connect(get_graph_repository.path)
        cursor = database_connection.cursor()

        # act
        graph_id = 2
        graph_name = get_graph_repository.get_graph(graph_id)

        sql_select = f"SELECT graph.id, graph.name FROM graph WHERE graph.id = '{graph_id}';"
        cursor.execute(sql_select)
        values_existing_graph = cursor.fetchall()

        # assert
        self.assertEqual(values_existing_graph, graph_name)
        database_connection.commit()
        database_connection.close()

    def test_update_graph(self):

        # prepare
        update_graph_repository = GraphRepository()
        database_connection = sqlite3.connect(update_graph_repository.path)
        cursor = database_connection.cursor()

        # act

        # insert new graph
        graph_name = 'Nar Graph'
        insert_sql_syntax = f"INSERT OR IGNORE INTO graph (name) " \
                            f"VALUES ('{graph_name}')"

        cursor.execute(insert_sql_syntax)
        database_connection.commit()

        # get the id of new graph
        sql_select = f"SELECT graph.id FROM graph WHERE graph.name = '{graph_name}';"
        cursor.execute(sql_select)
        database_connection.commit()
        list_graph_id = cursor.fetchone()
        last_graph_id = list_graph_id[0]

        # update graph
        graph_updated_name = 'Updated Name Graph'
        update_graph_repository.update_graph(last_graph_id, graph_updated_name)
        database_connection.commit()

        # select updated graph
        sql_select = f"SELECT graph.name FROM graph WHERE graph.id = '{last_graph_id}';"
        cursor.execute(sql_select)
        database_connection.commit()
        values_existing_graph = cursor.fetchall()

        # assert
        self.assertEqual(values_existing_graph, [(graph_updated_name,)])
        database_connection.close()

    def test_delete_graph(self):
        # prepare
        delete_graph_repository = GraphRepository()
        database_connection = sqlite3.connect(delete_graph_repository.path)
        cursor = database_connection.cursor()

        # act

        # insert new_graph
        graph_name = 'To be deleted Graph'
        insert_sql_syntax = f"INSERT OR IGNORE INTO graph (name) " \
                            f"VALUES ('{graph_name}')"
        cursor.execute(insert_sql_syntax)
        database_connection.commit()

        # get id of new graph
        sql_select = f"SELECT graph.id FROM graph WHERE graph.name = '{graph_name}';"
        cursor.execute(sql_select)
        database_connection.commit()
        new_graph_id = cursor.fetchone()[0]

        # delete new_graph
        delete_graph_repository.delete_graph(new_graph_id)

        # select new_graph
        sql_query = f"SELECT * FROM graph WHERE graph.id = '{new_graph_id}';"
        cursor.execute(sql_query)
        database_connection.commit()
        values_existing_graph = cursor.fetchall()

        # assert
        self.assertEqual(values_existing_graph, [])
        database_connection.close()
