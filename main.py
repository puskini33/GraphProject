from tkinter import *
from view.graph_view import GraphView
from models.graph_model import GraphModel
from application_service.graph_application_service import GraphApplicationService
from business_service.graph_business_service import GraphBusinessService
from business_service.node_business_service import NodeBusinessService
from business_service.edge_business_service import EdgeBusinessService
from repository_service.graph_repository import GraphRepository
from repository_service.node_repository import NodeRepository
from repository_service.edge_repository import EdgeRepository
from models.edge_model import EdgeModel
from models.node_model import NodeModel
import types


def main():
    window = Tk()
    window.geometry("700x700")
    graph_repository = GraphRepository()
    node_repository = NodeRepository()
    edge_repository = EdgeRepository()
    graph_business_service = GraphBusinessService(graph_repository)
    node_business_service = NodeBusinessService(node_repository)
    edge_business_service = EdgeBusinessService(edge_repository)
    unsaved_graph_model = GraphModel(graph_name='Elena')

    trial_graph_app_service = GraphApplicationService(graph_business_service, node_business_service,
                                                      edge_business_service)

    # saved_graph_model = trial_graph_app_service.save_graph_model(unsaved_graph_model)
    graph_model = trial_graph_app_service.get_graph_model(55)

    graph_view = GraphView(window, graph_model, trial_graph_app_service)
    window.mainloop()

    edge_model = EdgeModel()
    node_model = NodeModel()
    edge_model.start_node = node_model

if __name__ == '__main__':
    main()






