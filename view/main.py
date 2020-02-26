from tkinter import *


def draw_line(event):

    x, y = event.x, event.y
    if my_canvas.old_coordinates:
        x1, y1 = my_canvas.old_coordinates
        my_canvas.create_line(x, y, x1, y1, fill='black', width=3)
        my_canvas.old_coordinates = None
        return
    my_canvas.old_coordinates = x, y


def draw_circle(event):
    x, y = event.x, event.y
    my_canvas.create_oval(x, y, x + 50, y + 50, fill='black', width=3)


my_window = Tk()
my_canvas = Canvas(my_window, width=600, height=600, bg='white')
my_canvas.grid(row=0, column=0)
my_canvas.old_coordinates = None
my_canvas.bind('<Button-1>', draw_line)
my_canvas.bind('<Button-3>', draw_circle)
my_window.mainloop()
