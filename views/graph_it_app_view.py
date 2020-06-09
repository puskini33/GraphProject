from tkinter import *


class GraphItAppView(Tk):

    def __init__(self) -> None:
        Tk.__init__(self)

    def set_application_title(self, application_title: str) -> None:
        self.title(application_title)

    def set_application_geometry(self, application_geometry: str) -> None:
        self.geometry(application_geometry)

    def destroy_root_view(self) -> None:
        self.destroy()
