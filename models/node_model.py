class NodeModel(object):

    def __init__(self, node_id: int = -1, node_name: str = '', graph_id: int = -1):
        self.node_id = node_id
        self.node_name = node_name
        self.graph_id = graph_id

    def __repr__(self):
        return f'[Node Id: {self.node_id}, Node Name: {self.node_name}, Graph Id: {self.graph_id}]'
