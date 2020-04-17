from functools import partial
from tkinter import *
import view
from view.application_runner import GraphItApp
from view.presenter import BackendSetup
from view.graph_view import UIInitialization


class NewGraphCanvas(Frame):
    counter_id = -1

    def __init__(self, master: GraphItApp):
        Frame.__init__(self, master)
        self.configure(width=850, height=800)
        save_button = Button(self, text='Save Graph', bg='DeepSkyBlue4', fg='white', width=10,
                             font='bold', command=self.save_new_graph)
        action_with_arg = partial(master.switch_frame, view.start_page.StartPage)
        back_button = Button(self, text="Back", bg='DeepSkyBlue4', fg='white', width=10,
                             font='bold', command=action_with_arg)

        self.backend = BackendSetup()
        self.graph_app_service = BackendSetup.graph_app_service
        self.graph_model = self.backend.save_graph()

        Label(self, text="Introduce Graph Name:", font=('Helvetica', 8, "bold")).place(relx=0.93, rely=.10, anchor='n')
        self.entry_graph_name = Entry(self, font='yellow', width=10)
        self.entry_graph_name.place(relx=0.93, rely=.15, anchor='n')

        self.canvas = Canvas(self, bg='white', cursor='arrow')
        self.canvas.place(width=700, height=500)
        back_button.place(relx=.99, rely=.50, anchor="e")
        save_button.place(relx=.99, rely=.35, anchor="e")

        self.UI_initialize = UIInitialization(self.graph_model, self.graph_app_service, self.canvas)
        self.UI_initialize.entry_graph_name = self.entry_graph_name

    def save_new_graph(self):
        self.UI_initialize.save_graph_name()