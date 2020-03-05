from tests.business_service.graph_repository_mock.graph_repository_mock import GraphRepositoryMock
from models.graph_model import GraphModel
import unittest
import pytest
from business_service.graph_business_service import GraphBusinessService


class TestGraphBusinessService(unittest.TestCase):

    def test_insert_graph(self):
        # prepare
        graph_repository_mock = GraphRepositoryMock()
        graph_model = GraphModel()
        graph_model.graph_name = graph_repository_mock.mock_graph_name

        graph_business_service = GraphBusinessService(graph_repository_mock)

        # act
        result_graph_model = graph_business_service.insert_graph(graph_model)

        # assert
        # assert id of object is the same
        self.assertEqual(result_graph_model.graph_id, graph_repository_mock.mock_graph_id)

        # assert it is the same object/ instance of class
        self.assertEqual(result_graph_model, graph_model)

        # assert name of object is same
        self.assertEqual(result_graph_model.graph_name, graph_repository_mock.mock_graph_name)

    def test_get_graph_model(self):
        # prepare
        graph_repository_mock = GraphRepositoryMock()
        graph_business_service = GraphBusinessService(graph_repository_mock)

        # act
        result_graph_model = graph_business_service.get_graph_model(graph_repository_mock.mock_graph_id)

        # assert
        # assert name of object is the same
        self.assertEqual(result_graph_model.graph_name, graph_repository_mock.mock_graph_name)

        # assert id is the same
        self.assertEqual(result_graph_model.graph_id, graph_repository_mock.mock_graph_id)

        # assert type graph_model
        self.assertEqual(type(result_graph_model), GraphModel)

    def test_update_graph(self):
        # prepare
        graph_repository_mock = GraphRepositoryMock()
        graph_business_service = GraphBusinessService(graph_repository_mock)
        graph_model = GraphModel()
        graph_model.graph_id = graph_repository_mock.mock_graph_id
        graph_model.graph_name = graph_repository_mock.mock_updated_graph_name

        # act
        result_graph_model = graph_business_service.update_graph(graph_model)

        # assert type graph_model
        self.assertEqual(type(result_graph_model), GraphModel)

        # assert name of object is the same
        self.assertEqual(result_graph_model.graph_name, graph_repository_mock.mock_updated_graph_name)

        # assert id is the same
        self.assertEqual(result_graph_model.graph_id, graph_repository_mock.mock_graph_id)


if __name__ == '__main__':
    unittest.main()