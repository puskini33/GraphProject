from abc import ABC, abstractmethod


class PresenterBase(ABC):

    @abstractmethod
    def load_view(self) -> None:
        pass

    @abstractmethod
    def destroy_view(self) -> None:
        pass
