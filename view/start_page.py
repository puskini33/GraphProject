from view.application_runner import GraphItAppView
from tkinter import *
import view


class StartPageView(Frame):
    def __init__(self, root: Tk):
        Frame.__init__(self, root)

        self.config(background='antique white', width=1280, height=720)
        self.welcome_label = Label(self, text='Welcome to the GraphIt Application!', bg='antique white', font=("Courier", 15))
        self.draw_button = Button(self, text='Draw Graph', bd=15, bg='DeepSkyBlue3', fg='white', width=15,
                             font='bold')  # command=lambda: root.switch_frame(view.new_graph_canvas.NewGraphCanvas)
        self.load_button = Button(self, text='Load Graph', bd=15, bg='DeepSkyBlue3', fg='white', width=15,
                             font='bold')  # command=lambda: root.switch_frame(view.graph_selection_page.GraphSelectionPage)
        self.quit_button = Button(self, text='Quit', bd=7, bg='DeepSkyBlue3', fg='white', pady=3)  # command=root.destroy

        self.place_widgets()

    def place_widgets(self):
        self.welcome_label.place(relx=.50, rely=.25, anchor="center")
        self.draw_button.place(relx=.35, rely=.55, anchor="center")
        self.load_button.place(relx=.65, rely=.55, anchor="center")
        self.quit_button.place(relx=.99, rely=.89, anchor="e")

    def load_frame(self):
        self.pack()

    def destroy_frame(self):
        self.destroy()