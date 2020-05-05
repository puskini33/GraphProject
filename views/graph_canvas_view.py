from contracts.views.view_base import ViewBase
from tkinter import *


class GraphCanvasView(ViewBase, Frame):

    def __init__(self, root: Tk):
        Frame.__init__(self, root)
        self.configure(width=1000, height=800, background='antique white')
        self.save_button = Button(self, text='Save Graph', bg='DeepSkyBlue3', fg='white', width=10,
                                  font='bold')  # command=self.save_new_graph
        self.back_button = Button(self, text="Back", bg='DeepSkyBlue3', fg='white', width=10,
                                  font='bold')  # command=action_with_arg
        self.label1 = Label(self, text="Introduce Graph Name:",  bg='antique white', font=('Helvetica', 8, "bold"))
        self.entry_graph_name = Entry(self, font='yellow', width=10)
        # ToDo: self.graph_view.entry_graph_name = self.entry_graph_name
        self.place_widgets()

    def place_widgets(self) -> None:
        self.back_button.place(relx=.99, rely=.50, anchor="e")
        self.save_button.place(relx=.99, rely=.35, anchor="e")
        self.label1.place(relx=0.93, rely=.10, anchor='n')
        self.entry_graph_name.place(relx=0.93, rely=.15, anchor='n')

    def load_frame(self) -> None:
        self.pack()

    def destroy_frame(self) -> None:
        self.destroy()