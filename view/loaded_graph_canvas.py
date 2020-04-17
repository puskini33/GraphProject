from view.application_runner import GraphItApp
from view.presenter import BackendSetup
from view.graph_view import UIInitialization
from functools import partial
from tkinter import *
import view


class LoadedGraphCanvas(Frame):
    counter_id = -1

    def __init__(self, master: GraphItApp, graph_id):
        Frame.__init__(self, master)
        self.configure(width=850, height=800)
        save_button = Button(self, text='Save Graph', bg='DeepSkyBlue4', fg='white', width=10,
                             font='bold', command=self.save_new_graph)
        action_with_arg = partial(master.switch_frame, view.start_page.StartPage)
        back_button = Button(self, text="Back", bg='DeepSkyBlue4', fg='white', width=10,
                             font='bold', command=action_with_arg)

        self.graph_id = graph_id
        self.backend = BackendSetup()
        self.graph_app_service = BackendSetup.graph_app_service
        self.graph_model = self.backend.load_graph(self.graph_id)

        self.canvas = Canvas(self, bg='white', cursor='arrow')
        self.canvas.place(width=700, height=500)
        back_button.place(relx=.99, rely=.50, anchor="e")
        save_button.place(relx=.99, rely=.35, anchor="e")

        self.UI_initialize = UIInitialization(self.graph_model, self.graph_app_service, self.canvas)

    def save_new_graph(self):
        self.UI_initialize.save_graph_name()
