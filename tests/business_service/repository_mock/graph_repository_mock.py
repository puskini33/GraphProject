from contracts.repository_service.graph_repository_base import GraphRepositoryBase
from typing import List, Tuple


class GraphRepositoryMock(GraphRepositoryBase):

    def __init__(self):
        self.mock_graph_id1 = 33
        self.mock_graph_id2 = 14
        self.mock_graph_name1 = 'GraphName1'
        self.mock_graph_name2 = 'GraphName2'
        self.mock_updated_graph_name1 = 'UpdatedGraphName1'

    def insert_graph(self, graph_name: str) -> int:
        return self.mock_graph_id1

    def get_graph(self, graph_id: int) -> List[Tuple]:
        return [(self.mock_graph_id1, self.mock_graph_name1)]

    def get_all_graphs(self) -> List[Tuple]:
        return [(self.mock_graph_id1, self.mock_graph_name1), (self.mock_graph_id2, self.mock_graph_name2)]

    def update_graph(self, graph_id: int, graph_name: str):
        return

    def delete_graph(self, graph_id: int):
        pass
