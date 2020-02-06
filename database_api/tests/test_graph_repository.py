import unittest
from database_api.graph_repository import GraphRepository
from database_api.connect_to_database import db_connect, create_cursor
from database_api.close_database import commit_and_close_database


class TestGraphRepository(unittest.TestCase):

    def test_get_graph(self, graph_repository, c):

        c.execute(graph_repository.get_graph(1))
        fetched_inserted_values = c.fetchall()

        self.assertEqual(fetched_inserted_values, [(1, 'Test_Graph1')])

        c.execute(graph_repository.get_graph(5))
        fetched_inserted_values = c.fetchall()
        self.assertEqual(fetched_inserted_values, [(5, 'Elena_Graph')])

    def test_insert(self, graph_repository, c):
        c.execute(graph_repository.insert('First_Graph'))
        fetched_inserted_values = c.fetchall()

        self.assertEqual(fetched_inserted_values, [])

    def test_get_graph_nodes(self):
        pass


if __name__ == '__main__':
    local_graph_repository = GraphRepository()
    conn = db_connect('E:\\PYTHON\\code\\GraphProject\\SQL\\graph.db')
    cursor = create_cursor(conn)
    test_graph = TestGraphRepository()
    test_graph.test_insert(local_graph_repository, cursor)
