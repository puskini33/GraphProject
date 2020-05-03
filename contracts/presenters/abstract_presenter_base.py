from abc import ABC, abstractmethod


class AbstractPresenterBase(ABC):

    @abstractmethod
    def load_view(self):
        pass

    @abstractmethod
    def destroy_view(self):
        pass
