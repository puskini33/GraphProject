from business_service.node_business_service import NodeBusinessService
from tests.business_service.repository_mock.node_repository_mock import NodeRepositoryMock
from models.node_model import NodeModel
import unittest


class TestNodeBusinessService(unittest.TestCase):

    def verify_properties_of_first_node_model(self, node_model: NodeModel, node_repository_mock: NodeRepositoryMock):
        self.assertEqual(node_model.node_id, node_repository_mock.first_node_id)
        self.assertEqual(node_model.node_name, node_repository_mock.first_node_name)
        self.assertEqual(node_model.x_coord, node_repository_mock.first_x_coord)
        self.assertEqual(node_model.y_coord, node_repository_mock.first_y_coord)
        self.assertEqual(node_model.graph_id, node_repository_mock.graph_id)

    def test_insert_node(self):
        # prepare
        node_repository_mock = NodeRepositoryMock()
        node_business_service = NodeBusinessService(node_repository_mock)
        node_model = NodeModel()

        node_name = 'TestNodeName'
        x_coord = 100
        y_coord = 87
        graph_id = 1

        node_model.node_name = node_name
        node_model.graph_id = graph_id
        node_model.x_coord = x_coord
        node_model.y_coord = y_coord

        # act
        result_node_model = node_business_service.insert_node(node_model)

        # assert node id the same
        self.assertEqual(result_node_model.node_id, node_repository_mock.first_node_id)

        # assert it is the same node_model instance
        self.assertEqual(result_node_model, node_model)

        # assert it is the same graph_id
        self.assertEqual(result_node_model.graph_id, node_repository_mock.graph_id)

        # assert is is the same second_x_coord
        self.assertEqual(result_node_model.x_coord, node_repository_mock.first_x_coord)

    def test_get_node_model(self):
        # prepare
        node_repository_mock = NodeRepositoryMock()
        node_business_service = NodeBusinessService(node_repository_mock)

        # act
        result_node_model = node_business_service.get_node_model(node_repository_mock.first_node_id)

        # assert type is node_model
        self.assertEqual(type(result_node_model), NodeModel)

        # verify properties are correct
        self.verify_properties_of_first_node_model(result_node_model, node_repository_mock)

    def test_get_node_models(self):
        # prepare
        node_repository_mock = NodeRepositoryMock()
        node_business_service = NodeBusinessService(node_repository_mock)

        # act
        result_list_node_models = node_business_service.get_node_models(node_repository_mock.graph_id)

        # assert type is node_model
        for element in result_list_node_models:
            self.assertEqual(type(element), NodeModel)

        # verify properties are correct
        self.verify_properties_of_first_node_model(result_list_node_models[0], node_repository_mock)

        self.assertEqual(result_list_node_models[1].node_id, node_repository_mock.second_node_id)
        self.assertEqual(result_list_node_models[1].node_name, node_repository_mock.second_node_name)
        self.assertEqual(result_list_node_models[1].x_coord, node_repository_mock.second_x_coord)
        self.assertEqual(result_list_node_models[1].y_coord, node_repository_mock.second_y_coord)
        self.assertEqual(result_list_node_models[1].graph_id, node_repository_mock.graph_id)

    def test_update_node(self):
        # prepare
        node_repository_mock = NodeRepositoryMock()
        node_business_service = NodeBusinessService(node_repository_mock)
        node_model = NodeModel()

        updated_node_name = 'UpdatedNodeName'
        updated_x_coord = 130
        updated_y_coord = 100

        node_model.node_id = node_repository_mock.first_node_id
        node_model.node_name = updated_node_name
        node_model.graph_id = node_repository_mock.graph_id
        node_model.x_coord = updated_x_coord
        node_model.y_coord = updated_y_coord

        # act
        result_node_model = node_business_service.update_node(node_model)

        # assert
        # assert same node model instance
        self.assertEqual(result_node_model, node_model)

        # verify properties of result_node_model
        self.assertEqual(result_node_model.node_id, node_repository_mock.first_node_id)

        # assert name is updated
        self.assertEqual(result_node_model.node_name, updated_node_name)

        # assert x_coord are updated
        self.assertEqual(result_node_model.x_coord, updated_x_coord)

        # assert y coord are updated
        self.assertEqual(result_node_model.y_coord, updated_y_coord)


