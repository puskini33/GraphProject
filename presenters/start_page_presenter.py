import presenters
from views.start_page_view import StartPageView
from contracts.presenters.presenter_base import PresenterBase
from models.common_models.view_navigation_parameter import ViewNavigationParameter
from models.enums.graph_canvas_state import GraphCanvasState


class StartPagePresenter(PresenterBase):

    def __init__(self, root_presenter: presenters.graph_it_app_presenter.GraphItAppPresenter) -> None:
        self.root_presenter: presenters.graph_it_app_presenter.GraphItAppPresenter = root_presenter

        self.view: StartPageView = StartPageView(self.root_presenter.get_root_view())
        self.view.draw_button.bind('<Button-1>', self.go_to_graph_canvas_page)
        self.view.load_button.bind('<Button-1>', self.root_presenter.go_to_load_page)
        self.view.quit_button.bind('<Button-1>', self.root_presenter.close_application)

    def go_to_graph_canvas_page(self, event) -> None:
        view_parameter = ViewNavigationParameter(GraphCanvasState.new)
        self.root_presenter.go_to_graph_canvas_page(view_parameter)

    def load_view(self) -> None:
        self.view.load_frame()

    def destroy_view(self) -> None:
        self.view.destroy_frame()


