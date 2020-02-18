class NodeArchNode(object):

    def __init__(self, begin_node, end_node):
        self.begin_node = begin_node
        self.end_node = end_node

    def __repr__(self):
        nval = self.begin_node and self.begin_node.ordering_number or None
        pval = self.end_node and self.end_node.ordering_number or None
        return f'[{repr(nval)}, {repr(pval)}]'
