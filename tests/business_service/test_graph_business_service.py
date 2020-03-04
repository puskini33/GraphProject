from tests.business_service.graph_repository_mock.graph_repository_mock import GraphRepositoryMock
from models.graph_model import GraphModel
import unittest
import pytest
from business_service.graph_business_service import GraphBusinessService


class TestGraphBusinessService(unittest.TestCase):

    def test_insert_graph(self):
        # prepare
        graph_name = 'GraphName1'
        graph_model = GraphModel()
        graph_model.graph_name = graph_name

        self.graph_repository = GraphRepositoryMock()
        graph_business_service = GraphBusinessService(self.graph_repository)

        # act
        business_service_graph_id = graph_business_service.insert_graph(graph_model)

        graph_id = 0
        graph_model.graph_id = graph_id

        # assert
        self.assertEqual(business_service_graph_id, graph_model)

    def test_get_graph_model(self):
        # prepare
        graph_id = 0


        self.graph_repository = GraphRepositoryMock()
        graph_business_service = GraphBusinessService(self.graph_repository)
        # act

        # assert


if __name__ == '__main__':
    unittest.main()