from tkinter import *


def reset_circle():
    global clicked_circles
    clicked_circles = []


def select_circles(event):
    x, y = event.x, event.y
    selection = my_canvas.find_overlapping(x, y, x, y)
    if len(selection) == 0:
        return
    elif len(selection) != 0 and len(clicked_circles) < 2:
        clicked_circles.append(selection)
    if len(clicked_circles) == 2:
        if all(clicked_circles):
            join_circles()
    elif len(clicked_circles) == 2 and clicked_circles[0] == clicked_circles[1]:
        return


def join_circles():
    global clicked_circles
    coordinates = []
    for circle in clicked_circles:
        try:
            x, y = find_center(circle)
            coordinates.append(x)
            coordinates.append(y)
        except TypeError:
            reset_circle()
            return
    my_canvas.create_line(coordinates, tag='all')
    reset_circle()


def find_center(item):
    if my_canvas.bbox(item) is None:
        return
    x0, y0, x1, y1 = my_canvas.bbox(item)
    coord_x = ((x0 + 0.01) + (x1 + 0.01)) / 2
    coord_y = ((y0 + 0.01) + (y1 + 0.01)) / 2
    return coord_x, coord_y


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