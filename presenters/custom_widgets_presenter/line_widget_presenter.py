from views.custom_widgets_view.line_widget_view import LineWidgetView
from helpers.utils import get_middle_point_of_line
from models.edge_model import EdgeModel
from typing import Callable
from tkinter import Canvas


class LineWidgetPresenter(object):

    def __init__(self, on_line_click: Callable, edge_model: EdgeModel, canvas: Canvas) -> None:
        self.edge_model = edge_model
        self.on_line_click = on_line_click
        self.canvas = canvas
        self.view: LineWidgetView = LineWidgetView(self.canvas, self.edge_model, self.on_line_click_presenter)
        self.view.draw_line()
        self.init_view_elements()

    def init_view_elements(self) -> None:
        center_line_coordinates = get_middle_point_of_line(self.edge_model.start_node, self.edge_model.end_node)
        self.view.place_widget(center_line_coordinates)
        self.view.bind_line_label_to_click()

    def on_line_click_presenter(self) -> None:
        self.on_line_click(self)
