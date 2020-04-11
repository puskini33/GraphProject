from tests.business_service.repository_mock.graph_repository_mock import GraphRepositoryMock
from models.graph_model import GraphModel
import unittest
from business_service.graph_business_service import GraphBusinessService


class TestGraphBusinessService(unittest.TestCase):

    def test_insert_graph(self):
        # prepare
        graph_repository_mock = GraphRepositoryMock()
        graph_model = GraphModel()
        graph_model.graph_name = graph_repository_mock.mock_graph_name1

        graph_business_service = GraphBusinessService(graph_repository_mock)

        # act
        result_graph_model = graph_business_service.insert_graph(graph_model)

        # assert
        # assert id of object is the same
        self.assertEqual(result_graph_model.graph_id, graph_repository_mock.mock_graph_id1)

        # assert it is the same object/ instance of class
        self.assertEqual(result_graph_model, graph_model)

        # assert name of object is same
        self.assertEqual(result_graph_model.graph_name, graph_repository_mock.mock_graph_name1)

    def test_get_graph_model(self):
        # prepare
        graph_repository_mock = GraphRepositoryMock()
        graph_business_service = GraphBusinessService(graph_repository_mock)

        # act
        result_graph_model = graph_business_service.get_graph_model(graph_repository_mock.mock_graph_id1)

        # assert
        # assert name of object is the same
        self.assertEqual(result_graph_model.graph_name, graph_repository_mock.mock_graph_name1)

        # assert id is the same
        self.assertEqual(result_graph_model.graph_id, graph_repository_mock.mock_graph_id1)

        # assert type graph_model
        self.assertEqual(type(result_graph_model), GraphModel)

    def test_get_all_graph_models(self):
        # prepare
        graph_repository_mock = GraphRepositoryMock()
        graph_business_service = GraphBusinessService(graph_repository_mock)

        # act
        result_graph_model = graph_business_service.get_all_graph_models()

        # assert
        # assert name of object is the same
        self.assertEqual(result_graph_model[0].graph_name, graph_repository_mock.mock_graph_name1)
        self.assertEqual(result_graph_model[1].graph_name, graph_repository_mock.mock_graph_name2)

        # assert id is the same
        self.assertEqual(result_graph_model[0].graph_id, graph_repository_mock.mock_graph_id1)
        self.assertEqual(result_graph_model[1].graph_id, graph_repository_mock.mock_graph_id2)

        # assert type graph_model
        self.assertEqual(type(result_graph_model[0]), GraphModel)

    def test_update_graph(self):
        # prepare
        graph_repository_mock = GraphRepositoryMock()
        graph_business_service = GraphBusinessService(graph_repository_mock)
        graph_model = GraphModel()
        graph_model.graph_id = graph_repository_mock.mock_graph_id1
        graph_model.graph_name = graph_repository_mock.mock_updated_graph_name1

        # act
        result_graph_model = graph_business_service.update_graph(graph_model)

        # assert type graph_model
        self.assertEqual(type(result_graph_model), GraphModel)

        # assert name of object is the same
        self.assertEqual(result_graph_model.graph_name, graph_repository_mock.mock_updated_graph_name1)

        # assert id is the same
        self.assertEqual(result_graph_model.graph_id, graph_repository_mock.mock_graph_id1)


if __name__ == '__main__':
    unittest.main()