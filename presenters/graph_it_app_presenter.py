from contracts.presenters.presenter_base import PresenterBase
from views.graph_it_app_view import GraphItAppView
from models.common_models.view_navigation_parameter import ViewNavigationParameter
import presenters


class GraphItAppPresenter(object):

    def __init__(self) -> None:
        self.view: GraphItAppView = GraphItAppView()
        self.application_name: str = 'GraphIt'
        self.application_geometry: str = "1000x500-450+250"
        self.init_view()
        self.current_child_presenter: PresenterBase or None = None
        self.go_to_start_page(event=None)

    def init_view(self) -> None:
        self.view.set_application_title(self.application_name)
        self.view.set_application_geometry(self.application_geometry)

    def get_root_view(self) -> GraphItAppView:
        return self.view

    def go_to_graph_canvas_page(self, view_parameter: ViewNavigationParameter) -> None:
        self.destroy_current_child_presenter()
        self.current_child_presenter = presenters.graph_canvas_presenter.GraphCanvasPresenter(self, view_parameter)
        self.current_child_presenter.load_view()

    def go_to_load_page(self, event) -> None:
        self.destroy_current_child_presenter()
        self.current_child_presenter = presenters.graph_selection_presenter.GraphSelectionPresenter(self)
        self.current_child_presenter.load_view()

    def close_application(self, event) -> None:
        self.view.destroy_root_view()

    def go_to_start_page(self, event) -> None:
        self.destroy_current_child_presenter()
        self.current_child_presenter = presenters.start_page_presenter.StartPagePresenter(self)
        self.current_child_presenter.load_view()

    def destroy_current_child_presenter(self) -> None:
        if self.current_child_presenter is not None:
            self.current_child_presenter.destroy_view()

    def run(self) -> None:
        self.view.mainloop()
