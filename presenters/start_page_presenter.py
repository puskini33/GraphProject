import presenters
from view.start_page import StartPageView
from contracts.presenters.abstract_presenter_base import AbstractPresenterBase


class StartPagePresenter(AbstractPresenterBase):

    def __init__(self, root_presenter: presenters.graph_it_app_presenter.GraphItAppPresenter):
        self.root_presenter: presenters.graph_it_app_presenter.GraphItAppPresenter = root_presenter
        self.view: StartPageView = StartPageView(self.root_presenter.get_root_view())
        self.view.draw_button.bind('<Button-1>', self.root_presenter.go_to_draw_page)
        self.view.load_button.bind('<Button-1>', self.root_presenter.go_to_load_page)
        self.view.quit_button.bind('<Button-1>', self.root_presenter.close_application)

    def load_view(self):
        self.view.load_frame()

    def destroy_view(self):
        self.view.destroy_frame()


