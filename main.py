from tkinter import *
from view.graph_view import GraphView
from models.graph_model import GraphModel
from application_service.graph_application_service import GraphApplication
from business_service.graph_business_service import GraphBusinessService
from business_service.node_business_service import NodeBusinessService
from repository_service.graph_repository import GraphRepository
from repository_service.node_repository import NodeRepository


def main():
    window = Tk()
    window.geometry("700x700")
    graph_repository = GraphRepository()
    node_repository = NodeRepository()
    graph_business_service = GraphBusinessService(graph_repository)
    node_business_service = NodeBusinessService(node_repository)
    trial_graph_model = GraphModel(graph_name='Elena')
    trial_graph_app_service = GraphApplication(graph_business_service, node_business_service)
    graph_model_from_db = trial_graph_app_service.get_graph_model(1)
    graph= GraphView(window, graph_model_from_db, trial_graph_app_service)

    window.mainloop()


if __name__ == '__main__':
    main()
