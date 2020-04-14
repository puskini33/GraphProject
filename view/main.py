from models.graph_model import GraphModel
from application_service.graph_application_service import GraphApplicationService
from business_service.graph_business_service import GraphBusinessService
from business_service.node_business_service import NodeBusinessService
from business_service.edge_business_service import EdgeBusinessService
from repository_service.graph_repository import GraphRepository
from repository_service.node_repository import NodeRepository
from repository_service.edge_repository import EdgeRepository
from typing import List, Tuple
from tkinter import *
import view


class BackendSetup(object):

    graph_repository = GraphRepository()
    node_repository = NodeRepository()
    edge_repository = EdgeRepository()
    graph_business_service = GraphBusinessService(graph_repository)
    node_business_service = NodeBusinessService(node_repository)
    edge_business_service = EdgeBusinessService(edge_repository)
    graph_app_service = GraphApplicationService(graph_business_service, node_business_service, edge_business_service)

    def load_graph(self, graph_id):
        loaded_graph_model = BackendSetup.graph_app_service.get_graph_model(graph_id)
        return loaded_graph_model

    def save_graph(self):
        unsaved_graph_model = GraphModel()
        return unsaved_graph_model


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
        Frame.__init__(self, master, width=1280, height=720)
        self.config(background='light cyan')
        welcome_label = Label(self, text='Welcome to the GraphIt application!', font=("Courier", 15))
        draw_button = Button(self, text='Draw Graph', bd=15, bg='DeepSkyBlue4', fg='white', width=15,
                             font='bold', command=lambda: master.switch_frame(DrawPage))
        load_button = Button(self, text='Load Graph', bd=15, bg='DeepSkyBlue4', fg='white', width=15,
                             font='bold', command=lambda: master.switch_frame(LoadPage))
        quit_button = Button(self, text='Quit', bd=7, bg='DeepSkyBlue4', fg='white', pady=3,
                             command=master.destroy)

        welcome_label.place(relx=.50, rely=.25, anchor="center")
        draw_button.place(relx=.35, rely=.55, anchor="center")
        load_button.place(relx=.65, rely=.55, anchor="center")
        quit_button.place(relx=.99, rely=.89, anchor="e")


class DrawPage(Frame):
    def __init__(self, master):
        self.master = master
        self.backend = BackendSetup()
        master.title('DrawGraph')
        Frame.__init__(self, master)
        self.save_drew_graph()

    def save_drew_graph(self):
        graph_model = self.backend.save_graph()
        view.graph_view.GraphView(self.master, graph_model, BackendSetup.graph_app_service)



class LoadPage(Frame):
    def __init__(self, master):
        self.master = master
        self.backend = BackendSetup()
        Frame.__init__(self, self.master)
        LoadPage.configure(self, width=700, height=800)

        label1 = Label(self, text="Please select a graph to upload: ", font=("Courier", 17))
        load_button = Button(self, text="Load Graph", bg='DeepSkyBlue4', fg='white', width=10,
                             font='bold', command=lambda: [self.load_selected_graph(), self.destroy()])
        back_button = Button(self, text="Back", bg='DeepSkyBlue4', fg='white', width=10,
                             font='bold', command=lambda: self.master.switch_frame(StartPage))
        self.listbox = Listbox(self, font=("Courier", 10), highlightcolor='black', highlightthickness=2, relief='ridge')

        self.listbox.place(relx=.50, rely=.45, anchor="center")
        back_button.place(relx=.53, rely=.75)
        load_button.place(relx=.33, rely=.75)
        label1.place(relx=.20, rely=.15)

        graph_options = self.get_graphs_from_repository()
        for item in graph_options:
            self.listbox.insert(END, item)

    def get_graphs_from_repository(self) -> List[Tuple]:
        return self.backend.graph_repository.get_all_graphs()

    def get_id_selected_graph(self) -> int:
        selected_graph_value = self.listbox.get(ACTIVE)
        graph_id = selected_graph_value[0]
        return graph_id

    def get_graph_model(self) -> GraphModel:
        graph_id = self.get_id_selected_graph()
        graph_model = self.backend.load_graph(graph_id)
        return graph_model

    def load_selected_graph(self):
        graph_model = self.get_graph_model()
        view.graph_view.GraphView(self.master, graph_model, BackendSetup.graph_app_service)


if __name__ == '__main__':
    set_backend = BackendSetup()
    app_window = GraphItApp()
    app_window.title('GraphIt')
    app_window.configure(background='SlateGray3')
    geometry_values = "1000x500-450+250"
    app_window.geometry(geometry_values)
    app_window.mainloop()
