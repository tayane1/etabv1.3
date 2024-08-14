from models import Utilisateur, Professeur, Eleve
from datetime import datetime
import time

def afficher_menu_principal():
    print("""
    ******************************************************
    BIENVENU DANS L’APPLICATION ETAB v1.3
    ******************************************************
    MENU:
    1: Gestion des élèves
    2: Gestion des professeurs
    3: Gestion des utilisateurs
    0: Quitter
    ******************************************************
    """)
    print(" Date système :", time.strftime("%H:%M"))

def afficher_menu_eleve():
    print("""
    ******************************************************
    GESTION DES ELEVES
    ******************************************************
    Menu :
    1: Ajouter un élève
    2: Supprimer un élève
    3: Modifier les informations de l'élève
    4: Lister les élèves
    5: Obtenir âge de l'élève
    6: Obtenir le dernier élève ajouté
    7: Retour
    0: Quitter
    ******************************************************
    """)

def afficher_menu_professeur():
    print("""
    ******************************************************
    GESTION DES PROFESSEURS
    ******************************************************
    Menu :
    1: Ajouter un professeur
    2: Supprimer un professeur
    3: Modifier les informations du professeur
    4: Lister les professeurs
    5: Obtenir âge du professeur
    6: Obtenir le dernier professeur ajouté
    7: Accueil
    ******************************************************
    """)

def afficher_menu_utilisateur():
    print("""
    ******************************************************
    GESTION DES UTILISATEURS
    ******************************************************
    Menu :
    1: Ajouter un utilisateur
    2: Supprimer un utilisateur
    3: Modifier le mot de passe d'un utilisateur
    4: Lister les utilisateurs
    0: Retour
    ******************************************************
    """)

def menu_principal():
    start_time = time.time()
    while True:
        afficher_menu_principal()
        choix = input("Choisissez une option : ")
        if choix == '1':
            menu_eleve()
        elif choix == '2':
            menu_professeur()
        elif choix == '3':
            menu_utilisateur()
        elif choix == '0':
            quitter_application(start_time)
            exit()
        else:
            print("Option invalide.")

def menu_eleve():
    while True:
        afficher_menu_eleve()
        choix = input("Choisissez une option : ")
        if choix == '1':
            ajouter_eleve()
        elif choix == '2':
            supprimer_eleve()
        elif choix == '3':
            modifier_eleve()
        elif choix == '4':
            lister_eleves()
        elif choix == '5':
            obtenir_age_eleve(Personne)
        elif choix == '6':
            obtenir_dernier_eleve()
        elif choix == '7':
            menu_principal()
        elif choix == '0':
            quitter_application(start_time)
            exit()
        else:
            print("Option invalide.")

def menu_professeur():
    while True:
        afficher_menu_professeur()
        choix = input("Choisissez une option : ")
        if choix == '1':
            ajouter_professeur()
        elif choix == '2':
            supprimer_professeur()
        elif choix == '3':
            modifier_professeur()
        elif choix == '4':
            lister_professeurs()
        elif choix == '5':
            obtenir_age_professeur(personne)
        elif choix == '6':
            obtenir_dernier_professeur()
        elif choix == '7':
            menu_principal()
        else:
            print("Option invalide.")

def menu_utilisateur():
    while True:
        afficher_menu_utilisateur()
        choix = input("Choisissez une option : ")
        if choix == '1':
            ajouter_utilisateur()
        elif choix == '2':
            supprimer_utilisateur()
        elif choix == '3':
            modifier_mot_de_passe()
        elif choix == '4':
            lister_utilisateurs()
        elif choix == '0':
            exit()
        else:
            print("Option invalide.")

def ajouter_professeur():
    try:
        id = int(input("ID : "))
        date_naissance = datetime.strptime(input("Date de naissance (YYYY-MM-DD) : "), "%Y-%m-%d")
        ville = input("Ville : ")
        prenom = input("Prénom : ")
        nom = input("Nom : ")
        telephone = input("Téléphone : ")
        vacant = input("Vacant (True/False) : ").strip().lower() == 'true'
        matiere_enseigne = input("Matière enseignée : ")
        prochain_cours = input("Prochain cours : ")
        sujet_prochaine_reunion = input("Sujet prochaine réunion : ")
        professeur = Professeur(id, date_naissance, ville, prenom, nom, telephone, vacant, matiere_enseigne, prochain_cours, sujet_prochaine_reunion)
        professeur.ajouter()
        print("Professeur ajouté avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'ajout du professeur : {e}")

def supprimer_professeur():
    try:
        id = int(input("ID du professeur à supprimer : "))
        professeur = Professeur.supprimerprofesseur(id=id, dateNaissance=None, ville=None, prenom=None, nom=None, telephone=None, vacant=None, matiereEnseigne=None, prochainCours=None, sujetProchaineReunion=None)
        professeur.supprimer(id)
        print("Professeur supprimé avec succès.")
    except Exception as e:
        print(f"Erreur lors de la suppression du professeur : {e}")

def modifier_professeur():
    try:
        id = int(input("ID du professeur à modifier : "))
        date_naissance = datetime.strptime(input("Nouvelle date de naissance (YYYY-MM-DD) : "), "%Y-%m-%d")
        ville = input("Nouvelle ville : ")
        prenom = input("Nouveau prénom : ")
        nom = input("Nouveau nom : ")
        telephone = input("Nouveau téléphone : ")
        vacant = input("Vacant (True/False) : ").strip().lower() == 'true'
        matiere_enseigne = input("Nouvelle matière enseignée : ")
        prochain_cours = input("Nouveau prochain cours : ")
        sujet_prochaine_reunion = input("Nouveau sujet prochaine réunion : ")
        professeur = Professeur(id, date_naissance, ville, prenom, nom, telephone, vacant, matiere_enseigne, prochain_cours, sujet_prochaine_reunion)
        professeur.mettreAJour()
        print("Professeur mis à jour avec succès.")
    except Exception as e:
        print(f"Erreur lors de la modification du professeur : {e}")

def lister_professeurs():
    try:
        professeurs = Professeur.obtenirProfesseur()
        for professeur in professeurs:
            print(professeur)
    except Exception as e:
        print(f"Erreur lors de la liste des professeurs : {e}")
        
        
def obtenir_age_professeur():
    try:
        id = int(input("ID du professeur : "))
        db = Database()
        query = "SELECT * FROM Personne p JOIN Professeur pr ON p.id = pr.id WHERE pr.id = %s"
        professeur_data = db.fetch_query(query, (id,))
        db.close()

        if professeur_data:
            professeur_data = professeur_data[0]
            date_naissance = datetime.strptime(professeur_data['dateNaissance'], "%Y-%m-%d")
            professeur = Professeur(
                id=professeur_data['id'],
                dateNaissance=date_naissance,
                ville=professeur_data['ville'],
                prenom=professeur_data['prenom'],
                nom=professeur_data['nom'],
                telephone=professeur_data['telephone'],
                vacant=professeur_data['vacant'],
                matiereEnseigne=professeur_data['matiereEnseigne'],
                prochainCours=professeur_data['prochainCours'],
                sujetProchaineReunion=professeur_data['sujetProchaineReunion']
            )
            age = professeur.obtenirAge()
            print(f"L'âge du professeur est : {age} ans.")
        else:
            print("Professeur non trouvé.")
    except Exception as e:
        print(f"Erreur lors de l'obtention de l'âge du professeur : {e}")


def obtenir_dernier_professeur():
    try:
        professeurs = Professeur.obtenirProfesseur()
        if professeurs:
            print("Dernier professeur ajouté :", professeurs[-1])
        else:
            print("Aucun professeur trouvé.")
    except Exception as e:
        print(f"Erreur lors de l'obtention du dernier professeur : {e}")

def ajouter_eleve():
    try:
        id = int(input("ID : "))
        date_naissance = datetime.strptime(input("Date de naissance (YYYY-MM-DD) : "), "%Y-%m-%d")
        ville = input("Ville : ")
        prenom = input("Prénom : ")
        nom = input("Nom : ")
        telephone = input("Téléphone : ")
        classe = input("Classe : ")
        matricule = input("Matricule : ")
        eleve = Eleve(id, date_naissance, ville, prenom, nom, telephone, classe, matricule)
        eleve.ajouter()
        print("Élève ajouté avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'ajout de l'élève : {e}")

def supprimer_eleve():
    try:
        id = int(input("ID de l'élève à supprimer : "))
        eleve = Eleve.supprimereleve(id=id, dateNaissance=None, ville=None, prenom=None, nom=None, telephone=None, classe=None, matricule=None)
        eleve.supprimer(id)
        print("Élève supprimé avec succès.")
    except Exception as e:
        print(f"Erreur lors de la suppression de l'élève : {e}")

def modifier_eleve():
    try:
        id = int(input("ID de l'élève à modifier : "))
        date_naissance = datetime.strptime(input("Nouvelle date de naissance (YYYY-MM-DD) : "), "%Y-%m-%d")
        ville = input("Nouvelle ville : ")
        prenom = input("Nouveau prénom : ")
        nom = input("Nouveau nom : ")
        telephone = input("Nouveau téléphone : ")
        classe = input("Nouvelle classe : ")
        matricule = input("Nouveau matricule : ")
        eleve = Eleve(id, date_naissance, ville, prenom, nom, telephone, classe, matricule)
        eleve.mettreAJour()
        print("Élève mis à jour avec succès.")
    except Exception as e:
        print(f"Erreur lors de la modification de l'élève : {e}")

def lister_eleves():
    try:
        eleves = Eleve.obtenirEleve()
        for eleve in eleves:
            print(eleve)
    except Exception as e:
        print(f"Erreur lors de la liste des élèves : {e}")
        

def obtenir_age_eleve():
    try:
        id = int(input("ID de l'élève : "))
        db = Database()
        query = "SELECT * FROM Eleve WHERE id = %s"
        eleve_data = db.fetch_query(query, (id,))
        db.close()

        if eleve_data:
            eleve_data = eleve_data[0]
            date_naissance = datetime.strptime(eleve_data['dateNaissance'], "%Y-%m-%d")
            eleve = Eleve(
                id=eleve_data['id'],
                dateNaissance=date_naissance,
                ville=eleve_data['ville'],
                prenom=eleve_data['prenom'],
                nom=eleve_data['nom'],
                telephone=eleve_data['telephone'],
                classe=eleve_data['classe'],
                matricule=eleve_data['matricule']
            )
            age = eleve.obtenirAge()
            print(f"L'âge de l'élève est : {age} ans.")
        else:
            print("Élève non trouvé.")
    except Exception as e:
        print(f"Erreur lors de l'obtention de l'âge de l'élève : {e}")


def obtenir_dernier_eleve():
    try:
        eleves = Eleve.obtenirEleve()
        if eleves:
            print("Dernier élève ajouté :", eleves[-1])
        else:
            print("Aucun élève trouvé.")
    except Exception as e:
        print(f"Erreur lors de l'obtention du dernier élève : {e}")

def ajouter_utilisateur():
    try:
        identifiant = input("Identifiant : ")
        mot_de_passe = input("Mot de passe : ")
        Utilisateur.ajouterCompte(identifiant, mot_de_passe)
        print("Utilisateur ajouté avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'ajout de l'utilisateur : {e}")

def supprimer_utilisateur():
    try:
        identifiant = input("Identifiant de l'utilisateur à supprimer : ")
        Utilisateur.supprimerCompte(identifiant)
        print("Utilisateur supprimé avec succès.")
    except Exception as e:
        print(f"Erreur lors de la suppression de l'utilisateur : {e}")

def modifier_mot_de_passe():
    try:
        identifiant = input("Identifiant : ")
        nouveau_mot_de_passe = input("Nouveau mot de passe : ")
        Utilisateur.modiferMotDePasse(identifiant, nouveau_mot_de_passe)
        print("Mot de passe modifié avec succès.")
    except Exception as e:
        print(f"Erreur lors de la modification du mot de passe : {e}")

def lister_utilisateurs():
    try:
        utilisateurs = Utilisateur.listerUtilisateur()
        for utilisateur in utilisateurs:
            print(utilisateur)
    except Exception as e:
        print(f"Erreur lors de la liste des utilisateurs : {e}")
        
def quitter_application(start_time):
    try:
        end_time = time.time()
        duree_session = int((end_time - start_time) / 60)
        print("Au revoir !")
        print(f"Durée de la session : {duree_session} minutes")
    except Exception as e:
        print(f"Erreur inattendue: {e}")

if __name__ == "__main__":
    identifiant = input("Identifiant : ")
    mot_de_passe = input("Mot de passe : ")
    admin = Utilisateur(id=1, identifiant='admin', motDePasse='admin')
    if admin.authentification(identifiant, mot_de_passe):
        menu_principal()
    else:
        print("Identifiant ou mot de passe incorrect")
