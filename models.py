from db import Database
from datetime import datetime

class Utilisateur:
    def __init__(self, id, identifiant, motDePasse):
        self.id = id
        self.identifiant = identifiant
        self.motDePasse = motDePasse

    def authentification(self, identifiant, motDePasse):
        return self.identifiant == identifiant and self.motDePasse == motDePasse

    @staticmethod
    def ajouterCompte(identifiant, motDePasse):
        db = Database()
        query = "INSERT INTO utilisateur (identifiant, motDePasse) VALUES (%s, %s)"
        db.execute_query(query, (identifiant, motDePasse))
        db.close()

    @staticmethod
    def modiferMotDePasse(identifiant, motDePasse):
        db = Database()
        query = "UPDATE utilisateur SET motDePasse = %s WHERE identifiant = %s"
        db.execute_query(query, (motDePasse, identifiant))
        db.close()

    @staticmethod
    def supprimerCompte(identifiant):
        db = Database()
        query = "DELETE FROM utilisateur WHERE identifiant = %s"
        db.execute_query(query, (identifiant,))
        db.close()

    @staticmethod
    def listerUtilisateur():
        db = Database()
        query = "SELECT * FROM utilisateur"
        return db.fetch_query(query)

class Personne:
    def __init__(self, id, dateNaissance, ville, prenom, nom, telephone):
        self.id = id
        self.dateNaissance = dateNaissance
        self.ville = ville
        self.prenom = prenom
        self.nom = nom
        self.telephone = telephone

    def supprimer(self, id):
        db = Database()
        query = "DELETE FROM Personne WHERE id = %s"
        db.execute_query(query, (id,))
        db.close()

    def lister(self):
        db = Database()
        query = "SELECT * FROM Personne"
        return db.fetch_query(query)

    def obtenirAge(self):
        today = datetime.now()
        age = today.year - self.dateNaissance.year - ((today.month, today.day) < (self.dateNaissance.month, self.dateNaissance.day))
        return age

class Professeur(Personne):
    def __init__(self, id, dateNaissance, ville, prenom, nom, telephone, vacant, matiereEnseigne, prochainCours, sujetProchaineReunion):
        super().__init__(id, dateNaissance, ville, prenom, nom, telephone)
        self.vacant = vacant
        self.matiereEnseigne = matiereEnseigne
        self.prochainCours = prochainCours
        self.sujetProchaineReunion = sujetProchaineReunion

    def ajouter(self):
        db = Database()
        query = """INSERT INTO Professeur (id, dateNaissance, ville, prenom, nom, telephone, vacant, matiereEnseigne, prochainCours, sujetProchaineReunion) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        db.execute_query(query, (self.id, self.dateNaissance, self.ville, self.prenom, self.nom, self.telephone, self.vacant, self.matiereEnseigne, self.prochainCours, self.sujetProchaineReunion))
        db.close()

    def mettreAJour(self):
        db = Database()
        query = """UPDATE Professeur SET vacant = %s, matiereEnseigne = %s, prochainCours = %s, sujetProchaineReunion = %s 
                WHERE id = %s"""
        db.execute_query(query, (self.vacant, self.matiereEnseigne, self.prochainCours, self.sujetProchaineReunion, self.id))
        db.close()
        
    def supprimerprofesseur(self):
        db = Database()
        query = "DELETE FROM Professeur WHERE id = %s"
        db.execute_query(query, (id,))
        db.close()

    @staticmethod
    def obtenirProfesseur():
        db = Database()
        query = "SELECT * FROM Professeur"
        return db.fetch_query(query)

class Eleve(Personne):
    def __init__(self, id, dateNaissance, ville, prenom, nom, telephone, classe, matricule):
        super().__init__(id, dateNaissance, ville, prenom, nom, telephone)
        self.classe = classe
        self.matricule = matricule

    def ajouter(self):
        db = Database()
        query = """INSERT INTO Eleve (id, dateNaissance, ville, prenom, nom, telephone, classe, matricule) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        db.execute_query(query, (self.id, self.dateNaissance, self.ville, self.prenom, self.nom, self.telephone, self.classe, self.matricule))
        db.close()

    def mettreAJour(self):
        db = Database()
        query = """UPDATE Eleve SET classe = %s, matricule = %s 
                WHERE id = %s"""
        db.execute_query(query, (self.classe, self.matricule, self.id))
        db.close()
        
    def supprimereleve(self):
        db = Database()
        query = "DELETE FROM Eleve WHERE id = %s"
        db.execute_query(query, (id,))
        db.close()

    @staticmethod
    def obtenirEleve():
        db = Database()
        query = "SELECT * FROM Eleve"
        return db.fetch_query(query)

class Education:
    def enseigner(self, matiere):
        return f"Enseigne la matière {matiere}"

    def preparerCours(self, cours):
        return f"Prépare le contenu d'un cours sur le sujet {cours}"

    def assisterReunion(self, sujet):
        return f"Doit assister à une reunion sur {sujet}"
