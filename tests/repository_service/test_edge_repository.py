from repository_service.edge_repository import EdgeRepository
from tests.repository_service.test_base_repository import PrepareDatabase
from unittest import TestCase
import sqlite3


class TestEdgeRepository(TestCase):

    def __init__(self, *args, **kwargs):
        self.path = 'test_database.db'
        self.edge_repository = EdgeRepository(self.path)
        self.test_database_connection = sqlite3.connect(self.path)
        self.test_cursor = self.test_database_connection.cursor()
        self.database_preparation = PrepareDatabase(self.test_database_connection, self.test_cursor)
        super().__init__(*args, **kwargs)

    def delete_values_from_database(self):
        self.database_preparation.delete_graph_values()
        self.database_preparation.delete_node_values()
        self.database_preparation.delete_edge_values()

    def test_insert_edge(self):
        try:
            # prepare
            self.delete_values_from_database()

            # act
            # insert_graph new graph
            graph_name = 'Gaga'
            self.database_preparation.insert_graph(graph_name)

            # get id of graph
            graph_id = self.database_preparation.get_graph_id(graph_name)

            # insert_graph 2 nodes
            node_start_name = 'L'
            start_node_x_coord = 123
            start_node_y_coord = 234
            self.database_preparation.insert_node(node_start_name, start_node_x_coord, start_node_y_coord, graph_id)

            node_end_name = 'G'
            end_node_x_coord = 323
            end_node_y_coord = 298
            self.database_preparation.insert_node(node_end_name, end_node_x_coord, end_node_y_coord, graph_id)

            # get id of nodes
            node_start_id = self.database_preparation.get_node_id(node_start_name, start_node_x_coord, start_node_y_coord, graph_id)
            node_end_id = self.database_preparation.get_node_id(node_end_name, end_node_x_coord, end_node_y_coord, graph_id)

            # insert_graph new_edge via edge_repository
            edge_name = 'LG'
            edge_cost = 34
            edge_id_from_repository = self.edge_repository.insert_edge(edge_name, edge_cost, node_start_id,
                                                                       node_end_id, graph_id)
            self.edge_repository.close_connection()

            # manually get id of new edge
            edge_id = self.database_preparation.get_edge_id(edge_name, edge_cost, node_start_id, node_end_id, graph_id)

            # assert
            self.assertEqual(edge_id_from_repository, edge_id)
        finally:
            self.test_database_connection.close()

    def test_get_edge(self):
        try:
            # prepare
            self.delete_values_from_database()

            # act
            # insert_graph
            graph_name = 'Mimo'
            self.database_preparation.insert_graph(graph_name)

            # get id of graph
            graph_id = self.database_preparation.get_graph_id(graph_name)

            # insert_graph 2 nodes
            node_start_name = 'K'
            node_start_x_coord = 345
            node_start_y_coord = 291
            self.database_preparation.insert_node(node_start_name, node_start_x_coord, node_start_y_coord, graph_id)

            node_end_name = 'A'
            node_end_x_coord = 345
            node_end_y_coord = 291
            self.database_preparation.insert_node(node_end_name, node_end_x_coord, node_end_y_coord, graph_id)

            # get id of nodes
            node_start_id = self.database_preparation.get_node_id(node_start_name, node_start_x_coord, node_start_y_coord, graph_id)
            node_end_id = self.database_preparation.get_node_id(node_end_name, node_end_x_coord, node_end_y_coord, graph_id)

            # insert new_edge
            edge_name = 'KA'
            edge_cost = 49
            self.database_preparation.insert_edge(edge_name, edge_cost, node_start_id, node_end_id, graph_id)

            # manually get id of new edge
            edge_id = self.database_preparation.get_edge_id(edge_name, edge_cost, node_start_id, node_end_id, graph_id)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            edge_values = (edge_id, edge_name, edge_cost, node_start_id, node_end_id, graph_id)
=======
            edge_values = (edge_id, edge_name, edge_cost, node_start_id, node_end_id, graph_id, )
>>>>>>> add_line_widget
=======
            edge_values = (edge_id, edge_name, edge_cost, node_start_id, node_end_id, graph_id, )
>>>>>>> add_line_widget
=======
            edge_values = (edge_id, edge_name, edge_cost, node_start_id, node_end_id, graph_id, )
>>>>>>> add_line_widget
=======
            edge_values = (edge_id, edge_name, edge_cost, node_start_id, node_end_id, graph_id, )
>>>>>>> add_line_widget
=======
            edge_values = (edge_id, edge_name, edge_cost, node_start_id, node_end_id, graph_id)
>>>>>>> 965f01744ac4d658480afd0395435f9a50eabf45

            # get values of edge via edge_repository
            edge_values_from_repository = self.edge_repository.get_edge_values(edge_id)[0]
            self.edge_repository.close_connection()

            # assert
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            for index in range(len(edge_values_from_repository)):
                self.assertEqual(edge_values_from_repository[index], edge_values[index])
=======
            for value_index in range(len(edge_values_from_repository)):
                self.assertEqual(edge_values_from_repository[value_index], edge_values[value_index])
>>>>>>> add_line_widget
=======
            for value_index in range(len(edge_values_from_repository)):
                self.assertEqual(edge_values_from_repository[value_index], edge_values[value_index])
>>>>>>> add_line_widget
=======
            for value_index in range(len(edge_values_from_repository)):
                self.assertEqual(edge_values_from_repository[value_index], edge_values[value_index])
>>>>>>> add_line_widget
=======
            for value_index in range(len(edge_values_from_repository)):
                self.assertEqual(edge_values_from_repository[value_index], edge_values[value_index])
>>>>>>> add_line_widget
=======
            for index in range(len(edge_values_from_repository)):
                self.assertEqual(edge_values_from_repository[index], edge_values[index])
>>>>>>> 965f01744ac4d658480afd0395435f9a50eabf45
        finally:
            self.test_database_connection.close()

    def test_get_edge_nodes(self):
        try:
            # prepare
            self.delete_values_from_database()

            # act
            # insert_graph new graph
            graph_name = 'Cara'
            self.database_preparation.insert_graph(graph_name)

            # get id of graph
            graph_id = self.database_preparation.get_graph_id(graph_name)

            # insert_graph 2 nodes
            node_start_name = 'P'
            node_start_x_coord = 345
            node_start_y_coord = 291
            self.database_preparation.insert_node(node_start_name, node_start_x_coord, node_start_y_coord, graph_id)

            node_end_name = 'E'
            node_end_x_coord = 345
            node_end_y_coord = 291
            self.database_preparation.insert_node(node_end_name, node_end_x_coord, node_end_y_coord, graph_id)

            # get id of nodes
            node_start_id = self.database_preparation.get_node_id(node_start_name, node_start_x_coord, node_start_y_coord, graph_id)
            node_end_id = self.database_preparation.get_node_id(node_end_name, node_end_x_coord, node_end_y_coord, graph_id)

            # insert new edge
            edge_name = 'PE'
            edge_cost = 56
            self.database_preparation.insert_edge(edge_name, edge_cost, node_start_id, node_end_id, graph_id)

            # get edge_ id
            edge_id = self.database_preparation.get_edge_id(edge_name, edge_cost, node_start_id, node_end_id, graph_id)
            edge_values = (edge_id, edge_name, edge_cost, node_start_id, node_end_id, graph_id)

            # get edges of nodes from edge_repository
            node_edge_values_from_repository = self.edge_repository.get_node_edges(node_start_id)[0]
            self.edge_repository.close_connection()

            # assert
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            for index in range(len(node_edge_values_from_repository)):
                self.assertEqual(node_edge_values_from_repository[index], edge_values[index])
=======
            for value_index in range(len(node_edge_values_from_repository)):
                self.assertEqual(node_edge_values_from_repository[value_index], edge_values[value_index])
>>>>>>> add_line_widget
=======
            for value_index in range(len(node_edge_values_from_repository)):
                self.assertEqual(node_edge_values_from_repository[value_index], edge_values[value_index])
>>>>>>> add_line_widget
=======
            for value_index in range(len(node_edge_values_from_repository)):
                self.assertEqual(node_edge_values_from_repository[value_index], edge_values[value_index])
>>>>>>> add_line_widget
=======
            for value_index in range(len(node_edge_values_from_repository)):
                self.assertEqual(node_edge_values_from_repository[value_index], edge_values[value_index])
>>>>>>> add_line_widget
=======
            for index in range(len(node_edge_values_from_repository)):
                self.assertEqual(node_edge_values_from_repository[index], edge_values[index])
>>>>>>> 965f01744ac4d658480afd0395435f9a50eabf45
        finally:
            self.test_database_connection.close()

    def test_get_graph_edges(self):
        try:
            # prepare
            self.delete_values_from_database()

            # act
            # insert_graph new graph
            graph_name = 'Mara'
            self.database_preparation.insert_graph(graph_name)

            # get id of graph
            graph_id = self.database_preparation.get_graph_id(graph_name)

            # insert_graph 2 nodes
            node_start_name = 'S'
            node_start_x_coord = 399
            node_start_y_coord = 299
            self.database_preparation.insert_node(node_start_name, node_start_x_coord, node_start_y_coord, graph_id)

            node_end_name = 'E'
            node_end_x_coord = 321
            node_end_y_coord = 221
            self.database_preparation.insert_node(node_end_name, node_end_x_coord, node_end_y_coord, graph_id)

            # get id of nodes
            node_start_id = self.database_preparation.get_node_id(node_start_name, node_start_x_coord,
                                                                  node_start_y_coord, graph_id)
            node_end_id = self.database_preparation.get_node_id(node_end_name, node_end_x_coord, node_end_y_coord,
                                                                graph_id)

            # insert new edge
            edge_name = 'SE'
            edge_cost = 56
            self.database_preparation.insert_edge(edge_name, edge_cost, node_start_id, node_end_id, graph_id)

            # get edge_ id
            edge_id = self.database_preparation.get_edge_id(edge_name, edge_cost, node_start_id, node_end_id, graph_id)
            edge_values = (edge_id, edge_name, edge_cost, node_start_id, node_end_id, graph_id)

            # get edges of graph from edge_repository
            graph_edge_values_from_repository = self.edge_repository.get_graph_edges(graph_id)[0]
            self.edge_repository.close_connection()

            # assert
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            for index in range(len(graph_edge_values_from_repository)):
                self.assertEqual(graph_edge_values_from_repository[index], edge_values[index])
=======
            for value_index in range(len(graph_edge_values_from_repository)):
                self.assertEqual(graph_edge_values_from_repository[value_index], edge_values[value_index])
>>>>>>> add_line_widget
=======
            for value_index in range(len(graph_edge_values_from_repository)):
                self.assertEqual(graph_edge_values_from_repository[value_index], edge_values[value_index])
>>>>>>> add_line_widget
=======
            for value_index in range(len(graph_edge_values_from_repository)):
                self.assertEqual(graph_edge_values_from_repository[value_index], edge_values[value_index])
>>>>>>> add_line_widget
=======
            for value_index in range(len(graph_edge_values_from_repository)):
                self.assertEqual(graph_edge_values_from_repository[value_index], edge_values[value_index])
>>>>>>> add_line_widget
=======
            for index in range(len(graph_edge_values_from_repository)):
                self.assertEqual(graph_edge_values_from_repository[index], edge_values[index])
>>>>>>> 965f01744ac4d658480afd0395435f9a50eabf45
        finally:
            self.test_database_connection.close()

    def test_update_edge(self):
        try:
            # prepare
            self.delete_values_from_database()

            # act
            # insert_graph new graph
            graph_name = 'Mera'
            self.database_preparation.insert_graph(graph_name)

            # get id of graph
            graph_id = self.database_preparation.get_graph_id(graph_name)

            # insert_graph 2 nodes
            node_start_name = 'V'
            node_start_x_coord = 345
            node_start_y_coord = 291
            self.database_preparation.insert_node(node_start_name, node_start_x_coord, node_start_y_coord, graph_id)

            node_end_name = 'S'
            node_end_x_coord = 345
            node_end_y_coord = 291
            self.database_preparation.insert_node(node_end_name, node_end_x_coord, node_end_y_coord, graph_id)

            # get id of nodes
            node_start_id = self.database_preparation.get_node_id(node_start_name, node_start_x_coord, node_start_y_coord, graph_id)
            node_end_id = self.database_preparation.get_node_id(node_end_name, node_end_x_coord, node_end_y_coord, graph_id)

            # insert_graph new edge
            edge_name = 'VS'
            edge_cost = 2
            self.database_preparation.insert_edge(edge_name, edge_cost, node_start_id, node_end_id, graph_id)

            # manually get id of new edge
            edge_id = self.database_preparation.get_edge_id(edge_name, edge_cost, node_start_id, node_end_id, graph_id)

            # update edge via edge_repository
            new_edge_cost = 36
            self.edge_repository.update_edge(edge_id, edge_name, new_edge_cost, node_start_id, node_end_id, graph_id)
            self.edge_repository.close_connection()

            # get updated_cost of edge
            sql_get_edge_updated_cost = f"SELECT cost FROM edge WHERE id = '{edge_id}' AND name = '{edge_name}' AND " \
                f"start_node_id = '{node_start_id}' AND end_node_id = '{node_end_id}' AND graph_id = '{graph_id}';"
            self.test_cursor.execute(sql_get_edge_updated_cost)
            self.test_database_connection.commit()
            updated_edge_cost = self.test_cursor.fetchall()[0][0]

            # assert
            self.assertEqual(updated_edge_cost, new_edge_cost)
        finally:
            self.test_database_connection.close()

    def test_delete_edge(self):
        try:
            # prepare
            self.delete_values_from_database()

            # act
            # insert_graph new graph
            graph_name = 'Tare'
            self.database_preparation.insert_graph(graph_name)

            # get id of graph
            graph_id = self.database_preparation.get_graph_id(graph_name)

            # insert_graph 2 nodes
            node_start_name = 'G'
            node_start_x_coord = 345
            node_start_y_coord = 291
            self.database_preparation.insert_node(node_start_name, node_start_x_coord, node_start_y_coord, graph_id)

            node_end_name = 'M'
            node_end_x_coord = 345
            node_end_y_coord = 291
            self.database_preparation.insert_node(node_end_name, node_end_x_coord, node_end_y_coord, graph_id)

            # get id of nodes
            node_start_id = self.database_preparation.get_node_id(node_start_name, node_start_x_coord, node_start_y_coord, graph_id)
            node_end_id = self.database_preparation.get_node_id(node_end_name, node_end_x_coord, node_end_y_coord, graph_id)

            # insert new edge
            edge_name = 'GM'
            edge_cost = 29
            self.database_preparation.insert_edge(edge_name, edge_cost, node_start_id, node_end_id, graph_id)

            # manually get id of new edge
            edge_id = self.database_preparation.get_edge_id(edge_name, edge_cost, node_start_id, node_end_id, graph_id)

            # delete edge from edge_repository
            self.edge_repository.delete_edge(edge_id)
            self.edge_repository.close_connection()

            # manually check if edge is deleted
            sql_statement_edge_id = f"SELECT id FROM edge WHERE name = '{edge_name}' AND cost = '{edge_cost}' AND " \
                                    f"start_node_id = '{node_start_id}' AND end_node_id = '{node_end_id}' AND graph_id = '{graph_id}';"
            self.test_cursor.execute(sql_statement_edge_id)
            self.test_database_connection.commit()
            deleted_edge_id = self.test_cursor.fetchall()

            # assert
            self.assertEqual(deleted_edge_id, [])
        finally:
            self.test_database_connection.close()
