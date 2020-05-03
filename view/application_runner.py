from tkinter import *
import view


class GraphItAppView(Tk):

    def __init__(self):
        Tk.__init__(self)

    def set_application_title(self, application_title: str):
        self.title(application_title)

    def set_application_geometry(self, application_geometry: str):
        self.geometry(application_geometry)

    def destroy_root_view(self):
        self.destroy()

    """def switch_frame(self, frame_class, graph_id=None):  # refractor
        if frame_class and type(graph_id) == int:
            new_frame = frame_class(self, graph_id)
            if self._frame:
                self._frame.destroy()
            self._frame = new_frame
            self._frame.pack()
        elif frame_class and not graph_id:
            new_frame = frame_class(self)
            if self._frame:
                self._frame.destroy()
            self._frame = new_frame
            self._frame.pack()"""


