from tkinter import *
import view


class GraphItApp(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.title('GraphIt')
        self.geometry("1000x500-450+250")
        self._frame = None
        self.switch_frame(view.start_page.StartPage)

    def switch_frame(self, frame_class, graph_id=None):  # refractor
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
            self._frame.pack()


