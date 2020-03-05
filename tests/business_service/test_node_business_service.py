from business_service.node_business_service import NodeBusinessService
from tests.business_service.repository_mock.node_repository_mock import NodeRepositoryMock
from models.node_model import NodeModel
import unittest
import pytest


class TestNodeBusinessService(unittest.TestCase):

    def test_insert_node(self):
        # prepare
        node_repository_mock = NodeRepositoryMock()
        node_business_service = NodeBusinessService(node_repository_mock)
        node_model = NodeModel()

        node_model.node_name = node_repository_mock.node_name_0
        node_model.graph_id = node_repository_mock.graph_id
        node_model.x_coord = node_repository_mock.x_coord_0
        node_model.y_coord = node_repository_mock.y_coord_0

        # act
        result_node_model = node_business_service.insert_node(node_model)

        # assert node id the same
        self.assertEqual(result_node_model.node_id, node_repository_mock.node_id_0)

        # assert it is the same node_model instance
        self.assertEqual(result_node_model, node_model)

        # assert it is the same graph_id
        self.assertEqual(result_node_model.graph_id, node_repository_mock.graph_id)

        # assert is is the same x_coord_1
        self.assertEqual(result_node_model.x_coord, node_repository_mock.x_coord_0)

    def test_get_node_model(self):
        # prepare
        node_repository_mock = NodeRepositoryMock()
        node_business_service = NodeBusinessService(node_repository_mock)

        # act
        result_node_model = node_business_service.get_node_model(node_repository_mock.node_id_0)

        # assert type is node_model
        self.assertEqual(type(result_node_model), NodeModel)

        # assert node id the same
        self.assertEqual(result_node_model.node_id, node_repository_mock.node_id_0)

    def test_get_node_models(self):
        # prepare
        node_repository_mock = NodeRepositoryMock()
        node_business_service = NodeBusinessService(node_repository_mock)

        # act
        result_list_node_models = node_business_service.get_node_models(node_repository_mock.graph_id)

        # assert type is node_model
        for element in result_list_node_models:
            self.assertEqual(type(element), NodeModel)

        # assert same graph_id
        self.assertEqual(result_list_node_models[0].graph_id, node_repository_mock.graph_id)
        self.assertEqual(result_list_node_models[1].graph_id, node_repository_mock.graph_id)

    def test_update_node(self):
        # prepare
        node_repository_mock = NodeRepositoryMock()
        node_business_service = NodeBusinessService(node_repository_mock)
        node_model = NodeModel()

        node_model.node_id = node_repository_mock.node_id_0
        node_model.node_name = node_repository_mock.node_updated_name_0
        node_model.graph_id = node_repository_mock.graph_id
        node_model.x_coord = node_repository_mock.updated_x_coord_0
        node_model.y_coord = node_repository_mock.updated_y_coord_0

        # act
        result_node_model = node_business_service.update_node(node_model)

        # assert same node model instance
        self.assertEqual(result_node_model, node_model)

        # assert node_id is same
        self.assertEqual(result_node_model.node_id, node_repository_mock.node_id_0)

        # assert name is same
        self.assertEqual(result_node_model.node_name, node_repository_mock.node_updated_name_0)



