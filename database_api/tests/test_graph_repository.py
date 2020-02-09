import unittest
from database_api.graph_repository import GraphRepository
from database_api.base_repository import BaseRepository


class TestGraphRepository(unittest.TestCase):

    def test_insert_graph_repository(self):

        # prepare
        insert_to_graph_repository = GraphRepository()
        cursor = insert_to_graph_repository.cursor

        # act
        graph_name = 'XcV4 Graph'
        insert_to_graph_repository.insert(graph_name)

        sql_select = f"SELECT graph.id, graph.name FROM graph WHERE graph.name = '{graph_name}';"
        cursor.execute(sql_select)
        values_existing_graph = cursor.fetchall()

        # assert
        self.assertEqual(values_existing_graph[0][1], graph_name)
        insert_to_graph_repository.close_database()

    def test_get_graph(self):

        # prepare
        get_graph_repository = GraphRepository()
        cursor = get_graph_repository.cursor

        # act
        graph_id = 2
        graph_name = get_graph_repository.get_graph(graph_id)

        sql_select = f"SELECT graph.id, graph.name FROM graph WHERE graph.id = '{graph_id}';"
        cursor.execute(sql_select)
        values_existing_graph = cursor.fetchall()

        # assert
        self.assertEqual(values_existing_graph, graph_name)
        get_graph_repository.close_database()

        """# insert 'First_Graph'
        cursor.execute()
        fetched_inserted_values = cursor.fetchall()


        # get graph values
        cursor.execute(local_graph_repository.get_graph(1))
        fetched_selected_values_1 = cursor.fetchall()
        self.assertEqual(fetched_selected_values_1, [(1, 'Test_Graph1')])

        # insert 'Elena_Graph'
        cursor.execute(local_graph_repository.insert(12, 'Elena_Graph'))
        fetched_inserted_values_1 = cursor.fetchall()
        self.assertEqual(fetched_inserted_values_1, [])

        # update graph values
        cursor.execute(local_graph_repository.update_graph(12, 'Elena_Graph'))
        fetched_update_values_2 = cursor.fetchall()
        self.assertEqual(fetched_update_values_2, [])

        # get graph values
        cursor.execute(local_graph_repository.get_graph(12))
        fetched_selected_values_2 = cursor.fetchall()
        self.assertEqual(fetched_selected_values_2, [(12, 'Elena_Graph')])

        # get graph nodes
        cursor.execute(local_graph_repository.get_graph_nodes(1))
        fetched_selected_values_3 = cursor.fetchall()
        self.assertEqual(fetched_selected_values_3, [(1, 1, 'a'), (1, 2, 'b'), (1, 3, 'c'), (1, 4, 'd'), (1, 5, 'e')])

        # update graph values
        cursor.execute(local_graph_repository.update_graph(12, 'Test_Graph9'))
        fetched_update_values_2 = cursor.fetchall()
        self.assertEqual(fetched_update_values_2, [])

        # get graph values
        cursor.execute(local_graph_repository.get_graph(12))
        fetched_selected_values_3 = cursor.fetchall()
        self.assertEqual(fetched_selected_values_3, [(12, 'Test_Graph9')])

        # delete values
        cursor.execute(local_graph_repository.delete_graph(5))
        fetched_deleted_values = cursor.fetchall()
        self.assertEqual(fetched_deleted_values, [])

        # get graph values
        cursor.execute(local_graph_repository.get_graph(5))
        fetched_selected_values_4 = cursor.fetchall()
        self.assertIsNot(fetched_selected_values_4, [(5, 'Test_Graph9')])

        commit_and_close_database(conn)


class TestGraphRepository(unittest.TestCase):

    def test_graph_repository_insert(self):
     # prepare
     graph_repository = GraphRepository()
     connection = sqlite3.connect('E:\\PYTHON\\code\\GraphProject\\SQL\\graph.db')
     cursor = connection.cursor()
     graph_name = 'Ionut_Graph'

    # act
    graph_id = graph_repository.insert(graph_name)

    #assert
    sql_select = f"SELECT graph.id, graph.name FROM graph WHERE graph.id = '{graph_id}';"
    existing_graph = cursor.execute(sql_select)
    self.assertEqual(existing_graph[0], graph_id)
    self.assertEqual(existing_graph[1], graph_name)"""

