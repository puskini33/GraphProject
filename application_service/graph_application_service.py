from contracts.business_service.graph_business_service_base import GraphBusinessServiceBase
from contracts.business_service.node_business_service_base import NodeBusinessServiceBase
from contracts.business_service.edge_business_service_base import EdgeBusinessServiceBase
from models.graph_model import GraphModel


class GraphApplicationService(object):

    def __init__(self, in_graph_business_service: GraphBusinessServiceBase,
                 in_node_business_service: NodeBusinessServiceBase, in_edge_business_service: EdgeBusinessServiceBase):
        self.graph_business_service = in_graph_business_service
        self.node_business_service = in_node_business_service
        self.edge_business_service = in_edge_business_service

    def save_graph_model(self, graph_model: GraphModel):
        if graph_model.graph_id == -1:  # introduce graph_model for first time
            self.graph_business_service.insert_graph(graph_model)

        if graph_model.list_of_nodes:  # if nodes are created
            for node_model in graph_model.list_of_nodes:
                if node_model.node_id < 0:  # if node was not already inserted
                    unsaved_node_id = node_model.node_id
                    node_model.graph_id = graph_model.graph_id
                    self.node_business_service.insert_node(node_model)

                    if node_model.start_edges:
                        self.insert_edge_model(node_model.start_edges, unsaved_node_id, graph_model, node_model)

                    if node_model.end_edges:
                        self.insert_edge_model(node_model.end_edges, unsaved_node_id, graph_model, node_model)

    def insert_edge_model(self, edge_model_list, unsaved_node_id, graph_model, node_model):
        for edge_model in edge_model_list:
            edge_model.graph_id = graph_model.graph_id
            if edge_model.start_node_id == unsaved_node_id:
                edge_model.start_node_id = node_model.node_id
            elif edge_model.end_node_id == unsaved_node_id:
                edge_model.end_node_id = node_model.node_id

            if edge_model.start_node_id > 0 and edge_model.end_node_id > 0:
                self.edge_business_service.insert_edge(edge_model)

    def get_graph_model(self, graph_id: int) -> GraphModel:
        graph_model = self.graph_business_service.get_graph_model(graph_id)
        graph_nodes = self.node_business_service.get_node_models(graph_id)
        graph_model.list_of_nodes = graph_nodes
        graph_edges = self.edge_business_service.get_edge_models_of_graph(graph_id)

        dictionary_of_nodes = {node_model.node_id: node_model for node_model in graph_nodes}

        for edge_model in graph_edges:
            if edge_model.start_node_id in dictionary_of_nodes:
                start_node = dictionary_of_nodes[edge_model.start_node_id]
                start_node.start_edges.append(edge_model)
                edge_model.start_node = start_node
            if edge_model.end_node_id in dictionary_of_nodes:
                end_node = dictionary_of_nodes[edge_model.end_node_id]
                end_node.end_edges.append(edge_model)
                edge_model.end_node = end_node

        return graph_model


