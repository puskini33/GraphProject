from tkinter import *
import view
from view.presenter import BackendSetup
from typing import List, Tuple
from view.loaded_graph_canvas import LoadedGraphCanvas


class GraphSelectionPage(Frame):
    def __init__(self, master):
        self.master = master
        self.backend = BackendSetup()
        Frame.__init__(self, self.master)
        GraphSelectionPage.configure(self, width=700, height=800)

        self.label1 = Label(self, text="Please select a graph to upload: ", font=("Courier", 17))
        load_button = Button(self, text="Load Graph", bg='DeepSkyBlue4', fg='white', width=10,
                             font='bold', command=self.get_id_selected_graph)
        back_button = Button(self, text="Back", bg='DeepSkyBlue4', fg='white', width=10,
                             font='bold', command=lambda: self.master.switch_frame(view.start_page.StartPage))

        self.listbox = Listbox(self, font=("Courier", 10), highlightcolor='black', highlightthickness=2, relief='ridge')

        self.listbox.place(relx=.50, rely=.45, anchor="center")
        back_button.place(relx=.53, rely=.75)
        load_button.place(relx=.33, rely=.75)
        self.label1.place(relx=.20, rely=.15)

        graph_options = self.get_graphs_from_repository()
        for item in graph_options:
            self.listbox.insert(END, item)

    def get_graphs_from_repository(self) -> List[Tuple]:
        return self.backend.graph_repository.get_all_graphs()

    def get_id_selected_graph(self):
        selected_graph_value = self.listbox.curselection()
        if selected_graph_value:
            graph_id = selected_graph_value[0] + 1
            self.switch_frame(graph_id)
        else:
            self.label1.configure(fg='red')

    def switch_frame(self, graph_id):
        self.master.switch_frame(LoadedGraphCanvas, graph_id)