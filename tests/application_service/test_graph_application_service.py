from application_service.graph_application_service import GraphApplicationService
from tests.application_service.business_service_mock.graph_business_service_mock import GraphBusinessServiceMock
from tests.application_service.business_service_mock.node_business_service_mock import NodeBusinessServiceMock
from tests.application_service.business_service_mock.edge_business_service_mock import EdgeBusinessServiceMock
from models.graph_model import GraphModel
from models.node_model import NodeModel
from models.edge_model import EdgeModel
import unittest


class TestGraphApplicationService(unittest.TestCase):

    def test_save_graph_model(self):

        # prepare
        graph_business_service_mock = GraphBusinessServiceMock()
        node_business_service_mock = NodeBusinessServiceMock()
        edge_business_service_mock = EdgeBusinessServiceMock()

        graph_model = GraphModel()
        graph_application_service = GraphApplicationService(graph_business_service_mock, node_business_service_mock, edge_business_service_mock)

        # act

        # insert graph_model

        graph_application_service.save_graph_model(graph_model)

        # add nodes to graph.list_of_nodes
        node1 = NodeModel()
        node1.node_id = -1
        node2 = NodeModel()
        node2.node_id = -2
        graph_model.list_of_nodes.append(node1)
        graph_model.list_of_nodes.append(node2)

        # add edges
        edge1 = EdgeModel()
        edge1.start_node_id = node1.node_id
        edge1.end_node_id = node2.node_id

        node1.start_edges.append(edge1)
        node2.end_edges.append(edge1)

        # insert node_models
        graph_application_service.save_graph_model(graph_model)

        # assert
        self.assertEqual(graph_model.graph_id, graph_business_service_mock.graph_model_id)
        self.assertEqual(graph_model.list_of_nodes[0].node_id, node_business_service_mock.node_id)
        self.assertEqual(graph_model.list_of_nodes[0].start_edges[0].edge_id, edge_business_service_mock.edge_id)

    def test_get_graph_model(self):
        # prepare
        graph_business_service_mock = GraphBusinessServiceMock()
        node_business_service_mock = NodeBusinessServiceMock()
        edge_business_service_mock = EdgeBusinessServiceMock()
        graph_application_service = GraphApplicationService(graph_business_service_mock, node_business_service_mock, edge_business_service_mock)

        # act
        graph_model_result = graph_application_service.get_graph_model(1)

        # assert
        # self.assertEqual(graph_model_result.list_of_nodes, node_business_service_mock.get_node_models(1))
        # self.assertEqual(graph_model_result.list_of_nodes[0].start_edges, edge_business_service_mock.get_edge_models(1))