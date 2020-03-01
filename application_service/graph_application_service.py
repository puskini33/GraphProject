from business_service.graph_business_service import GraphBusinessService
from business_service.node_business_service import NodeBusinessService
from models.graph_model import GraphModel


class GraphApplication(object):

    def __init__(self, in_graph_business_service: GraphBusinessService, in_node_business_service: NodeBusinessService):
        self.graph_business_service = in_graph_business_service
        self.node_business_service = in_node_business_service

    def save_graph_model(self, graph_model: GraphModel):
        if graph_model.graph_id == -1:
            self.graph_business_service.insert_graph(graph_model)
        if len(graph_model.list_of_nodes) > 0:
            for node_model in graph_model.list_of_nodes:
                if node_model.node_id == -1:
                    node_model.graph_id = graph_model.graph_id
                    self.node_business_service.insert_node(node_model)

    def get_graph_model(self, graph_id: int):
        graph_model = self.graph_business_service.get_graph_model(graph_id)
        graph_nodes = self.node_business_service.get_node_models(graph_id)
        graph_model.list_of_nodes = graph_nodes
        return graph_model
