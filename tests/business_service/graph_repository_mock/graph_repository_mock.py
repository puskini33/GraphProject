from repository_service.contracts.graph_repository_base import GraphRepositoryBase


class GraphRepositoryMock(GraphRepositoryBase):

    def __init__(self):
        self.latest_graph_id = -1
        self.list_of_graphs = []

    def insert_graph(self, graph_name: str) -> int:
        self.latest_graph_id += 1
        self.list_of_graphs.append((self.latest_graph_id, graph_name))
        return self.latest_graph_id

    def get_graph(self, graph_id: int) -> list or tuple:
        pass

    def update_graph(self, graph_id: int, graph_name: str):
        pass

    def delete_graph(self, graph_id: int):
        pass
