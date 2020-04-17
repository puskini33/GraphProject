from models.graph_model import GraphModel
from application_service.graph_application_service import GraphApplicationService
from business_service.graph_business_service import GraphBusinessService
from business_service.node_business_service import NodeBusinessService
from business_service.edge_business_service import EdgeBusinessService
from repository_service.graph_repository import GraphRepository
from repository_service.node_repository import NodeRepository
from repository_service.edge_repository import EdgeRepository


class BackendSetup(object):

    graph_repository = GraphRepository()
    node_repository = NodeRepository()
    edge_repository = EdgeRepository()
    graph_business_service = GraphBusinessService(graph_repository)
    node_business_service = NodeBusinessService(node_repository)
    edge_business_service = EdgeBusinessService(edge_repository)
    graph_app_service = GraphApplicationService(graph_business_service, node_business_service, edge_business_service)

    def load_graph(self, graph_id):
        loaded_graph_model = BackendSetup.graph_app_service.get_graph_model(graph_id)
        return loaded_graph_model

    def save_graph(self):
        unsaved_graph_model = GraphModel()
        return unsaved_graph_model