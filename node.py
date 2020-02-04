class Node(object):

    def __init__(self, ordering_number, arch1=None, arch2=None, prev_node=None, next_node=None):
        self.ordering_number = ordering_number
        self.arch1 = arch1
        self.arch2 = arch2
        self.prev_node = prev_node
        self.next_node = next_node

    def __repr__(self):
        return f'[Order: {self.ordering_number}, Arch1: {self.arch1}, Arch2: {self.arch2}, PrevNode: {self.prev_node}, NextNode: {self.next_node}]'
