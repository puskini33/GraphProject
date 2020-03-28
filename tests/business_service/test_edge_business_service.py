from models.edge_model import EdgeModel
from tests.business_service.repository_mock.edge_repository_mock import EdgeRepositoryMock
from business_service.edge_business_service import EdgeBusinessService
import unittest


class TestEdgeBusinessService(unittest.TestCase):

    def verify_properties_of_first_edge(self, edge_model: EdgeModel, edge_repository_mock: EdgeRepositoryMock):
        self.assertEqual(edge_model.edge_id, edge_repository_mock.first_edge_id)
        self.assertEqual(edge_model.edge_name, edge_repository_mock.first_edge_name)
        self.assertEqual(edge_model.edge_cost, edge_repository_mock.first_edge_cost)
        self.assertEqual(edge_model.start_node_id, edge_repository_mock.first_start_node_id)
        self.assertEqual(edge_model.end_node_id, edge_repository_mock.first_end_node_id)
        self.assertEqual(edge_model.graph_id, edge_repository_mock.graph_id)

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

    def test_get_edge_models_of_node(self):
        # prepare
        edge_repository_mock = EdgeRepositoryMock()
        edge_business_service = EdgeBusinessService(edge_repository_mock)

        # act
        result_list_of_edge_models = edge_business_service.get_edge_models_of_node(edge_repository_mock.first_end_node_id)

        # assert type of elements is EdgeModel
        for element in result_list_of_edge_models:
            self.assertEqual(type(element), EdgeModel)

        # assert values of edge_model_properties are correct
        self.verify_properties_of_first_edge(result_list_of_edge_models[0], edge_repository_mock)

        self.assertEqual(result_list_of_edge_models[1].edge_id, edge_repository_mock.second_edge_id)
        self.assertEqual(result_list_of_edge_models[1].edge_name, edge_repository_mock.second_edge_name)
        self.assertEqual(result_list_of_edge_models[1].edge_cost, edge_repository_mock.second_edge_cost)
        self.assertEqual(result_list_of_edge_models[1].start_node_id, edge_repository_mock.second_start_node_id)
        self.assertEqual(result_list_of_edge_models[1].end_node_id, edge_repository_mock.first_end_node_id)
        self.assertEqual(result_list_of_edge_models[1].graph_id, edge_repository_mock.graph_id)

    def test_get_edge_models_of_graph(self):
        # prepare
        edge_repository_mock = EdgeRepositoryMock()
        edge_business_service = EdgeBusinessService(edge_repository_mock)

        # act
        result_list_of_edge_models = edge_business_service.get_edge_models_of_graph(
            edge_repository_mock.graph_id)

        # assert type of elements is EdgeModel
        for element in result_list_of_edge_models:
            self.assertEqual(type(element), EdgeModel)

        # assert values of edge_model_properties are correct
        self.verify_properties_of_first_edge(result_list_of_edge_models[0], edge_repository_mock)

        self.assertEqual(result_list_of_edge_models[1].edge_id, edge_repository_mock.second_edge_id)
        self.assertEqual(result_list_of_edge_models[1].edge_name, edge_repository_mock.second_edge_name)
        self.assertEqual(result_list_of_edge_models[1].edge_cost, edge_repository_mock.second_edge_cost)
        self.assertEqual(result_list_of_edge_models[1].start_node_id, edge_repository_mock.second_start_node_id)
        self.assertEqual(result_list_of_edge_models[1].end_node_id, edge_repository_mock.first_end_node_id)
        self.assertEqual(result_list_of_edge_models[1].graph_id, edge_repository_mock.graph_id)

    def test_update_edge(self):
        # prepare
        edge_repository_mock = EdgeRepositoryMock()
        edge_business_service = EdgeBusinessService(edge_repository_mock)
        edge_model = EdgeModel()

        updated_edge_name = 'UpdatedEdgeName'
        updated_edge_cost = 31
        updated_start_node_id = 9

        edge_model.edge_name = updated_edge_name
        edge_model.edge_cost = updated_edge_cost
        edge_model.start_node_id = updated_start_node_id
        edge_model.edge_id = edge_repository_mock.first_edge_id
        edge_model.end_node_id = edge_repository_mock.first_end_node_id
        edge_model.graph_id = edge_repository_mock.graph_id

        # act
        resulted_edge_model = edge_business_service.update_edge(edge_model)

        # assert returned type is GraphModel
        self.assertEqual(type(resulted_edge_model), EdgeModel)

        # assert same instance of node_model is returned
        self.assertEqual(resulted_edge_model, edge_model)

        # assert updated properties did not change
        self.assertEqual(resulted_edge_model.edge_name, updated_edge_name)
        self.assertEqual(resulted_edge_model.edge_cost, updated_edge_cost)
        self.assertEqual(resulted_edge_model.start_node_id, updated_start_node_id)
