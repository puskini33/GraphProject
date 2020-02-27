import tkinter as tk


class CommandButtons(tk.Frame):
    def __init__(self, master):
        self.master = master
        super().__init__(self.master)
        self.make_circle_btn = tk.Button(root, text='make_circle', command=make_circle)
        self.make_circle_btn.pack()
        self.join_circles_btn = tk.Button(root, text='join_circles', command=select_circles)
        self.join_circles_btn.pack()
        self.pack()


class CircleApp(tk.Frame):
    def __init__(self, master):
        self.master = master
        super().__init__(self.master)
        self.canvas = tk.Canvas(root, width=600, height=600, bg='cyan')
        self.canvas.pack(expand=True, fill=tk.BOTH)
        self.pack()


def make_circle():
    _purge_selection()
    print('cmd make_circle selected')
    c_app.canvas.bind('<Button-1>', _make_circle)


def _make_circle(event):
    c_app.canvas.create_oval(event.x - 25, event.y - 25, event.x + 25, event.y + 25, fill="blue")


def select_circles():
    _purge_selection()
    print('cmd join_circles selected')
    c_app.canvas.bind('<Button-1>', _select_circles)


def _select_circles(event):
    print(f'select circle {event}')
    x, y = event.x, event.y
    selection = c_app.canvas.find_overlapping(x, y, x, y)
    if selection is not None and len(selected_circles) < 2:
        selected_circles.append(selection)
        c_app.canvas.itemconfigure(selection, fill='red')
    if len(selected_circles) == 2:
        if all(selected_circles):
            _join_circles()
        _purge_selection()


def _join_circles():
    coordinates = []
    for item in selected_circles:
        x, y = find_center(item)
        print(x, y)
        coordinates.append(x)
        coordinates.append(y)
    c_app.canvas.create_line(coordinates)


def _purge_selection():
    global selected_circles
    for item in selected_circles:
        c_app.canvas.itemconfigure(item, fill='blue')
    selected_circles = []


def find_center(item):
    x0, y0, x1, y1 = c_app.canvas.bbox(item)
    return (x0 + x1) / 2, (y0 + y1) / 2


if __name__ == '__main__':
    selected_circles = []

    root = tk.Tk()
    command_frame = CommandButtons(root)
    c_app = CircleApp(root)

    root.mainloop()