from contracts.presenters.abstract_presenter_base import AbstractPresenterBase
from view.application_runner import GraphItAppView
import presenters


class GraphItAppPresenter(object):

    def __init__(self):
        self.view: GraphItAppView = GraphItAppView()
        self.application_name: str = 'GraphIt'
        self.application_geometry: str = "1000x500-450+250"
        self.init_view()
        self.current_child_presenter: AbstractPresenterBase or None = None
        self.go_to_start_page()

    def init_view(self):
        self.view.set_application_title(self.application_name)
        self.view.set_application_geometry(self.application_geometry)

    def get_root_view(self) -> GraphItAppView:
        return self.view

    def go_to_draw_page(self):
        self.destroy_current_child_presenter()

    def go_to_load_page(self):
        pass

    def close_application(self, event):
        self.view.destroy_root_view()

    def go_to_start_page(self):
        self.destroy_current_child_presenter()
        self.current_child_presenter = presenters.start_page_presenter.StartPagePresenter(self)
        self.current_child_presenter.load_view()

    def destroy_current_child_presenter(self):
        if self.current_child_presenter is not None:
            self.current_child_presenter.destroy_view()

    def run(self):
        self.view.mainloop()
