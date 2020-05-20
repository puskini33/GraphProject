from views.graph_selection_view import GraphSelectionView
from contracts.presenters.presenter_base import PresenterBase
from models.common_models.view_navigation_parameter import ViewNavigationParameter
from models.enums.graph_canvas_state import GraphCanvasState
from business_service.graph_business_service import GraphBusinessService
from repository_service.graph_repository import GraphRepository
from models.graph_model import GraphModel
import presenters


class GraphSelectionPresenter(PresenterBase):

    def __init__(self, root_presenter: presenters.graph_it_app_presenter.GraphItAppPresenter) -> None:
        self.root_presenter: presenters.graph_it_app_presenter.GraphItAppPresenter = root_presenter
        self.view: GraphSelectionView = GraphSelectionView(self.root_presenter.get_root_view())
        self.graph_repository = GraphRepository()
        self.graph_business_service = GraphBusinessService(self.graph_repository)
        self.graph_canvas_state = GraphCanvasState(GraphCanvasState.saved)
        self.view_parameter = ViewNavigationParameter(self.graph_canvas_state)
        self.view.load_button.bind('<Button-1>', self.go_to_graph_canvas_page)
        self.view.back_button.bind('<Button-1>', self.root_presenter.go_to_start_page)

        self.all_graph_models = self.graph_business_service.get_all_graph_models()
        self.populate_list()

    def go_to_graph_canvas_page(self, event) -> None:
        selected_graph_model = self.get_selected_graph_model()
        if selected_graph_model is not None:
            self.view_parameter.graph_id = selected_graph_model.graph_id
            self.root_presenter.go_to_graph_canvas_page(self.view_parameter)
        else:
            self.display_warning_message()

    def display_warning_message(self) -> None:
        self.view.change_label_color()

    def get_selected_graph_model(self) -> GraphModel or None:
        item_index = self.view.get_list_selected_index()
        if item_index != -1:
            return self.all_graph_models[item_index]
        else:
            return None

    def populate_list(self) -> None:
        self.view.populate_listbox(self.all_graph_models)

    def load_view(self) -> None:
        self.view.load_frame()

    def destroy_view(self) -> None:
        self.view.destroy_frame()