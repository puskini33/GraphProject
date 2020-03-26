from models.graph_model import GraphModel
from models.node_model import NodeModel
from models.edge_model import EdgeModel
from application_service.graph_application_service import GraphApplicationService
from tkinter import *


class GraphView(Frame):
    counter_id = -1

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

    def right_click_event_handler(self, event):
        x, y = event.x, event.y
        node_model = NodeModel(node_name='TrialNode')
        self.set_id(node_model)
        node_model.set_coord(x, y)
        self.graph_model.list_of_nodes.append(node_model)
        self.draw_node(node_model)

    def left_click_event_handler(self, event):
        x, y = event.x, event.y
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
        edge_model = EdgeModel(edge_name='TrialEdge')
        self.set_id(edge_model)
        coordinates = []
        circle_number = 1
        for circle in self.selected_circles:  # append edge_model for circle1
            try:
                x, y = self.calculate_center_node(circle, edge_model, circle_number)
                circle_number += 1
                coordinates.append(x)
                coordinates.append(y)
            except TypeError:
                self.selected_circles = []
                return
        self.canvas.create_line(coordinates, tag='all', arrow='last', width=3)
        self.selected_circles = []

    def calculate_center_node(self, item, edge_model, circle_number):
        if self.canvas.bbox(item) is None:
            return
        x0, y0, x1, y1 = self.canvas.bbox(item)
        coord_x = ((x0 + 0.01) + (x1 + 0.01)) / 2
        coord_y = ((y0 + 0.01) + (y1 + 0.01)) / 2
        for node in self.graph_model.list_of_nodes:  # x,y is in the center of the node, not the coord of node
            if node.x_coord == int(coord_x) and node.y_coord == int(coord_y):
                if circle_number == 1:
                    edge_model.start_node_id = node.node_id
                    node.start_edges.append(edge_model)
                elif circle_number == 2:
                    edge_model.end_node_id = node.node_id
                    node.end_edges.append(edge_model)
        return coord_x, coord_y

    def set_id(self, element):
        GraphView.counter_id -= 1
        if type(element) == NodeModel:
            element.node_id = GraphView.counter_id
        elif type(element) == GraphModel:
            element.graph_id = GraphView.counter_id
        elif type(element) == EdgeModel:
            element.edge_id = GraphView.counter_id

    def draw_graph(self, graph_model: GraphModel):
        for node_model in graph_model.list_of_nodes:
            self.draw_node(node_model)

    def dr
            for edge_model in node_model.start_edges:
                self.select_node(node_model.x_coord, node_model.y_coord)
            for edge_model in node_model.end_edges:
                self.select_node(node_model.x_coord, node_model.y_coord)

    def draw_node(self, node_model):
        self.canvas.create_oval(node_model.x_coord - self.node_radius, node_model.y_coord - self.node_radius,
                                node_model.x_coord + self.node_radius, node_model.y_coord + self.node_radius, fill='orange', width=3, tag='all')

    def save_graph(self):
        self.graph_app_service.save_graph_model(self.graph_model)
