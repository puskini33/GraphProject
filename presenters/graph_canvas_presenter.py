from contracts.presenters.presenter_base import PresenterBase
from views.graph_canvas_view import GraphCanvasView
import presenters
from application_service.graph_application_service_factory import GraphAppServiceFactory
from views.graph_view_init import GraphViewInit
from models.common_models.view_navigation_parameter import ViewNavigationParameter
from models.enums.graph_canvas_state import GraphCanvasState
from models.graph_model import GraphModel


class GraphCanvasPresenter(PresenterBase):

    def __init__(self,  root_presenter: presenters.graph_it_app_presenter.GraphItAppPresenter, view_parameter: ViewNavigationParameter):
        self.root_presenter: presenters.graph_it_app_presenter.GraphItAppPresenter = root_presenter
        self.view: GraphCanvasView = GraphCanvasView(self.root_presenter.get_root_view())
        self.view.save_button.bind('<Button-1>', self.save_graph)
        self.view.back_button.bind('<Button-1>', self.root_presenter.go_to_start_page)

        self.graph_app_service = GraphAppServiceFactory.get_instance()
        if view_parameter.graph_canvas_state == GraphCanvasState.new:
            self.graph_model = GraphModel()
            
        self.graph_view_init = GraphViewInit(self.graph_model, self.graph_app_service, self.view)

    def load_view(self) -> None:
        self.view.load_frame()

    def destroy_view(self) -> None:
        self.view.destroy_frame()

    def save_graph(self, event):
        self.graph_view_init.save_graph_name(event)

    def load_graph_model(self, graph_id: int) -> GraphModel:
        loaded_graph_model = GraphAppServiceFactory.graph_app_service.get_graph_model(graph_id)
        return loaded_graph_model
