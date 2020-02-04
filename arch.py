class Arch(object):

    def __init__(self, length, node1, node2):
        self.length = length
        self.node1 = node1
        self.node2 = node2

    def __repr__(self):
        return f'[{self.length}, {self.node1}, {self.node2}]'
