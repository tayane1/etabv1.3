from models import Utilisateur
from eleve import Eleve
from professeur import Professeur
import time
from datetime import datetime
import uuid

class Main:
    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
    def menu_principal():
        start_time = time.time()
        while True:
            Main.afficher_menu_principal()
            choix = input("Choisissez une option : ")
            if choix == '1':
                Main.menu_eleve()
            elif choix == '2':
                Main.menu_professeur()
            elif choix == '3':
                Main.menu_utilisateur()
            elif choix == '0':
                Main.quitter_application(start_time)
                exit()
            else:
                print("Option invalide.")

    @staticmethod
    def menu_eleve():
        while True:
            Main.afficher_menu_eleve()
            choix = input("Choisissez une option : ")
            if choix == '1':
                Main.ajouter_eleve()
            elif choix == '2':
                Main.supprimer_eleve()
            elif choix == '3':
                Main.modifier_eleve()
            elif choix == '4':
                Main.lister_eleves()
            elif choix == '5':
                Main.obtenir_age_eleve()
            elif choix == '6':
                Main.obtenir_dernier_eleve()
            elif choix == '7':
                Main.menu_principal()
            elif choix == '0':
                exit()
            else:
                print("Option invalide.")

    @staticmethod
    def menu_professeur():
        while True:
            Main.afficher_menu_professeur()
            choix = input("Choisissez une option : ")
            if choix == '1':
                Main.ajouter_professeur()
            elif choix == '2':
                Main.supprimer_professeur()
            elif choix == '3':
                Main.modifier_professeur()
            elif choix == '4':
                Main.lister_professeurs()
            elif choix == '5':
                Main.obtenir_age_professeur()
            elif choix == '6':
                Main.obtenir_dernier_professeur()
            elif choix == '7':
                Main.menu_principal()
            else:
                print("Option invalide.")

    @staticmethod
    def menu_utilisateur():
        while True:
            Main.afficher_menu_utilisateur()
            choix = input("Choisissez une option : ")
            if choix == '1':
                Main.ajouter_utilisateur()
            elif choix == '2':
                Main.supprimer_utilisateur()
            elif choix == '3':
                Main.modifier_mot_de_passe()
            elif choix == '4':
                Main.lister_utilisateurs()
            elif choix == '0':
                exit()
            else:
                print("Option invalide.")

# Début gestion des professeurs
    @staticmethod
    def ajouter_professeur():
        try:
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
        except ValueError as ve:
            print(f"Erreur de valeur : {ve}")
        except Exception as e:
            print(f"Erreur lors de l'ajout du professeur : {e}")

    @staticmethod
    def supprimer_professeur():
        try:
            id = int(input("ID du professeur à supprimer : "))
            professeur = Professeur(id=id)
            professeur.supprimer(id)
            print("Professeur supprimé avec succès.")
        except ValueError as ve:
            print(f"Erreur de valeur : {ve}")
        except Exception as e:
            print(f"Erreur lors de la suppression du professeur : {e}")

    @staticmethod
    def modifier_professeur():
        try:
            id = int(input("ID du professeur à modifier : "))
            telephone = input("Nouveau téléphone : ")
            vacant = input("Vacant (True/False) : ").strip().lower() == 'true'
            matiere_enseigne = input("Nouvelle matière enseignée : ")
            prochain_cours = input("Nouveau prochain cours : ")
            sujet_prochaine_reunion = input("Nouveau sujet prochaine réunion : ")
            professeur = Professeur(id, telephone=telephone, vacant=vacant, matiere_enseigne=matiere_enseigne, prochain_cours=prochain_cours, sujet_prochaine_reunion=sujet_prochaine_reunion)
            professeur.mettre_a_jour()
            print("Professeur mis à jour avec succès.")
        except ValueError as ve:
            print(f"Erreur de valeur : {ve}")
        except Exception as e:
            print(f"Erreur lors de la modification du professeur : {e}")

    @staticmethod
    def lister_professeurs():
        try:
            professeurs = Professeur.obtenir_professeurs()
            for professeur in professeurs:
                print(professeur)
        except Exception as e:
            print(f"Erreur lors de la liste des professeurs : {e}")

    @staticmethod
    def obtenir_age_professeur():
        try:
            id = int(input("ID du professeur : "))
            professeur_data = Professeur.obtenir_professeurs(id)
            if professeur_data:
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
                age = professeur.obtenir_age()
                print(f"L'âge du professeur est : {age} ans.")
            else:
                print("Professeur non trouvé.")
        except ValueError as ve:
            print(f"Erreur de valeur : {ve}")
        except Exception as e:
            print(f"Erreur lors de l'obtention de l'âge du professeur : {e}")

    @staticmethod
    def obtenir_dernier_professeur():
        try:
            professeurs = Professeur.obtenir_professeurs()
            if professeurs:
                print("Dernier professeur ajouté :", professeurs[-1])
            else:
                print("Aucun professeur trouvé.")
        except Exception as e:
            print(f"Erreur lors de l'obtention du dernier professeur : {e}")

# Fin gestion des professeurs

# Début gestion des élèves
    @staticmethod
    def ajouter_eleve():
        try:
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
        except ValueError as ve:
            print(f"Erreur de valeur : {ve}")
        except Exception as e:
            print(f"Erreur lors de l'ajout de l'élève : {e}")

    @staticmethod
    def supprimer_eleve():
        try:
            id = int(input("ID de l'élève à supprimer : "))
            eleve = Eleve(id=id)
            eleve.supprimer(id)
            print("Élève supprimé avec succès.")
        except ValueError as ve:
            print(f"Erreur de valeur : {ve}")
        except Exception as e:
            print(f"Erreur lors de la suppression de l'élève : {e}")

    @staticmethod
    def modifier_eleve():
        try:
            id = int(input("ID de l'élève à modifier : "))
            telephone = input("Nouveau téléphone : ")
            classe = input("Nouvelle classe : ")
            matricule = input("Nouveau matricule : ")
            eleve = Eleve(id, telephone=telephone, classe=classe, matricule=matricule)
            eleve.mettre_a_jour()
            print("Élève mis à jour avec succès.")
        except ValueError as ve:
            print(f"Erreur de valeur : {ve}")
        except Exception as e:
            print(f"Erreur lors de la modification de l'élève : {e}")

    @staticmethod
    def lister_eleves():
        try:
            eleves = Eleve.obtenir_eleves()
            for eleve in eleves:
                print(eleve)
        except Exception as e:
            print(f"An error occurred: {e}")


    @staticmethod
    def obtenir_age_eleve():
        try:
            id = int(input("ID de l'élève : "))
            eleve_data = Eleve.obtenir_eleves(id)
            if eleve_data:
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
                age = eleve.obtenir_age()
                print(f"L'âge de l'élève est : {age} ans.")
            else:
                print("Élève non trouvé.")
        except ValueError as ve:
            print(f"Erreur de valeur : {ve}")
        except Exception as e:
            print(f"Erreur lors de l'obtention de l'âge de l'élève : {e}")

    @staticmethod
    def obtenir_dernier_eleve():
        try:
            eleves = Eleve.obtenir_eleves()
            if eleves:
                print("Dernier élève ajouté :", eleves[-1])
            else:
                print("Aucun élève trouvé.")
        except Exception as e:
            print(f"Erreur lors de l'obtention du dernier élève : {e}")

# Fin gestion des élèves

# Début gestion des utilisateurs
    @staticmethod
    def ajouter_utilisateur():
        try:
            pseudo = input("Votre pseudo : ")
            motDePasse = input("Mot de passe : ")
            admin = Utilisateur(pseudo=pseudo, motDePasse=motDePasse, )
            admin.ajouter()
            print("Utilisateur ajouté avec succès.")
        except ValueError as ve:
            print(f"Erreur de valeur : {ve}")
        except Exception as e:
            print(f"Erreur lors de l'ajout de l'utilisateur : {e}")

    @staticmethod
    def supprimer_utilisateur():
        try:
            pseudo = input("Identifiant de l'utilisateur à supprimer : ")
            Utilisateur.supprimerCompte(pseudo)
            print("Utilisateur supprimé avec succès.")
        except ValueError as ve:
            print(f"Erreur de valeur : {ve}")
        except Exception as e:
            print(f"Erreur lors de la suppression de l'utilisateur : {e}")

    @staticmethod
    def modifier_mot_de_passe():
        try:
            pseudo = input("Votre pseudo : ")
            nouveau_mot_de_passe = input("Nouveau mot de passe : ")
            Utilisateur.modifierMotDePasse(pseudo, nouveau_mot_de_passe)
            print("Mot de passe modifié avec succès.")
        except ValueError as ve:
            print(f"Erreur de valeur : {ve}")
        except Exception as e:
            print(f"Erreur lors de la modification du mot de passe : {e}")

    @staticmethod
    def lister_utilisateurs():
        try:
            utilisateurs = Utilisateur.listerUtilisateur()
            for utilisateur in utilisateurs:
                print(utilisateur)
        except Exception as e:
            print(f"Erreur lors de la liste des utilisateurs : {e}")

# Fin gestion des utilisateurs

    @staticmethod
    def quitter_application(start_time):
        try:
            end_time = time.time()
            duree_session = int((end_time - start_time) / 60)
            print("Au revoir !")
            print(f"Durée de la session : {duree_session} minutes")
        except Exception as e:
            print(f"Erreur inattendue: {e}")

if __name__ == "__main__":
    pseudo = input("Pseudo : ")
    mot_de_passe = input("Mot de passe : ")
    admin = Utilisateur(id=1, pseudo=pseudo, motDePasse=mot_de_passe)  # Utilise pseudo au lieu d'identifiant
    if admin.authentification(pseudo, mot_de_passe):
        Main.menu_principal()
    else:
        print("Pseudo ou mot de passe incorrect")