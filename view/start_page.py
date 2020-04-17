from tkinter import *
import view
from view.application_runner import GraphItApp


class StartPage(Frame):
    def __init__(self, master: GraphItApp):

        Frame.__init__(self, master, width=1280, height=720)
        self.config(background='light cyan')
        welcome_label = Label(self, text='Welcome to the GraphIt application!', font=("Courier", 15))
        draw_button = Button(self, text='Draw Graph', bd=15, bg='DeepSkyBlue4', fg='white', width=15,
                             font='bold', command=lambda: master.switch_frame(view.new_graph_canvas.NewGraphCanvas))
        load_button = Button(self, text='Load Graph', bd=15, bg='DeepSkyBlue4', fg='white', width=15,
                             font='bold', command=lambda: master.switch_frame(view.load_page.GraphSelectionPage))
        quit_button = Button(self, text='Quit', bd=7, bg='DeepSkyBlue4', fg='white', pady=3,
                             command=master.destroy)

        welcome_label.place(relx=.50, rely=.25, anchor="center")
        draw_button.place(relx=.35, rely=.55, anchor="center")
        load_button.place(relx=.65, rely=.55, anchor="center")
        quit_button.place(relx=.99, rely=.89, anchor="e")