import mysql.connector
from db import Database
from datetime import datetime

class Utilisateur:
    def __init__(self, id=None, pseudo=None, motDePasse=None, dateCreation=None):
        self.id = id
        self.pseudo = pseudo
        self.motDePasse = motDePasse
        self.dateCreation = dateCreation or datetime.now() # Définir par défaut la date et l'heure actuelles si elles ne sont pas fournies


    @staticmethod
    def authentification(pseudo, motDePasse):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="087907210769323928Ti@", 
                database="etab_db"
            )

            cursor = connection.cursor(dictionary=True)
            query = "SELECT * FROM utilisateur WHERE pseudo = %s AND motDePasse = %s"
            cursor.execute(query, (pseudo, motDePasse))
            result = cursor.fetchone()

            cursor.close()
            connection.close()

            return True if result else False

        except mysql.connector.Error as err:
            print(f"Erreur: {err}")
            return False

    
    def ajouter(self):
        try:
            db = Database()
            query = """INSERT INTO Utilisateur (pseudo, motDePasse, dateCreation) 
                    VALUES (%s, %s, %s)"""
            params = (self.pseudo, self.motDePasse, self.dateCreation)
        
            # Déboguer les paramètres
            print("Paramètres de la requête :")
            for param in params:
                print(f"- {param} ({type(param)})")
        
            # Exécutez la requête et récupérez l'identifiant généré automatiquement
            db.execute_query(query, params, fetch_lastrowid=True)
            self.id = db.get_lastrowid()  # Mettre à jour self.id avec l'identifiant généré automatiquement
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            db.close()

    @staticmethod
    def modiferMotDePasse(pseudo, motDePasse):
        db = Database()
        query = "UPDATE utilisateur SET motDePasse = %s WHERE pseudo = %s"
        db.execute_query(query, (motDePasse, pseudo))
        db.close()

    @staticmethod
    def supprimerCompte(pseudo):
        db = Database()
        query = "DELETE FROM utilisateur WHERE pseudo = %s"
        db.execute_query(query, (pseudo,))
        db.close()

    @staticmethod
    def listerUtilisateur():
        db = Database()
        query = "SELECT * FROM utilisateur"
        return db.fetch_query(query)
