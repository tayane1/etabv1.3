import uuid
from db import Database
from datetime import datetime

class Eleve:
    def __init__(self, id=None, date_naissance=None, ville=None, prenom=None, nom=None, telephone=None, classe=None, matricule=None):
        self.id = id or int(uuid.uuid4())  # Génère un UUID si aucun ID n'est fourni
        self.date_naissance = date_naissance
        self.ville = ville
        self.prenom = prenom
        self.nom = nom
        self.telephone = telephone
        self.classe = classe
        self.matricule = matricule

    def ajouter(self):
        try:
            db = Database()
            query = """INSERT INTO Eleve (dateNaissance, ville, prenom, nom, telephone, classe, matricule) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            params = (self.date_naissance, self.ville, self.prenom, self.nom, self.telephone, self.classe, self.matricule)
        
            # Déboguer les paramètres
            print("Paramètres de la requête :")
            for param in params:
                print(f"- {param} ({type(param)})")
        
            # Execute the query and retrieve the auto-generated id
            db.execute_query(query, params, fetch_lastrowid=True)
            self.id = db.get_lastrowid()  # Update self.id with the auto-generated id
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            db.close()

    def mettre_a_jour(self):
        try:
            db = Database()
            query = """UPDATE Eleve SET classe = %s, matricule = %s 
                    WHERE id = %s"""
            db.execute_query(query, (self.classe, self.matricule, self.id))
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            db.close()

    def supprimer(self):
        try:
            db = Database()
            query = "DELETE FROM Eleve WHERE id = %s"
            db.execute_query(query, (self.id,))
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            db.close()

    @staticmethod
    def obtenir_age(id):
        db = Database()
        query = "SELECT dateNaissance FROM Eleve WHERE id = %s"
        try:
            result = db.fetch_query(query, (id,))
            if result:
                date_naissance_str = result[0][0]  # En supposant que le résultat soit une liste de tuples
                date_naissance = datetime.strptime(date_naissance_str, "%Y-%m-%d")
                age = datetime.now().year - date_naissance.year
                if (datetime.now().month, datetime.now().day) < (date_naissance.month, date_naissance.day):
                    age -= 1  # Ajustez l'âge si l'anniversaire n'a pas encore eu lieu cette année
                return age
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            db.close()

    @staticmethod
    def obtenir_eleves():
        db = Database()
        query = "SELECT * FROM Eleve"
        try:
            return db.fetch_query(query)
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            db.close()
