from repository_service.contracts.graph_repository_base import GraphRepositoryBase


class GraphRepositoryMock(GraphRepositoryBase):

    def __init__(self):
        self.inserted_graph_id = 33

    def insert_graph(self, graph_name: str) -> int:
        return self.inserted_graph_id

    def get_graph(self, graph_id: int) -> list or tuple:
        pass

    def update_graph(self, graph_id: int, graph_name: str):
        pass

    def delete_graph(self, graph_id: int):
        pass
