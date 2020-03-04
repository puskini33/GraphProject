from tests.business_service.graph_repository_mock.graph_repository_mock import GraphRepositoryMock
from models.graph_model import GraphModel
import unittest
import pytest
from business_service.graph_business_service import GraphBusinessService


class TestGraphBusinessService(unittest.TestCase):

    def test_insert_graph(self):
        # prepare
        graph_repository_mock = GraphRepositoryMock()
        graph_name = 'GraphName1'
        graph_model = GraphModel()
        graph_model.graph_name = graph_name

        graph_business_service = GraphBusinessService(graph_repository_mock)

        # act
        result_graph_model = graph_business_service.insert_graph(graph_model)

        # assert

        self.assertEqual(result_graph_model.graph_id, graph_repository_mock.inserted_graph_id)

        # assert it is the same object/ instance of class
        self.assertEqual(result_graph_model, graph_model)

        # assert name of object is same
        self.assertEqual(result_graph_model.graph_name, graph_name)

    


if __name__ == '__main__':
    unittest.main()