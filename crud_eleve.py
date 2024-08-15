from abc import ABC, abstractmethod


class CRUDEleve(ABC):
    @abstractmethod
    def ajouter(self, eleve):
        pass

    @abstractmethod
    def mettreAJour(self, eleve):
        pass

    @abstractmethod
    def supprimer(self, identifiant: int):
        pass

    @abstractmethod
    def obtenirEleve(self):
        pass

    @abstractmethod
    def obtenir(self, identifiant: int):
        pass
