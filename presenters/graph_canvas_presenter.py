from contracts.presenters.presenter_base import PresenterBase
from views.graph_canvas_view import GraphCanvasView
from application_service.graph_application_service_factory import GraphAppServiceFactory
from models.common_models.view_navigation_parameter import ViewNavigationParameter
from models.enums.graph_canvas_state import GraphCanvasState
from models.graph_model import GraphModel
from models.edge_model import EdgeModel
from helpers.utils import *
import presenters


class GraphCanvasPresenter(PresenterBase):
    counter_id = -1

    def __init__(self,  root_presenter: presenters.graph_it_app_presenter.GraphItAppPresenter,
                 view_parameter: ViewNavigationParameter) -> None:
        self.root_presenter: presenters.graph_it_app_presenter.GraphItAppPresenter = root_presenter
        self.view: GraphCanvasView = GraphCanvasView(self.root_presenter.get_root_view())
        self.view.save_button.bind('<Button-1>', self.save_graph)
        self.view.back_button.bind('<Button-1>', self.root_presenter.go_to_start_page)

        self.graph_app_service = GraphAppServiceFactory.get_instance()
        self.graph_model = None

        self.selected_circles = []

        self.set_graph_model(view_parameter)
        self.initialize_from_graph_model()
        self.init_view_elements()

    def init_view_elements(self) -> None:
        self.view.canvas.bind('<Button-3>', self.right_click_event_handler)
        self.view.canvas.bind('<Button-1>', self.left_click_event_handler)

    def right_click_event_handler(self, event) -> None:
        node_model = self.set_node_model(event.x, event.y)
        self.view.draw_circle(node_model)

    def left_click_event_handler(self, event) -> None:
        clicked_circle = self.get_overlapping_node(event.x, event.y)
        if clicked_circle:
            self.selected_circles.append(clicked_circle)
        if len(self.selected_circles) == 2:
            self.set_edge_model(self.selected_circles[0], self.selected_circles[1])
            self.view.draw_line(self.selected_circles[0], self.selected_circles[1])
            self.selected_circles = []

    def initialize_from_graph_model(self):
        self.view.entry_graph_name.insert(0, self.graph_model.graph_name)

    def set_graph_model(self, view_parameter: ViewNavigationParameter) -> None:
        if view_parameter.graph_canvas_state == GraphCanvasState.new:
            self.graph_model = GraphModel()
        elif view_parameter.graph_canvas_state == GraphCanvasState.saved:
            self.graph_model = self.graph_app_service.get_graph_model(view_parameter.graph_id)
            self.draw_graph(self.graph_model)

    def get_overlapping_node(self, x: int, y: int) -> NodeModel or None:
        for node in self.graph_model.list_of_nodes:
            value = are_coordinates_on_node(node, x, y)
            if value is True:
                return node

    def set_node_model(self, x: int, y: int) -> NodeModel:
        node_model = NodeModel(node_name='NodeName')
        self.set_id(node_model)
        node_model.set_coord(x, y)
        self.graph_model.list_of_nodes.append(node_model)
        return node_model

    def set_edge_model(self, start_node: NodeModel, end_node: NodeModel) -> None:
        edge_model = EdgeModel(edge_name='EdgeName')
        self.set_id(edge_model)

        edge_model.start_node_id = start_node.node_id
        start_node.start_edges.append(edge_model)

        edge_model.end_node_id = end_node.node_id
        end_node.end_edges.append(edge_model)

    def draw_graph(self, graph_model: GraphModel) -> None:
        for node_model in graph_model.list_of_nodes:
            self.view.draw_circle(node_model)

            if node_model.start_edges:
                for edge_model in node_model.start_edges:
                    self.view.draw_line(edge_model.start_node, edge_model.end_node)

            if node_model.end_edges:
                for edge_model in node_model.end_edges:
                    self.view.draw_line(edge_model.start_node, edge_model.end_node)

    def save_graph(self, event) -> None:
        ui_graph_name = self.view.entry_graph_name.get()
        if ui_graph_name:
            self.graph_model.graph_name = ui_graph_name
        else:
            self.graph_model.graph_name = 'Graph Name'

        self.graph_app_service.save_graph_model(self.graph_model)

    def set_id(self, element: NodeModel or EdgeModel or GraphModel) -> None:
        GraphCanvasPresenter.counter_id -= 1
        if type(element) == NodeModel:
            element.node_id = GraphCanvasPresenter.counter_id
        elif type(element) == GraphModel:
            element.graph_id = GraphCanvasPresenter.counter_id
        elif type(element) == EdgeModel:
            element.edge_id = GraphCanvasPresenter.counter_id

    def load_view(self) -> None:
        self.view.load_frame()

    def destroy_view(self) -> None:
        self.view.destroy_frame()