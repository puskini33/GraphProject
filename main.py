from tkinter import *
from view.graph_view import GraphView
from models.graph_model import GraphModel
from application_service.graph_application_service import GraphApplicationService
from business_service.graph_business_service import GraphBusinessService
from business_service.node_business_service import NodeBusinessService
from business_service.edge_business_service import EdgeBusinessService
from repository_service.graph_repository import GraphRepository
from repository_service.node_repository import NodeRepository
from repository_service.edge_repository import EdgeRepository



"""def load_graph():

    graph_repository = GraphRepository()
    node_repository = NodeRepository()
    edge_repository = EdgeRepository()
    graph_business_service = GraphBusinessService(graph_repository)
    node_business_service = NodeBusinessService(node_repository)
    edge_business_service = EdgeBusinessService(edge_repository)

    trial_graph_app_service = GraphApplicationService(graph_business_service, node_business_service,
                                                      edge_business_service)

    saved_graph_model = trial_graph_app_service.save_graph_model(unsaved_graph_model)

    graph_view = GraphView(app_window, saved_graph_model, trial_graph_app_service)


def save_graph(app_window):
    init_second_window(app_window)
    graph_repository = GraphRepository()
    node_repository = NodeRepository()
    edge_repository = EdgeRepository()
    graph_business_service = GraphBusinessService(graph_repository)
    node_business_service = NodeBusinessService(node_repository)
    edge_business_service = EdgeBusinessService(edge_repository)
    unsaved_graph_model = GraphModel()

    trial_graph_app_service = GraphApplicationService(graph_business_service, node_business_service,
                                                      edge_business_service)
    GraphView(app_window, unsaved_graph_model, trial_graph_app_service)
"""


class FirstWindow(object):
    def __init__(self, master, geometry):
        self.master = master
        self.frame = Frame(self.master)
        self.window_geometry = geometry
        self.label = Label(self.master, text='Welcome to the GraphIt application!', font=("Courier", 15), height=15)
        self.draw_button = Button(self.master, text='Draw Graph', bd=15, bg='black', fg='white', pady=15, width=15,
                                  font='bold', command=self.draw_graph)
        self.load_button = Button(self.master, text='Load Graph', bd=15, bg='black', fg='white', pady=15, width=15,
                                  font='bold')
        self.label.pack()
        self.draw_button.pack()
        self.draw_button.place(relx=.35, rely=.65, anchor="center")
        self.load_button.pack()
        self.load_button.place(relx=.65, rely=.65, anchor="center")
        self.frame.pack()

    def draw_graph(self):
        self.master.destroy()
        draw_window = Tk()
        draw_window.title('DrawGraph')
        draw_window.geometry(self.window_geometry)
        frame = Frame(draw_window)
        save_button = Button(draw_window, text='Save Graph', bd=5, bg='black', fg='white', pady=5, width=15,
                             font='bold', command=draw_window.destroy)
        quit_button = Button(draw_window, text='Quit GraphIt', bd=5, bg='black', fg='white', pady=5, width=15,
                             font='bold', command=draw_window.destroy)
        save_button.pack()
        save_button.place(relx=.95, rely=.35, anchor="e")
        quit_button.pack()
        quit_button.place(relx=.95, rely=.65, anchor="e")
        frame.pack()


if __name__ == '__main__':
    app_window = Tk()
    app_window.title('GraphIt')
    window_width = app_window.winfo_reqwidth()
    window_height = app_window.winfo_reqheight()
    position_right = int(app_window.winfo_screenwidth() / 2 - window_width / 2)
    position_down = int(app_window.winfo_screenheight() / 2 - window_height / 2)
    app_window.geometry(f"{position_right}x{position_down}")
    geometry = f"{position_right}x{position_down}"
    app = FirstWindow(app_window, geometry)
    app_window.mainloop()






