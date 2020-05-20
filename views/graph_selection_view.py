from contracts.views.view_base import ViewBase
from models.graph_model import GraphModel
from typing import List
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
        self.place_widgets()

    def place_widgets(self) -> None:
        self.listbox.place(relx=.50, rely=.45, anchor="center")
        self.back_button.place(relx=.53, rely=.75)
        self.load_button.place(relx=.33, rely=.75)
        self.label.place(relx=.30, rely=.15)

    def populate_listbox(self, all_graphs: List[GraphModel]) -> None:
        for item in all_graphs:
            self.listbox.insert(END, (item.graph_id, item.graph_name))

    def get_list_selected_index(self) -> int:
        selected_item = self.listbox.curselection()
        if len(selected_item) != 0:
            return selected_item[0]
        else:
            return -1

    def change_label_color(self) -> None:
        self.label.configure(fg='red')

    def load_frame(self) -> None:
        self.pack()

    def destroy_frame(self) -> None:
        self.destroy()