from contracts.repository_service.graph_repository_base import GraphRepositoryBase
from typing import List, Tuple


class GraphRepositoryMock(GraphRepositoryBase):

    def __init__(self):
        self.mock_graph_id = 33
        self.mock_graph_name = 'GraphName1'
        self.mock_updated_graph_name = 'UpdatedGraphName1'

    def insert_graph(self, graph_name: str) -> int:
        return self.mock_graph_id

    def get_graph(self, graph_id: int) -> List[Tuple]:
        return [(self.mock_graph_id, self.mock_graph_name)]

    def update_graph(self, graph_id: int, graph_name: str):
        return

    def delete_graph(self, graph_id: int):
        pass
