from contracts.presenters.presenter_base import PresenterBase
from views.graph_canvas_view import GraphCanvasView
from application_service.graph_application_service_factory import GraphAppServiceFactory
from models.common_models.view_navigation_parameter import ViewNavigationParameter
from models.enums.graph_canvas_state import GraphCanvasState
from presenters.custom_widgets_presenter.line_widget_presenter import LineWidgetPresenter
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
        self.selected_line_widget: LineWidgetPresenter or None = None  # Presenter or view

        self.set_graph_model(view_parameter)
        self.initialize_name_graph_model()
        self.init_view_elements()

    def init_view_elements(self) -> None:
        self.view.bind_buttons_to_click(self.right_click_event_handler, self.left_click_event_handler)
        self.view.bind_entry_edge_cost_to_change(self.on_edge_cost_changed)

    def right_click_event_handler(self, event) -> None:
        if self.is_already_node(event) is False:
            node_model = self.set_node_model(event.x, event.y)
            self.view.draw_circle(node_model)

    def left_click_event_handler(self, event) -> None:
        clicked_circle = self.get_overlapping_node(event.x, event.y)
        if clicked_circle:
            self.selected_circles.append(clicked_circle)
        if len(self.selected_circles) == 2 and self.selected_circles[0] != self.selected_circles[1]:
            if self.is_already_edge(self.selected_circles[0], self.selected_circles[1]) is False:  # if an edge exists
                edge_model = self.set_edge_model(self.selected_circles[0], self.selected_circles[1])
                self.draw_line(edge_model)
                self.selected_circles = []
            else:
                self.selected_circles.clear()
        elif len(self.selected_circles) == 2 and self.selected_circles[0] == self.selected_circles[1]:  # if user clicked twice on the same node
            self.selected_circles.clear()

    def is_already_node(self, event):
        node = self.get_overlapping_node(event.x, event.y)
        if node:
            return True

        return False

    def is_already_edge(self, start_node, end_node):
        for edge in start_node.start_edges:
            if edge in end_node.end_edges:  # if the edge already exists
                return True

        for edge in start_node.end_edges:  # if the edge already exists
            if edge in end_node.start_edges:
                return True
        return False

    def on_edge_cost_changed(self, event):
        if self.selected_line_widget is not None:
            edge_cost_from_label = self.view.entry_edge_cost.get()
            edge_cost = get_valid_number(edge_cost_from_label)  # verify validity of result from label and set edge_cost
            self.selected_line_widget.edge_model.edge_cost = edge_cost
            self.selected_line_widget.view.update_edge_cost_label()

    def initialize_name_graph_model(self):
        self.view.set_graph_name(self.graph_model)

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

    def set_edge_model(self, start_node: NodeModel, end_node: NodeModel) -> EdgeModel:
        edge_model = EdgeModel(edge_name='EdgeName')
        self.set_id(edge_model)

        edge_model.start_node_id = start_node.node_id
        edge_model.start_node = start_node
        start_node.start_edges.append(edge_model)

        edge_model.end_node_id = end_node.node_id
        edge_model.end_node = end_node
        end_node.end_edges.append(edge_model)
        return edge_model

    def on_line_click(self, line_widget: LineWidgetPresenter):
        if self.selected_line_widget is not None:
            self.selected_line_widget.view.change_to_default_color()  # change the color of the previous line to default

        self.selected_line_widget = line_widget
        self.view.set_edge_cost(self.selected_line_widget.edge_model)

    def draw_line(self, edge_model):
        line_widget = LineWidgetPresenter(self.on_line_click, edge_model, self.view.canvas)

    def draw_graph(self, graph_model: GraphModel) -> None:
        for node_model in graph_model.list_of_nodes:
            self.view.draw_circle(node_model)

            if node_model.start_edges:
                for edge_model in node_model.start_edges:
                    self.draw_line(edge_model)

            if node_model.end_edges:
                for edge_model in node_model.end_edges:
                    self.draw_line(edge_model)

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