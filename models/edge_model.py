class EdgeModel(object):

    def __init__(self, edge_id: int, edge_name: str, edge_cost: int, start_node_id: int, end_node_id: int,
                 graph_id: int):
        self.id = edge_id
        self.name = edge_name
        self.cost = edge_cost
        self.start_node_id = start_node_id
        self.end_node_id = end_node_id
        self.graph_id = graph_id

    def __repr__(self):
        return f'[Edge Id: {self.id}, Edge Name: {self.name}, Edge Cost: {self.cost}, ' \
               f'Start Node Id: {self.start_node_id},' \
               f' End Node Id: {self.end_node_id}, Graph Id: {self.graph_id}]'
