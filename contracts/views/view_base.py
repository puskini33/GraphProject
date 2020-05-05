from abc import ABC, abstractmethod


class ViewBase(ABC):

    @abstractmethod
    def place_widgets(self) -> None:
        pass

    @abstractmethod
    def load_frame(self) -> None:
        pass

    @abstractmethod
    def destroy_frame(self) -> None:
        pass
