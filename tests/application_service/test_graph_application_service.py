from application_service.graph_application_service import GraphApplicationService
from tests.application_service.business_service_mock.graph_business_service_mock import GraphBusinessServiceMock
from tests.application_service.business_service_mock.node_business_service_mock import NodeBusinessServiceMock
from models.graph_model import GraphModel
from models.node_model import NodeModel
import unittest


class TestGraphApplicationService(unittest.TestCase):

    def test_save_graph_model(self):

        # prepare
        graph_business_service_mock = GraphBusinessServiceMock()
        node_business_service_mock = NodeBusinessServiceMock()
        graph_model = GraphModel()
        graph_application_service = GraphApplicationService(graph_business_service_mock, node_business_service_mock)

        # act

        # insert graph_model

        graph_application_service.save_graph_model(graph_model)

        # add nodes to graph.list_of_nodes
        node1 = NodeModel()
        graph_model.list_of_nodes.append(node1)

        # insert node_models
        graph_application_service.save_graph_model(graph_model)

        # assert
        self.assertEqual(graph_model.graph_id, graph_business_service_mock.graph_model_id)
        self.assertEqual(graph_model.list_of_nodes[0].node_id, node_business_service_mock.node_id)

    def test_get_graph_model(self):
        # prepare
        graph_business_service_mock = GraphBusinessServiceMock()
        node_business_service_mock = NodeBusinessServiceMock()
        graph_application_service = GraphApplicationService(graph_business_service_mock, node_business_service_mock)

        # act
        graph_model_result = graph_application_service.get_graph_model(1)

        # assert
        # self.assertEqual(graph_model_result.list_of_nodes, node_business_service_mock.get_node_models(1))
