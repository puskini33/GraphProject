from models.edge_model import EdgeModel
from typing import List


class NodeModel(object):

    def __init__(self, node_id: int = -1, node_name: str = '', graph_id: int = -1):
        self.node_id = node_id
        self.node_name = node_name
        self.graph_id = graph_id
        self.x_coord = 0
        self.y_coord = 0
        self.start_edges: List[EdgeModel] = []
        self.end_edges: List[EdgeModel] = []

    def __repr__(self) -> str:
        return f'Node Id: {self.node_id}, Node Name: {self.node_name}, X Coord: {self.x_coord} ' \
               f'Y Coord: {self.y_coord}, Graph Id: {self.graph_id}'

    def set_coord(self, x: int, y: int):
        self.x_coord = x
        self.y_coord = y
