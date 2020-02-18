class Graph(object):

    def __init__(self, graph_id: int, graph_name: str):
        self.graph_id = graph_id
        self.graph_name = graph_name

    def __repr__(self):
        return f'Graph Id: {self.graph_id} , Graph Name: {self.graph_name}'
