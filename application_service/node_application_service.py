from business_service.edge_business_service import EdgeBusinessService
from business_service.node_business_service import NodeBusinessService
from models.node_model import NodeModel


class NodeApplication(object):

    def __init__(self, in_node_business_service: NodeBusinessService, in_edge_business_service: EdgeBusinessService):
        self.in_node_business_service = in_node_business_service
        self.in_edge_business_service = in_edge_business_service

