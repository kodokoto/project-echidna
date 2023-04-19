from abc import ABC, abstractmethod

class Visible(ABC):
    @abstractmethod
    def render(self):
        pass