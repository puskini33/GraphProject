from tkinter import *


from view.draw_circle import DrawCircle
from view.draw_line import DrawLine

my_window = Tk()
my_canvas = Canvas(my_window, width=600, height=600, bg='white')
my_canvas.grid(row=0, column=0)
my_drawn_circle = DrawCircle(my_canvas)
my_drawn_line = DrawLine(my_canvas)
my_window.mainloop()