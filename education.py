from abc import ABC, abstractmethod

class Education(ABC):
    @abstractmethod
    def enseigner(self, matiere: str) -> str:
        pass

    @abstractmethod
    def preparerCours(self, cours: str) -> str:
        pass

    @abstractmethod
    def assisterReunion(self, sujet: str) -> str:
        pass