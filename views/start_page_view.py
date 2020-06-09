from contracts.views.view_base import ViewBase
from tkinter import *


class StartPageView(ViewBase, Frame):

    def __init__(self, root: Tk) -> None:
        Frame.__init__(self, root)

        self.config(background='antique white', width=1280, height=720)
        self.welcome_label = Label(self, text='Welcome to the GraphIt Application!', bg='antique white', font=("Courier", 15))
        self.draw_button = Button(self, text='Draw Graph', bd=15, bg='DeepSkyBlue3', fg='white', width=15,
                                  font='bold')
        self.load_button = Button(self, text='Load Graph', bd=15, bg='DeepSkyBlue3', fg='white', width=15,
                                  font='bold')
        self.quit_button = Button(self, text='Quit', bd=7, bg='DeepSkyBlue3', fg='white', pady=3)

        self.place_widgets()

    def place_widgets(self) -> None:
        self.welcome_label.place(relx=.50, rely=.25, anchor="center")
        self.draw_button.place(relx=.35, rely=.55, anchor="center")
        self.load_button.place(relx=.65, rely=.55, anchor="center")
        self.quit_button.place(relx=.99, rely=.89, anchor="e")

    def load_frame(self) -> None:
        self.pack()

    def destroy_frame(self) -> None:
        self.destroy()