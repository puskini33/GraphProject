from models.enums.graph_canvas_state import GraphCanvasState


class ViewNavigationParameter(object):

    def __init__(self, graph_canvas_state: GraphCanvasState, graph_id: int = -1):
        self.graph_canvas_state: GraphCanvasState = graph_canvas_state
        self.graph_id: int = graph_id
