from contracts.views.view_base import ViewBase
from tkinter import *


class GraphCanvasView(ViewBase, Frame):

    def __init__(self, root: Tk):
        Frame.__init__(self, root)
        self.configure(width=1000, height=800, background='antique white')

        self.save_button = Button(self, text='Save Graph', bg='DeepSkyBlue3', fg='white', width=10,
                                  font='bold')
        self.back_button = Button(self, text="Back", bg='DeepSkyBlue3', fg='white', width=10,
                                  font='bold')
        self.label = Label(self, text="Introduce Graph Name:",  bg='antique white', font=('Helvetica', 8, "bold"))
        self.entry_graph_name = Entry(self, font='yellow', width=10)
        self.canvas = Canvas(self, bg='white', cursor='arrow')

        self.place_widgets()

    def place_widgets(self) -> None:
        self.back_button.place(relx=.99, rely=.50, anchor="e")
        self.save_button.place(relx=.99, rely=.35, anchor="e")
        self.label.place(relx=0.93, rely=.10, anchor='n')
        self.canvas.place(width=850, height=500)
        self.entry_graph_name.place(relx=0.93, rely=.15, anchor='n')

    def draw_circle(self, coordinates, circle_radius):
        self.canvas.create_oval(coordinates[0] - circle_radius, coordinates[1] - circle_radius,
                                coordinates[0] + circle_radius, coordinates[1] + circle_radius, fill='chocolate1', width=3, tag='all')

    def draw_line(self, coordinates):
        self.canvas.create_line(coordinates, tag='all', arrow='last', width=3)

    def load_frame(self) -> None:
        self.pack()

    def destroy_frame(self) -> None:
        self.destroy()