class Edge(object):

    def __init__(self, edge_id, edge_name, edge_cost, start_node_id, end_node_id, graph_id):
        self.id = edge_id
        self.name = edge_name
        self.cost = edge_cost
        self.start_node_id = start_node_id
        self.end_node_id = end_node_id
        self.graph_id = graph_id

    def __repr__(self):
        return f'[Edge Id: {self.id}, Edge Name: {self.name}, Edge Cost: {self.cost}, Start Node Id: {self.start_node_id},' \
               f' End Node Id: {self.end_node_id}, Graph Id: {self.graph_id}]'
