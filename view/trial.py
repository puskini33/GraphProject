from tkinter import filedialog
from tkinter import *


class GraphView(Frame):

    def __init__(self, window):
        self.window = window
        self.canvas = Canvas(self.window, width=700, height=700, bg='white')
        self.clicked_circles = []
        self.changes = [""]
        self.steps = int()
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.canvas.grid(row=0, column=0)
        self.canvas.old_coordinates = None
        self.canvas.bind('<Button-3>', self.draw_oval)
        self.canvas.bind('<Button-1>', self.select_circles)
        self.canvas.bind('<Button-2>', self.delete_all)
        # self.bind("<Control-z>", self.undo)
        # self.bind("<Key>", self.add_changes)

        self.master.title('GraphIt')
        menu_bar = Menu(self.master)
        self.master.config(menu=menu_bar)

        drop_down_menu = Menu(menu_bar)
        menu_bar.add_cascade(label="File", menu=drop_down_menu)
        # drop_down_menu.add_command(label="Undo", command=self.undo)
        drop_down_menu.add_command(label="Open..", command=self.open_graphit)
        drop_down_menu.add_command(label="Exit", command=self.exit_graphit)

    """def undo(self, event=None):
        if self.steps != 0:
            self.steps -= 1
            self.delete(0, END)
            self.insert(END, self.changes[self.steps])

    def add_changes(self, event=None):
        if self.get() != self.changes[-1]:
            self.changes.append(self.get())
            self.steps += 1"""

    def exit_graphit(self):
        self.quit()

    def open_graphit(self):
        self.window.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                          filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

    def reset_circle(self):
        self.clicked_circles = []

    def select_circles(self, event):
        x, y = event.x, event.y
        selection = self.canvas.find_overlapping(x, y, x, y)
        if len(selection) == 0:
            return
        elif len(selection) != 0 and len(self.clicked_circles) < 2:
            self.clicked_circles.append(selection)
        if len(self.clicked_circles) == 2:
            if all(self.clicked_circles):
                self.join_circles()
        elif len(self.clicked_circles) == 2 and self.clicked_circles[0] == self.clicked_circles[1]:
            return

    def join_circles(self):
        coordinates = []
        for circle in self.clicked_circles:
            try:
                x, y = self.find_center(circle)
                coordinates.append(x)
                coordinates.append(y)
            except TypeError:
                self.reset_circle()
                return
        self.canvas.create_line(coordinates, tag='all', arrow='last', width=3)
        self.reset_circle()

    def find_center(self, item):
        if self.canvas.bbox(item) is None:
            return
        x0, y0, x1, y1 = self.canvas.bbox(item)
        coord_x = ((x0 + 0.01) + (x1 + 0.01)) / 2
        coord_y = ((y0 + 0.01) + (y1 + 0.01)) / 2
        return coord_x, coord_y

    def draw_oval(self, event):
        x, y = event.x, event.y
        self.canvas.create_oval(x - 25, y - 25, x + 25, y + 25, fill='orange', width=3, tag='all')

    def delete_all(self, event):
        self.canvas.delete('all')


