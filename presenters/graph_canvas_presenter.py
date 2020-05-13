from contracts.presenters.presenter_base import PresenterBase
from views.graph_canvas_view import GraphCanvasView
from application_service.graph_application_service_factory import GraphAppServiceFactory
from models.common_models.view_navigation_parameter import ViewNavigationParameter
from models.enums.graph_canvas_state import GraphCanvasState
from models.graph_model import GraphModel
from models.node_model import NodeModel
from models.edge_model import EdgeModel
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
        if view_parameter.graph_canvas_state == GraphCanvasState.new:
            self.graph_model = GraphModel()
        elif view_parameter.graph_canvas_state == GraphCanvasState.saved:
            self.graph_model = self.graph_app_service.get_graph_model(view_parameter.graph_id)
            self.draw_graph(self.graph_model)

        self.selected_circles = []
        self.entry_graph_name = None

        self.init_presenter()

    def init_presenter(self) -> None:
        self.view.canvas.bind('<Button-3>', self.right_click_event_handler)
        self.view.canvas.bind('<Button-1>', self.left_click_event_handler)

    def right_click_event_handler(self, event) -> None:
        node_model = self.create_node_model(event.x, event.y)
        circle_coordinates = [event.x, event.y]
        self.view.draw_circle(circle_coordinates, node_model.radius)

    def left_click_event_handler(self, event) -> None:
        clicked_circle = self.get_node_if_clicked(event.x, event.y)
        if clicked_circle:
            self.selected_circles.append(clicked_circle)
        if len(self.selected_circles) == 2:
            line_coordinates = self.get_coordinates_center_circles()
            if line_coordinates is not None:
                self.selected_circles = []
                self.create_edge_model(line_coordinates)
                self.view.draw_line(line_coordinates)

    def get_abs_coordinates_difference(self, x: int, y: int, node_center_x: int, node_center_y: int) -> tuple:
        dx = abs(x - node_center_x)
        dy = abs(y - node_center_y)
        return dx, dy

    def get_node_if_clicked(self, x: int, y: int) -> NodeModel or bool:
        for node in self.graph_model.list_of_nodes:
            dx, dy = self.get_abs_coordinates_difference(x, y, node.x_coord, node.y_coord)
            if dx + dy <= node.radius:  # if click is inside circle
                return node
            if pow(dx, 2) + pow(dy, 2) <= pow(node.radius, 2):  # if click is on the contour of circle
                return node

        return False

    def get_coordinates_center_circles(self) -> list:
        coordinates = []
        for node_model in self.selected_circles:
            coordinates.append(node_model.x_coord)
            coordinates.append(node_model.y_coord)

        return coordinates

    def create_node_model(self, x: int, y: int) -> NodeModel:
        node_model = NodeModel(node_name='NodeName')
        self.set_id(node_model)
        node_model.set_coord(x, y)
        self.graph_model.list_of_nodes.append(node_model)
        return node_model

    def create_edge_model(self, coordinates: list) -> None:
        edge_model = EdgeModel(edge_name='EdgeName')
        self.set_id(edge_model)
        for node in self.graph_model.list_of_nodes:
            if node.x_coord == coordinates[0] and node.y_coord == coordinates[1]:
                edge_model.start_node_id = node.node_id
                node.start_edges.append(edge_model)
            elif node.x_coord == coordinates[2] and node.y_coord == coordinates[3]:
                edge_model.end_node_id = node.node_id
                node.end_edges.append(edge_model)

    def draw_graph(self, graph_model: GraphModel) -> None:
        try:
            for node_model in graph_model.list_of_nodes:
                circle_coordinates = [node_model.x_coord, node_model.y_coord]
                self.view.draw_circle(circle_coordinates, node_model.radius)

                if node_model.start_edges:
                    for edge_model in node_model.start_edges:
                        line_coordinates = [edge_model.start_node.x_coord, edge_model.start_node.y_coord,
                                            edge_model.end_node.x_coord, edge_model.end_node.y_coord]
                        self.view.draw_line(line_coordinates)

                if node_model.end_edges:
                    for edge_model in node_model.end_edges:
                        line_coordinates = [edge_model.start_node.x_coord, edge_model.start_node.y_coord,
                                            edge_model.end_node.x_coord, edge_model.end_node.y_coord]
                        self.view.draw_line(line_coordinates)
        except AttributeError:
            return

    def save_graph(self, event) -> None:
        if self.view.entry_graph_name.get():
            self.graph_model.graph_name = self.view.entry_graph_name.get()
            self.graph_app_service.save_graph_model(self.graph_model)
        else:  # if save button pressed without a graph_name
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
