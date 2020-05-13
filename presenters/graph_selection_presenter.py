from views.graph_selection_view import GraphSelectionView
from contracts.presenters.presenter_base import PresenterBase
from models.common_models.view_navigation_parameter import ViewNavigationParameter
from models.enums.graph_canvas_state import GraphCanvasState
import presenters


class GraphSelectionPresenter(PresenterBase):

    def __init__(self, root_presenter: presenters.graph_it_app_presenter.GraphItAppPresenter) -> None:
        self.root_presenter: presenters.graph_it_app_presenter.GraphItAppPresenter = root_presenter
        self.view: GraphSelectionView = GraphSelectionView(self.root_presenter.get_root_view())
        self.graph_canvas_state = GraphCanvasState(2)
        self.view_parameter = ViewNavigationParameter(self.graph_canvas_state)
        self.view.load_button.bind('<Button-1>', self.go_to_graph_canvas_page)
        self.view.back_button.bind('<Button-1>', self.root_presenter.go_to_start_page)

    def go_to_graph_canvas_page(self, event):
        if type(self.get_selected_graph_id()) == int:
            return self.root_presenter.go_to_graph_canvas_page(self.view_parameter)

    def get_selected_graph_id(self) -> int:
        graph_id = self.view.get_id_selected_graph()
        self.view_parameter.graph_id = graph_id
        return graph_id

    def load_view(self) -> None:
        self.view.load_frame()

    def destroy_view(self) -> None:
        self.view.destroy_frame()