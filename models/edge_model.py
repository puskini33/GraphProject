class EdgeModel(object):

    def __init__(self, edge_id: int = -1, edge_name: str = '', edge_cost: int = -1,
                 start_node_id: int = -1, end_node_id: int = -1, graph_id: int = -1):
        self.edge_id = edge_id
        self.edge_name = edge_name
        self.edge_cost = edge_cost
        self.start_node_id = start_node_id
        self.end_node_id = end_node_id
        self.graph_id = graph_id

    def __repr__(self) -> str:
        return f'Edge Id: {self.edge_id}, Edge Name: {self.edge_name}, Edge Cost: {self.edge_cost}, ' \
               f'Start Node Id: {self.start_node_id},' \
               f'End Node Id: {self.end_node_id}, Graph Id: {self.graph_id}'
