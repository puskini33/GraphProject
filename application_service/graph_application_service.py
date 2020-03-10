from contracts.business_service.graph_business_service_base import GraphBusinessServiceBase
from contracts.business_service.node_business_service_base import NodeBusinessServiceBase
from models.graph_model import GraphModel


class GraphApplicationService(object):

    def __init__(self, in_graph_business_service: GraphBusinessServiceBase, in_node_business_service: NodeBusinessServiceBase):
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

    def get_graph_model(self, graph_id: int) -> GraphModel:
        graph_model = self.graph_business_service.get_graph_model(graph_id)
        graph_nodes = self.node_business_service.get_node_models(graph_id)
        graph_model.list_of_nodes = graph_nodes
        return graph_model
