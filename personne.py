from datetime import datetime

class Personne:
    def __init__(self, id, dateNaissance, ville, prenom, nom, telephone):
        self.id = id
        self.dateNaissance = dateNaissance
        self.ville = ville
        self.prenom = prenom
        self.nom = nom
        self.telephone = telephone

    def obtenirAge(self):
        today = datetime.today()
        age = today.year - self.dateNaissance.year - ((today.month, today.day) < (self.dateNaissance.month, self.dateNaissance.day))
        return age

    def supprimer(self, id):
        # Code pour supprimer une personne de la base de données
        pass

    def lister(self):
        # Code pour lister les personnes
        pass
