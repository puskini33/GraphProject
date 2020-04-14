from models.graph_model import GraphModel
from models.node_model import NodeModel
from models.edge_model import EdgeModel
from application_service.graph_application_service import GraphApplicationService
from functools import partial
from tkinter import *
import view


class GraphView(Frame):
    counter_id = -1

    def __init__(self, window: view.main.GraphItApp, graph_model: GraphModel, graph_app_service: GraphApplicationService):
        self.window = window
        save_button = Button(self.window, text='Save Graph', bg='DeepSkyBlue4', fg='white', width=10,
                             font='bold', command=self.save_graph_name)
        action_with_arg = partial(self.window.switch_frame, view.main.StartPage)
        back_button = Button(self.window, text="Back", bg='DeepSkyBlue4', fg='white', width=10,
                             font='bold', command=action_with_arg)
        back_button.place(relx=.99, rely=.50, anchor="e")
        if graph_model.graph_id < 0:  # display entry with graph_name only if graph does not exist in the database
            Label(self.window, text="Introduce Graph Name:", font=('Helvetica', 8, "bold")).place(relx=0.93, rely=.10, anchor='n')
            self.entry_graph_name = Entry(self.window, font='yellow', width=10)
            self.entry_graph_name.place(relx=0.93, rely=.15, anchor='n')

        self.canvas = Canvas(self.window, width=700, height=500, bg='white', cursor='arrow', confine=True)

        save_button.place(relx=.99, rely=.35, anchor="e")

        self.canvas.pack()

        self.graph_model = graph_model
        self.graph_app_service = graph_app_service
        self.selected_circles = []
        self.node_radius = 25
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.canvas.bind('<Button-3>', self.right_click_event_handler)
        self.canvas.bind('<Button-1>', self.left_click_event_handler)
        self.draw_graph(self.graph_model)

    def right_click_event_handler(self, event):
        node_model = NodeModel(node_name='NodeName')
        self.set_id(node_model)
        node_model.set_coord(event.x, event.y)
        self.graph_model.list_of_nodes.append(node_model)
        self.draw_node(node_model)

    def left_click_event_handler(self, event):
        coordinates = self.select_node(event.x, event.y)
        if coordinates is not None:
            self.selected_circles = []
            self.draw_edge(coordinates)

    def select_node(self, x, y):
        selection = self.canvas.find_overlapping(x, y, x, y)
        if len(selection) == 0:
            return
        elif len(selection) != 0 and len(self.selected_circles) < 2:
            self.selected_circles.append(selection)
        if len(self.selected_circles) == 2:
            if all(self.selected_circles):
                return self.join_circles()
        elif len(self.selected_circles) == 2 and self.selected_circles[0] == self.selected_circles[1]:
            return

    def join_circles(self):
        coordinates = []
        circle_number = 1

        edge_model = EdgeModel(edge_name='EdgeName')
        self.set_id(edge_model)

        for circle in self.selected_circles:
            try:
                x, y = self.calculate_center_node(edge_model, circle, circle_number)
                circle_number += 1
                coordinates.append(x)
                coordinates.append(y)
            except TypeError:
                self.selected_circles = []
                return
        return coordinates

    def calculate_center_node(self, edge_model, item, circle_number):
        if self.canvas.bbox(item) is None:
            return
        x0, y0, x1, y1 = self.canvas.bbox(item)
        coord_x = ((x0 + 0.01) + (x1 + 0.01)) / 2
        coord_y = ((y0 + 0.01) + (y1 + 0.01)) / 2

        for node in self.graph_model.list_of_nodes:
            if node.x_coord == int(coord_x) and node.y_coord == int(coord_y):
                if circle_number == 1:
                    edge_model.start_node_id = node.node_id
                    node.start_edges.append(edge_model)
                elif circle_number == 2:
                    edge_model.end_node_id = node.node_id
                    node.end_edges.append(edge_model)
        return coord_x, coord_y

    def draw_graph(self, graph_model: GraphModel):
        try:
            coordinates = []
            for node_model in graph_model.list_of_nodes:
                self.draw_node(node_model)

                if node_model.start_edges:
                    for edge_model in node_model.start_edges:
                        coordinates = [edge_model.start_node.x_coord, edge_model.start_node.y_coord,
                                       edge_model.end_node.x_coord, edge_model.end_node.y_coord]
                        self.draw_edge(coordinates)

                if node_model.end_edges:
                    for edge_model in node_model.end_edges:
                        coordinates = [edge_model.start_node.x_coord, edge_model.start_node.y_coord,
                                       edge_model.end_node.x_coord, edge_model.end_node.y_coord]
                        self.draw_edge(coordinates)
        except AttributeError:
            return

    def draw_node(self, node_model):
        self.canvas.create_oval(node_model.x_coord - self.node_radius, node_model.y_coord - self.node_radius,
                                node_model.x_coord + self.node_radius, node_model.y_coord + self.node_radius, fill='orange', width=3, tag='all')

    def draw_edge(self, coordinates):
        self.canvas.create_line(coordinates, tag='all', arrow='last', width=3)

    def save_graph_name(self):
        try:
            if self.entry_graph_name.get():
                self.graph_model.graph_name = self.entry_graph_name.get()
                self.graph_app_service.save_graph_model(self.graph_model)
            else:
                self.entry_graph_name.configure({"background": "bisque"})
        except AttributeError:
            self.graph_app_service.save_graph_model(self.graph_model)

    def set_id(self, element):
        GraphView.counter_id -= 1
        if type(element) == NodeModel:
            element.node_id = GraphView.counter_id
        elif type(element) == GraphModel:
            element.graph_id = GraphView.counter_id
        elif type(element) == EdgeModel:
            element.edge_id = GraphView.counter_id