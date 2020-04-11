from view.graph_view import GraphView
from models.graph_model import GraphModel
from application_service.graph_application_service import GraphApplicationService
from business_service.graph_business_service import GraphBusinessService
from business_service.node_business_service import NodeBusinessService
from business_service.edge_business_service import EdgeBusinessService
from repository_service.graph_repository import GraphRepository
from repository_service.node_repository import NodeRepository
from repository_service.edge_repository import EdgeRepository
from tkinter import *


class SetBackend(object):

    graph_repository = GraphRepository()
    node_repository = NodeRepository()
    edge_repository = EdgeRepository()
    graph_business_service = GraphBusinessService(graph_repository)
    node_business_service = NodeBusinessService(node_repository)
    edge_business_service = EdgeBusinessService(edge_repository)

    def load_graph(self, graph_name):
        trial_graph_app_service = GraphApplicationService(SetBackend.graph_business_service, SetBackend.node_business_service,
                                                          SetBackend.edge_business_service)
    
        loaded_graph_model = trial_graph_app_service.save_graph_model(unsaved_graph_model)
    
        return loaded_graph_model, trial_graph_app_service

    def save_graph(self):
        unsaved_graph_model = GraphModel()

        graph_app_service = GraphApplicationService(SetBackend.graph_business_service, SetBackend.node_business_service,
                                                    SetBackend.edge_business_service)
        return unsaved_graph_model, graph_app_service


class GraphItApp(Tk):

    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class StartPage(Frame):
    def __init__(self, master: GraphItApp):
        Frame.__init__(self, master)
        welcome_label = Label(self, text='Welcome to the GraphIt application!', font=("Courier", 15), height=15)
        draw_button = Button(self, text='Draw Graph', bd=15, bg='black', fg='white', pady=15, width=15,
                             font='bold', command=lambda: master.switch_frame(DrawPage))
        load_button = Button(self, text='Load Graph', bd=15, bg='black', fg='white', pady=15, width=15,
                             font='bold', command=lambda: master.switch_frame(LoadPage))
        welcome_label.pack()
        draw_button.pack()
        draw_button.place(relx=.25, rely=.85, anchor="center")
        load_button.pack()
        load_button.place(relx=.75, rely=.85, anchor="center")


class DrawPage(Frame):
    def __init__(self, master):
        self.backend = SetBackend()
        master.title('DrawGraph')
        Frame.__init__(self, master)
        graph_model, graph_application_service = self.backend.save_graph()
        GraphView(master, graph_model, graph_application_service)


class LoadPage(Frame):
    def __init__(self, master):
        self.backend = SetBackend()
        Frame.__init__(self, master)
        LoadPage.configure(self, width=700, height=800)
        graph_options = self.backend.graph_repository.get_all_graphs()

        label1 = Label(self, text="Please select a graph to upload: ", font=("Courier", 17))
        label1.place(relx=.20, rely=.15)
        # label1.pack()

        load_button = Button(self, text="Load Graph", bd=7, bg='black', fg='white', pady=5, width=10,
                             font='bold', command=lambda: master.switch_frame(StartPage))
        load_button.place(relx=.33, rely=.75)
        back_button = Button(self, text="Back", bd=7, bg='black', fg='white', pady=5, width=10,
                             font='bold', command=lambda: master.switch_frame(StartPage))
        back_button.place(relx=.53, rely=.75)

        listbox = Listbox(self)
        listbox.configure(font=("Courier", 10), highlightcolor='black', highlightthickness=2, relief='ridge')
        listbox.pack()
        listbox.place(relx=.50, rely=.45, anchor="center")
        for item in graph_options:
            listbox.insert(END, item)





    """def __init__(self, master, geometry, backend: SetBackend):
        self.backend = backend
        self.master = master
        self.frame = Frame(self.master)
        # self.frame.grid(row=0, column=0)
        self.window_geometry = geometry
        self.label = Label(self.master, text='Welcome to the GraphIt application!', font=("Courier", 15), height=15)
        self.draw_button = Button(self.master, text='Draw Graph', bd=15, bg='black', fg='white', pady=15, width=15,
                                  font='bold', command=lambda: [self.switch_frame(DrawPage).pack()])
        self.load_button = Button(self.master, text='Load Graph', bd=15, bg='black', fg='white', pady=15, width=15,
                                  font='bold', command=self.get_graph_name)
        self.label.pack()
        self.draw_button.pack()
        self.draw_button.place(relx=.35, rely=.65, anchor="center")
        self.load_button.pack()
        self.load_button.place(relx=.65, rely=.65, anchor="center")
        self.frame.pack()

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self.frame is not None:
            self.frame.destroy()
        self.frame = new_frame
        self.frame.pack()

    def draw_graph(self):
        draw_frame = Frame(self.master)
        # draw_frame.grid(row=0, column=0)
        # draw_window = Tk()
        self.master.title('DrawGraph')

        #graph_model, graph_application_service = self.backend.save_graph()
        #GraphView(draw_frame, graph_model, graph_application_service)

    def load_graph(self):
        self.master.destroy()
        entry_graph_name = self.entry.get()
        if entry_graph_name:
            draw_window = Tk()
            draw_window.title('DrawGraph')
            draw_window.geometry(self.window_geometry)

    def get_graph_name(self):
        pop_up_window = Tk()
        label1 = Label(pop_up_window, text='Enter Graph Name')
        self.entry = Entry(pop_up_window)
        button1 = Button(pop_up_window, text='Load Graph', command=self.load_graph)
        button2 = Button(pop_up_window, text='Quit', command=pop_up_window.destroy)
        label1.grid(row=0, column=0)
        self.entry.grid(row=0, column=1)
        button1.grid(row=1, column=0)
        button2.grid(row=1, column=1)"""


if __name__ == '__main__':
    set_backend = SetBackend()
    app_window = GraphItApp()
    app_window.title('GraphIt')
    app_window.configure(background='SlateGray3')
    geometry_values = "1000x500-450+250"
    app_window.geometry(geometry_values)
    app_window.mainloop()







