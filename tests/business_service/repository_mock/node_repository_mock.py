from repository_service.contracts.node_repository_base import NodeRepositoryBase


class NodeRepositoryMock(NodeRepositoryBase):
    def __init__(self):
        self.node_id_0 = 16
        self.node_name_0 = 'TestNodeName0'
        self.node_updated_name_0 = 'UpdatedNodeName0'
        self.x_coord_0 = 100
        self.updated_x_coord_0 = 130
        self.y_coord_0 = 87
        self.updated_y_coord_0 = 100
        self.graph_id = 1
        self.node_id_1 = 17
        self.node_name_1 = 'TestNodeName1'
        self.x_coord_1 = 134
        self.y_coord_1 = 187

    def insert_node(self, node_name: str, node_x_coord: int, node_y_coord: int, graph_id: int) -> int:
        return self.node_id_0

    def get_node(self, node_id: int) -> list:
        return [(self.node_id_0, self.node_name_0, self.x_coord_0, self.y_coord_0, self.graph_id)]

    def get_graph_nodes(self, graph_id: int) -> list:
        return [[self.node_id_0, self.node_name_0, self.x_coord_0, self.y_coord_0, self.graph_id],
                [self.node_id_1, self.node_name_1, self.x_coord_1, self.y_coord_1, self.graph_id]]

    def update_node(self, node_id: int, node_name: str, node_x_coord: int, node_y_coord: int, graph_id: int):
        return

    def delete_node(self, node_id: int):
        pass
