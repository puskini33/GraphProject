from tkinter import *


def reset_circle():
    global clicked_circles
    for circle in clicked_circles:
        my_canvas.itemconfigure(circle, fill='black')
    clicked_circles = []


def select_circles(event):
    x, y = event.x, event.y
    selection = my_canvas.find_overlapping(x, y, x, y)
    if selection is not None and len(clicked_circles) < 2:
        clicked_circles.append(selection)
    if len(clicked_circles) == 2:
        if all(clicked_circles):
            join_circles()


def join_circles():
    coordinates = []
    for circle in clicked_circles:
        x, y = find_center(circle)
        coordinates.append(x)
        coordinates.append(y)
    my_canvas.create_line(coordinates, tag='all')
    reset_circle()


def find_center(item):
    x0, y0, x1, y1 = my_canvas.bbox(item)
    return ((x0 + 0.01) + (x1 + 0.01)) / 2, ((y0 + 0.01) + (y1 + 0.01)) / 2


def draw_oval(event):
    x, y = event.x, event.y
    my_canvas.create_oval(x - 25, y - 25, x + 25, y + 25, fill='black', width=3, tag='all')

def delete_all(event):
    my_canvas.delete('all')

my_window = Tk()
my_canvas = Canvas(my_window, width=600, height=600, bg='white')
my_canvas.grid(row=0, column=0)
my_canvas.old_coordinates = None
my_canvas.bind('<Button-3>', draw_oval)
my_canvas.bind('<Button-1>', select_circles)
my_canvas.bind('<Button-2>', delete_all)

clicked_circles = []
my_window.mainloop()