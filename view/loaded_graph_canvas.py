from view.application_runner import GraphItAppView
from view.presenter import Presenter
from view.graph_view import GraphView
from models.graph_model import GraphModel
from functools import partial
from tkinter import *
import view


class LoadedGraphCanvas(Frame):

    def __init__(self, master: GraphItAppView, graph_id: int):
        Frame.__init__(self, master)
        self.configure(width=1000, height=800, background='antique white')
        save_button = Button(self, text='Save Graph', bg='DeepSkyBlue3', fg='white', width=10,
                             font='bold', command=self.save_new_graph)
        action_with_arg = partial(master.switch_frame, view.start_page.StartPageView)
        back_button = Button(self, text="Back", bg='DeepSkyBlue3', fg='white', width=10,
                             font='bold', command=action_with_arg)

        self.graph_id = graph_id
        self.backend = Presenter()
        self.graph_app_service = self.backend.graph_app_service
        self.graph_model: GraphModel = self.backend.load_graph(self.graph_id)

        self.canvas = Canvas(self, bg='white', cursor='arrow')
        self.canvas.place(width=800, height=500)
        back_button.place(relx=.99, rely=.50, anchor="e")
        save_button.place(relx=.99, rely=.35, anchor="e")

        self.graph_view = GraphView(self.graph_model, self.graph_app_service, self.canvas)

    def save_new_graph(self):
        self.graph_view.save_graph_name()
