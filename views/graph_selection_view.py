from repository_service.graph_repository import GraphRepository
from contracts.views.view_base import ViewBase
from tkinter import *


class GraphSelectionView(ViewBase, Frame):

    def __init__(self, root: Tk) -> None:
        Frame.__init__(self, root)
        self.configure(width=1280, height=720, background='antique white')

        self.label = Label(self, text="Please select a graph to upload: ", bg='antique white', font=("Courier", 17))
        self.load_button = Button(self, text="Load Graph", bg='DeepSkyBlue3', fg='white', width=10,
                                  font='bold')
        self.back_button = Button(self, text="Back", bg='DeepSkyBlue3', fg='white', width=10,
                                  font='bold')

        self.listbox = Listbox(self, font=("Courier", 10), highlightcolor='black', highlightthickness=2, relief='ridge')

        self.graph_repository = GraphRepository()
        self.populate_listbox()
        self.place_widgets()

    def place_widgets(self):
        self.listbox.place(relx=.50, rely=.45, anchor="center")
        self.back_button.place(relx=.53, rely=.75)
        self.load_button.place(relx=.33, rely=.75)
        self.label.place(relx=.30, rely=.15)

    def populate_listbox(self) -> None:
        graph_options = self.graph_repository.get_all_graphs()
        for item in graph_options:
            self.listbox.insert(END, item)

    def get_id_selected_graph(self) -> int:
        selected_graph_value = self.listbox.curselection()
        if selected_graph_value:
            graph_id = selected_graph_value[0] + 1
            return graph_id
        else:
            self.label.configure(fg='red')

    def load_frame(self) -> None:
        self.pack()

    def destroy_frame(self) -> None:
        self.destroy()