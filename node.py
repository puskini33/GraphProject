class Node(object):

    def __init__(self, node_name, graph_id, prev_node_id=None, next_node_id=None):
        self.node_name = node_name
        self.prev_node_id = prev_node_id
        self.next_node_id = next_node_id
        self.graph_id = graph_id

    def __repr__(self):
        return f'[Node Name: {self.node_name}, PrevNode: {self.prev_node_id}, ' \
                f'NextNode: {self.next_node_id}, Graph Id: {self.graph_id}]'
