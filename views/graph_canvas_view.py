from contracts.views.view_base import ViewBase
from models.node_model import NodeModel
from tkinter import *
from models.edge_model import EdgeModel
from models.graph_model import GraphModel
from typing import Callable


class GraphCanvasView(ViewBase, Frame):

    def __init__(self, root: Tk) -> None:
        Frame.__init__(self, root)
        self.configure(width=1000, height=800, background='antique white')

        self.save_button = Button(self, text='Save Graph', bg='DeepSkyBlue3', fg='white', width=10,
                                  font='bold')
        self.back_button = Button(self, text="Back", bg='DeepSkyBlue3', fg='white', width=10,
                                  font='bold')

        self.edge_cost_label = Label(self, text="Set edge cost", bg='antique white', font=('Helvetica', 9, "bold"))
        self.graph_name_label = Label(self, text="Introduce Graph Name:", bg='antique white', font=('Helvetica', 8, "bold"))
        self.entry_graph_name = Entry(self, font='yellow', width=10)
        self.entry_edge_cost = Entry(self, font='yellow', width=10)
        self.canvas = Canvas(self, bg='white', cursor='arrow')
        self.place_widgets()

    def place_widgets(self) -> None:
        self.save_button.place(relx=.98, rely=.25, anchor="e")
        self.back_button.place(relx=.98, rely=.80, anchor="e")
        self.graph_name_label.place(relx=0.93, rely=.10, anchor='n')
        self.edge_cost_label.place(relx=.97, rely=.43, anchor="e")
        self.canvas.place(width=850, height=500)
        self.entry_graph_name.place(relx=0.93, rely=.15, anchor='n')
        self.entry_edge_cost.place(relx=.93, rely=.45, anchor="n")

    def draw_circle(self, node_model: NodeModel) -> None:
        self.canvas.create_oval(node_model.x_coord - node_model.radius, node_model.y_coord - node_model.radius,
                                node_model.x_coord + node_model.radius, node_model.y_coord + node_model.radius, fill='chocolate1', width=3)

    def draw_line(self, line_widget):
        line_widget.view.draw_line()

    def set_edge_cost(self, edge_model: EdgeModel):
        self.entry_edge_cost.delete(0, 'end')
        self.entry_edge_cost.insert(0, edge_model.edge_cost)

    def set_graph_name(self, graph_model: GraphModel):
        self.entry_graph_name.insert(0, graph_model.graph_name)

    def bind_entry_edge_cost_to_change(self, on_edge_cost_changed: Callable):
        self.entry_edge_cost.bind('<KeyRelease>', on_edge_cost_changed)

    def bind_buttons_to_click(self, right_click_event_handler: Callable, left_click_event_handler: Callable):
        self.canvas.bind('<Button-3>', right_click_event_handler)
        self.canvas.bind('<Button-1>', left_click_event_handler)

    def load_frame(self) -> None:
        self.pack()

    def destroy_frame(self) -> None:
        self.destroy()