from contracts.repository_service.graph_repository_base import GraphRepositoryBase
from business_service.map_helpers.graph_map_helper import GraphMapHelper
from contracts.business_service.graph_business_service_base import GraphBusinessServiceBase
from models.graph_model import GraphModel
from typing import List


class GraphBusinessService(GraphBusinessServiceBase):

    def __init__(self, in_graph_repository_base: GraphRepositoryBase):
        self.graph_repository = in_graph_repository_base
        super().__init__()

    def insert_graph(self, graph_model: GraphModel) -> GraphModel:
        graph_id = self.graph_repository.insert_graph(graph_model.graph_name)
        graph_model.graph_id = graph_id
        return graph_model

    def get_graph_model(self, graph_id: int) -> GraphModel:
        list_values_graph = self.graph_repository.get_graph(graph_id)
        return GraphMapHelper.db_entities_to_graph_models(list_values_graph)[0]

    def get_all_graph_models(self) -> List[GraphModel]:
        list_values_graphs = self.graph_repository.get_all_graphs()
        return GraphMapHelper.db_entities_to_graph_models(list_values_graphs)

    def update_graph(self, graph_model: GraphModel) -> GraphModel:
        self.graph_repository.update_graph(graph_model.graph_id, graph_model.graph_name)
        return graph_model

    def delete_graph(self, graph_id: int):
        self.graph_repository.delete_graph(graph_id)
