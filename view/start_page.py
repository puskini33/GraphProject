from view.application_runner import GraphItApp
from tkinter import *
import view


class StartPage(Frame):
    def __init__(self, master: GraphItApp):
        Frame.__init__(self, master, width=1280, height=720)
        self.config(background='antique white')
        welcome_label = Label(self, text='Welcome to the GraphIt Application!', bg='antique white', font=("Courier", 15))
        draw_button = Button(self, text='Draw Graph', bd=15, bg='DeepSkyBlue3', fg='white', width=15,
                             font='bold', command=lambda: master.switch_frame(view.new_graph_canvas.NewGraphCanvas))
        load_button = Button(self, text='Load Graph', bd=15, bg='DeepSkyBlue3', fg='white', width=15,
                             font='bold', command=lambda: master.switch_frame(view.graph_selection_page.GraphSelectionPage))
        quit_button = Button(self, text='Quit', bd=7, bg='DeepSkyBlue3', fg='white', pady=3,
                             command=master.destroy)

        welcome_label.place(relx=.50, rely=.25, anchor="center")
        draw_button.place(relx=.35, rely=.55, anchor="center")
        load_button.place(relx=.65, rely=.55, anchor="center")
        quit_button.place(relx=.99, rely=.89, anchor="e")