import uuid
from db import Database
from personne import Personne
from education import Education

class Professeur:
    def __init__(self, id=None, date_naissance=None, ville=None, prenom=None, nom=None, telephone=None, vacant=None, matiere_enseigne=None, prochain_cours=None, sujet_prochaine_reunion=None):
        self.id = id or int(uuid.uuid4())  # Génère un UUID si aucun ID n'est fourni
        self.date_naissance = date_naissance
        self.ville = ville
        self.prenom = prenom
        self.nom = nom
        self.telephone = telephone
        self.vacant = vacant
        self.matiere_enseigne = matiere_enseigne
        self.prochain_cours = prochain_cours
        self.sujet_prochaine_reunion = sujet_prochaine_reunion

    def ajouter(self):
        try:
            db = Database()
            query = """INSERT INTO Professeur (dateNaissance, ville, prenom, nom, telephone, vacant, matiereEnseigne, prochainCours, sujetProchaineReunion) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            params = (self.date_naissance, self.ville, self.prenom, self.nom, self.telephone, self.vacant, self.matiere_enseigne, self.prochain_cours, self.sujet_prochaine_reunion)
            
            # Exécutez la requête et récupérez l'identifiant généré automatiquement
            self.id = db.execute_query(query, params, fetch_lastrowid=True)
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            db.close()
        
    def mettre_a_jour(self):
        try:
            db = Database()
            query = """UPDATE Professeur SET vacant = %s, matiereEnseigne = %s, prochainCours = %s, sujetProchaineReunion = %s, telephone = %s 
                    WHERE id = %s"""
            db.execute_query(query, (self.vacant, self.matiere_enseigne, self.prochain_cours, self.sujet_prochaine_reunion, self.telephone, self.id))
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            db.close()
        
    def supprimer(self):
        try:
            db = Database()
            query = "DELETE FROM Professeur WHERE id = %s"
            db.execute_query(query, (self.id,))
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            db.close()
        
    @staticmethod
    def obtenir_age(id):
        try:
            db = Database()
            query = "SELECT dateNaissance FROM Professeur WHERE id = %s"
            professeur_data = db.fetch_query(query, (id,))
            if professeur_data:
                # En supposant que vous ayez une fonction pour calculer l'âge à partir de date_naissance
                return calculate_age(professeur_data[0]['dateNaissance'])
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            db.close()

    @staticmethod
    def obtenir_professeurs():
        try:
            db = Database()
            query = "SELECT * FROM Professeur"
            return db.fetch_query(query)
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            db.close()
