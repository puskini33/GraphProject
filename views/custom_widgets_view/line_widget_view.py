from tkinter import *
from models.edge_model import EdgeModel
from typing import Callable


class LineWidgetView(Frame):

    def __init__(self, canvas_parent, edge_model: EdgeModel, on_line_click: Callable) -> None:
        self.canvas_parent = canvas_parent
        Frame.__init__(self, self.canvas_parent)

        self.on_line_click = on_line_click
        self.edge_model = edge_model
        self.line = None
        self.edge_cost = StringVar()
        self.edge_cost.set(f'{self.edge_model.edge_cost}')
        self.label = Label(self.canvas_parent, textvariable=self.edge_cost, font="Times 8 bold")

    def place_widget(self, center_line_coordinates: tuple) -> None:
        self.label.place(x=center_line_coordinates[0] + 5, y=center_line_coordinates[1] + 15)

    def bind_line_label_to_click(self) -> None:
        self.canvas_parent.tag_bind('line' + str(self.edge_model.edge_id), '<Button-1>', self.on_click)

    def update_edge_cost_label(self):
        self.edge_cost.set(self.edge_model.edge_cost)

    def draw_line(self, color: str ='black'):
        self.line = self.canvas_parent.create_line([self.edge_model.start_node.x_coord, self.edge_model.start_node.y_coord,
                           self.edge_model.end_node.x_coord, self.edge_model.end_node.y_coord],
                           tag=('line' + f'{self.edge_model.edge_id}'), arrow='last', width=3, fill=f'{color}')

    def change_to_selected_color(self):
        self.canvas_parent.itemconfig(self.line, fill='red')

    def change_to_default_color(self):
        self.canvas_parent.itemconfig(self.line, fill='black')

    def on_click(self, event):
        if self.line is not None:  # a line was clicked
            self.change_to_selected_color()
        if self.on_line_click is not None:
            self.on_line_click()