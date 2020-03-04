from abc import abstractmethod


class GraphRepositoryBase(object):

    @abstractmethod
    def insert_graph(self, graph_name: str) -> int:
        pass

    @abstractmethod
    def get_graph(self, graph_id: int) -> list or tuple:
        pass

    @abstractmethod
    def update_graph(self, graph_id: int, graph_name: str):
        pass

    @abstractmethod
    def delete_graph(self, graph_id: int):
        pass
