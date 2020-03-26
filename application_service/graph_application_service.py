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
        pair_of_node_ids = []  # list of tuple containing unsaved and saved node_id
        if graph_model.graph_id == -1:  # introduce graph_model for first time
            self.graph_business_service.insert_graph(graph_model)

        if len(graph_model.list_of_nodes) > 0:  # if nodes are created
            for node_model in graph_model.list_of_nodes:  # for each created node
                if node_model.node_id < 0:  # if node was not already inserted
                    unsaved_node_id = node_model.node_id
                    node_model.graph_id = graph_model.graph_id
                    self.node_business_service.insert_node(node_model)  # insert node
                    pair_of_node_ids.append((unsaved_node_id, node_model.node_id))  # append the pair of saved and unsaved node_id

                if len(node_model.start_edges) > 0:  # if there are edges in node_model.start_edges
                    for edge_model in node_model.start_edges:  # for every edge_model
                        edge_model.graph_id = graph_model.graph_id  # set the graph_id
                        for pair_of_ids in pair_of_node_ids:
                            if edge_model.start_node_id == pair_of_ids[0]:
                                edge_model.start_node_id = pair_of_ids[1]

                        if edge_model.start_node_id > 0 and edge_model.end_node_id > 0:
                            self.edge_business_service.insert_edge(edge_model)

                if len(node_model.end_edges) > 0:
                    for edge_model in node_model.end_edges:
                        edge_model.graph_id = graph_model.graph_id
                        for pair_of_ids in pair_of_node_ids:
                            if edge_model.end_node_id == pair_of_ids[0]:
                                edge_model.end_node_id = pair_of_ids[1]

                        if edge_model.start_node_id > 0 and edge_model.end_node_id > 0:
                            self.edge_business_service.insert_edge(edge_model)

    def get_graph_model(self, graph_id: int) -> GraphModel:
        graph_model = self.graph_business_service.get_graph_model(graph_id)
        graph_nodes = self.node_business_service.get_node_models(graph_id)
        graph_model.list_of_nodes = graph_nodes
        for node in graph_model.list_of_nodes:
            graph_edges = self.edge_business_service.get_edge_models(node.node_id)
            for edge_model in graph_edges:
                if edge_model.start_node_id == node.node_id:
                    node.start_edges = edge_model
                elif edge_model.end_node_id == node.node_id:
                    node.end_edges = edge_model
        return graph_model
