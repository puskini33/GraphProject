from tkinter import *


class DrawLine(object):

    def __init__(self, canvas):
        self.canvas = canvas
        self.click_number = 0
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
        self.bind_left_button_to_line()

    def bind_left_button_to_line(self):
        self.canvas.bind('<Button-1>', self.draw_line)

    def draw_line(self, event):
        if self.click_number == 0:
            self.x1 = event.x
            self.y1 = event.y
            self.click_number = 1
        else:
            self.x2 = event.x
            self.y2 = event.y
            self.canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill='black', width=3)
            self.click_number = 0
