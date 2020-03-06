from models.node_model import NodeModel
from typing import List


class GraphModel(object):

    def __init__(self, graph_id: int = -1, graph_name: str = ''):
        self.graph_id = graph_id
        self.graph_name = graph_name
        self.list_of_nodes: List[NodeModel] = []

    def __repr__(self) -> str:
        return f'Graph Id: {self.graph_id} , Graph Name: {self.graph_name}'
