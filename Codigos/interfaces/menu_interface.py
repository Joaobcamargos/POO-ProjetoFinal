from abc import ABC, abstractmethod

class MenuI(ABC):
    @abstractmethod
    def iniciarMenu(self, objeto: object) -> None:
        pass
