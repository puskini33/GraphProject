from models.graph_model import GraphModel
from models.node_model import NodeModel
from models.edge_model import EdgeModel
from application_service.graph_application_service import GraphApplicationService
from tkinter import *


class GraphView(Frame):

    def __init__(self, window, graph_model: GraphModel, graph_app_service: GraphApplicationService):
        self.window = window
        self.canvas = Canvas(self.window, width=700, height=700, bg='white')
        self.graph_model = graph_model
        self.graph_app_service = graph_app_service
        self.selected_circles = []
        self.node_radius = 25
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.canvas.grid(row=0, column=0)
        self.canvas.bind('<Button-3>', self.right_click_event_handler)
        self.canvas.bind('<Button-1>', self.left_click_event_handler)
        self.master.title('GraphIt')
        self.add_menu_bar()
        self.draw_graph(self.graph_model)

    def add_menu_bar(self):
        menu_bar = Menu(self.master)
        self.master.config(menu=menu_bar)

        drop_down_menu = Menu(menu_bar)
        menu_bar.add_cascade(label="File", menu=drop_down_menu)
        drop_down_menu.add_command(label="Save", command=self.save_graph)
        drop_down_menu.add_command(label="Load Graph", command=self.get_graph)

    def right_click_event_handler(self, event):
        x, y = event.x, event.y
        node_model = NodeModel(node_name='TrialNode')
        node_model.set_coord(x, y)
        self.graph_model.list_of_nodes.append(node_model)
        self.draw_node(node_model)

    def left_click_event_handler(self, event):
        x, y = event.x, event.y
        edge_model = EdgeModel(edge_name='TrialEdge')
        self.select_node(x, y)

    def select_node(self, x, y):
        selection = self.canvas.find_overlapping(x, y, x, y)
        if len(selection) == 0:
            return
        elif len(selection) != 0 and len(self.selected_circles) < 2:
            self.selected_circles.append(selection)
        if len(self.selected_circles) == 2:
            if all(self.selected_circles):
                self.join_circles()
        elif len(self.selected_circles) == 2 and self.selected_circles[0] == self.selected_circles[1]:
            return

    def join_circles(self):
        coordinates = []
        for circle in self.selected_circles:
            try:
                x, y = self.calculate_center_node(circle)
                coordinates.append(x)
                coordinates.append(y)
            except TypeError:
                self.selected_circles = []
                return
        self.canvas.create_line(coordinates, tag='all', arrow='last', width=3)
        self.selected_circles = []

    def calculate_center_node(self, item):
        if self.canvas.bbox(item) is None:
            return
        x0, y0, x1, y1 = self.canvas.bbox(item)
        coord_x = ((x0 + 0.01) + (x1 + 0.01)) / 2
        coord_y = ((y0 + 0.01) + (y1 + 0.01)) / 2
        return coord_x, coord_y

    def draw_graph(self, graph_model: GraphModel):
        for node_model in graph_model.list_of_nodes:
            self.draw_node(node_model)

    def draw_node(self, node_model):
        self.canvas.create_oval(node_model.x_coord - self.node_radius, node_model.y_coord - self.node_radius,
                                node_model.x_coord + self.node_radius, node_model.y_coord + self.node_radius, fill='orange', width=3, tag='all')

    def save_graph(self):
        self.graph_app_service.save_graph_model(self.graph_model)

    def get_graph(self):
        self.graph_app_service.get_graph_model(graph_id=1)
