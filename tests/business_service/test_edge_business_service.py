from models.edge_model import EdgeModel
from tests.business_service.repository_mock.edge_repository_mock import EdgeRepositoryMock
from business_service.edge_business_service import EdgeBusinessService
import unittest
import pytest


class TestEdgeBusinessService(unittest.TestCase):

    def test_insert_edge(self):
        # prepare
        edge_repository_mock = EdgeRepositoryMock()
        edge_business_service = EdgeBusinessService(edge_repository_mock)
        edge_model = EdgeModel()

        edge_name = 'TestEdgeName0'
        edge_cost = 13
        start_node_id = 3
        end_node_id = 5
        graph_id = 1

        edge_model.edge_name = edge_name
        edge_model.edge_cost = edge_cost
        edge_model.start_node_id = start_node_id
        edge_model.end_node_id = end_node_id
        edge_model.graph_id = graph_id

        # act
        result_edge_model = edge_business_service.insert_edge(edge_model)

        # assert edge_model is returned
        self.assertEqual(type(result_edge_model), EdgeModel)

        # assert id is the same
        self.assertEqual(result_edge_model.edge_id, edge_repository_mock.first_edge_id)

    def test_get_edge_model(self):
        # prepare
        edge_repository_mock = EdgeRepositoryMock()
        edge_business_service = EdgeBusinessService(edge_repository_mock)

        # act
        result_edge_model = edge_business_service.get_edge_model(edge_repository_mock.first_edge_id)

        # assert resulted object is of EdgeModel type
        self.assertEqual(type(result_edge_model), EdgeModel)

        # assert edge_id is the same
        self.assertEqual(result_edge_model.edge_id, edge_repository_mock.first_edge_id)

        # assert name is the same
        self.assertEqual(result_edge_model.edge_name, edge_repository_mock.first_edge_name)
