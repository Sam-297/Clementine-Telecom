from utils import db
from utils.interface import *
from utils.requetes import *
import time

def menus(etat = "Menu",choix = "",conn_db = None):
    """Handles the menu navigation"""
    is_wrong = False
    while True:
        if conn_db == None:
            print("\033[91mImpossible d'ouvrir le fichier de base de données.\033[0m")
            time.sleep(1)
            exit(1)
        match etat:
            case "Menu": # Menu
                clear_terminal()
                print_title("Menu")
                print_body(1,"Effectuer une requête")
                print_body(2,"Insérer une donnée")
                print_body(3,"Supprimer une donnée")
                print_body(4,"Modifier une donnée")
                print_body(5,"Afficher une table")
                print_body("q", "Quitter le programme")
                print_end()
                if is_wrong:
                    is_wrong = False
                    print(f"\033[91m'{choix}' n'est pas une option.\033[0m")
                choix = input("Veuillez saisir votre choix: ")
                match choix:
                    case "":
                        pass
                    case '1':
                        etat = "Requetes"
                    case '2':
                        etat = "Insert"
                    case '3':
                        etat = "Supprimer"
                    case '4':
                        etat = "Modif"
                    case '5':
                        etat = "Afficher_table"
                    case 'q':
                        clear_terminal()
                        print("Merci et au revoir!")
                        time.sleep(0.5)
                        exit(0)
                    case _:
                        is_wrong = True                

            case "Requetes": #Menu -> Requetes
                clear_terminal()
                print_title("Effectuer une requête")
                print_body(1,"Dépenses Clients")
                print_body(2,"Empreintes Carbone Clients")
                print_body(3,"Techniciens qui ne reparent pas un type d'appareil")
                print_body(4,"Clients qui produisent une E.C. > moyenne")
                print_body("r","Retourner au menu précédent")
                print_body("q", "Quitter le programme")
                print_end()
                if is_wrong:
                    is_wrong = False
                    print(f"\033[91m'{choix}' n'est pas une option.\033[0m")
                choix = input("Veuillez saisir votre choix: ")
                match choix:
                    case "":
                        pass
                    case '1':
                        etat = "Depenses"
                    case '2':
                        etat = "EC"
                    case '3':
                        etat = "techniciens_type"
                    case '4':
                        etat = "ec_moyenne"
                    case 'r':
                        etat = "Menu"
                    case 'q':
                        clear_terminal()
                        print("Merci et au revoir!")
                        time.sleep(0.5)
                        exit(0)
                    case _:
                        is_wrong = True
            case "Depenses": #Menu -> Requetes -> Depenses
                clear_terminal()
                print_title("Dépenses Clients")
                print_body(1,"Forfait jusqu'à ce jour")
                print_body(2,"Appareils")
                print_body(3,"Réparations")
                print_body(4,"Total des dépenses")
                print_body("r","Retourner au menu précédent")
                print_body("q", "Quitter le programme")
                print_end()
                if is_wrong:
                    is_wrong = False
                    print(f"\033[91m'{choix}' n'est pas une option.\033[0m")
                choix = input("Veuillez saisir votre choix: ")
                match choix:
                    case "":
                        pass
                    case '1':
                        etat = "Depenses_Forfait"
                    case '2':
                        etat = "Depenses_App"
                    case '3':
                        etat = "Depenses_Rep"
                    case '4':
                        etat = "Depenses_Tout"
                    case 'r':
                        etat = "Requetes"
                    case 'q':
                        clear_terminal()
                        print("Merci et au revoir!")
                        time.sleep(0.5)
                        exit(0)
                    case _:
                        is_wrong = True 
            case "Depenses_Forfait":
                clear_terminal()
                print_title("Forfait jusqu'à ce jour")
                print_clients()
                if is_wrong:
                    is_wrong = False
                    print(f"\033[91m'{choix}' n'est pas une option.\033[0m")
                choix = input("Veuillez saisir votre choix: ")
                match choix:
                    case "":
                        pass
                    case '1':
                        clear_terminal()
                        prix_forfait_client(conn_db)
                        input("\nAppuyez sur n'importe quelle touche pour continuer: ")
                        etat = "Menu"
                        #fonction afficher tout depenses forfait
                    case '2':
                        nom = demande_nom()
                        prix_forfait_client(conn_db,nom_client=nom)
                        input("\nAppuyez sur n'importe quelle touche pour continuer: ")
                        etat = "Menu"
                        #fonction chercher nom depenses forfait
                    case '3':
                        prenom = demande_prenom()
                        prix_forfait_client(conn_db,prenom_client=prenom)
                        input("\nAppuyez sur n'importe quelle touche pour continuer: ")
                        etat = "Menu"
                        #fonction chercher prenom depenses forfait
                    case '4':
                        num=demande_numero()
                        prix_forfait_client(conn_db,num_tel_client=num)
                        input("\nAppuyez sur n'importe quelle touche pour continuer: ")
                        etat = "Menu"
                        #fonction chercher num telephone depenses forfait
                    case 'r':
                        etat = "Depenses"
                    case 'q':
                        clear_terminal()
                        print("Merci et au revoir!")
                        time.sleep(0.5)
                        exit(0)
                    case _:
                        is_wrong = True 

            case "Depenses_App":
                clear_terminal()
                print_title("Appareils")
                print_clients()
                if is_wrong:
                    is_wrong = False
                    print(f"\033[91m'{choix}' n'est pas une option.\033[0m")
                choix = input("Veuillez saisir votre choix: ")
                match choix:
                    case "":
                        pass
                    case '1':
                        clear_terminal()
                        prix_appareils_client(conn_db)
                        input("\nAppuyez sur n'importe quelle touche pour continuer: ")
                        etat = "Menu"
                        #fonction afficher tout depenses appareil
                    case '2':
                        nom = demande_nom()
                        prix_appareils_client(conn_db,nom_client=nom)
                        input("\nAppuyez sur n'importe quelle touche pour continuer: ")
                        etat = "Menu"
                        #fonction chercher nom depenses appareil
                    case '3':
                        prenom = demande_prenom()
                        prix_appareils_client(conn_db,prenom_client=prenom)
                        input("\nAppuyez sur n'importe quelle touche pour continuer: ")
                        etat = "Menu"
                        #fonction chercher prenom depenses appareil
                    case '4':
                        num = demande_numero()
                        prix_appareils_client(conn_db,num_tel_client=num)
                        input("\nAppuyez sur n'importe quelle touche pour continuer: ")
                        etat = "Menu"
                        #fonction chercher num telephone depenses appareil
                    case 'r':
                        etat = "Depenses"
                    case 'q':
                        clear_terminal()
                        print("Merci et au revoir!")
                        time.sleep(0.5)
                        exit(0)
                    case _:
                        is_wrong = True 

            case "Depenses_Rep":
                clear_terminal()
                print_title("Réparations")
                print_clients()
                if is_wrong:
                    is_wrong = False
                    print(f"\033[91m'{choix}' n'est pas une option.\033[0m")
                choix = input("Veuillez saisir votre choix: ")
                match choix:
                    case "":
                        pass
                    case '1':
                        clear_terminal()
                        prix_reparations_client(conn_db)
                        input("\nAppuyez sur n'importe quelle touche pour continuer: ")
                        etat = "Menu"
                        #fonction afficher tout depenses reparation
                    case '2':
                        nom = demande_nom()
                        prix_reparations_client(conn_db,nom_client=nom)
                        input("\nAppuyez sur n'importe quelle touche pour continuer: ")
                        etat = "Menu"
                        #fonction chercher nom depenses reparation
                    case '3':
                        prenom = demande_prenom()
                        prix_reparations_client(conn_db,prenom_client=prenom)
                        input("\nAppuyez sur n'importe quelle touche pour continuer: ")
                        etat = "Menu"
                        #fonction chercher prenom depenses reparation
                    case '4':
                        num = demande_numero()
                        prix_reparations_client(conn_db,num_tel_client=num)
                        input("\nAppuyez sur n'importe quelle touche pour continuer: ")
                        etat = "Menu"
                        #fonction chercher num telephone depenses reparation
                    case 'r':
                        etat = "Depenses"
                    case 'q':
                        clear_terminal()
                        print("Merci et au revoir!")
                        time.sleep(0.5)
                        exit(0)
                    case _:
                        is_wrong = True 

            case "Depenses_Tout":
                clear_terminal()
                print_title("Total des dépenses")
                print_clients()
                if is_wrong:
                    is_wrong = False
                    print(f"\033[91m'{choix}' n'est pas une option.\033[0m")
                choix = input("Veuillez saisir votre choix: ")
                match choix:
                    case "":
                        pass
                    case '1':
                        clear_terminal()
                        prix_total_client(conn_db)
                        input("\nAppuyez sur n'importe quelle touche pour continuer: ")
                        etat = "Menu"
                        #fonction afficher tout depenses Total des dépenses
                    case '2':
                        nom = demande_nom()
                        prix_total_client(conn_db,nom_client=nom)
                        input("\nAppuyez sur n'importe quelle touche pour continuer: ")
                        etat = "Menu"
                        #fonction chercher nom depenses Total des dépenses
                    case '3':
                        prenom = demande_prenom()
                        prix_total_client(conn_db,prenom_client=prenom)
                        input("\nAppuyez sur n'importe quelle touche pour continuer: ")
                        etat = "Menu"
                        #fonction chercher prenom depenses Total des dépenses
                    case '4':
                        num = demande_numero()
                        prix_total_client(conn_db,num_tel_client=num)
                        input("\nAppuyez sur n'importe quelle touche pour continuer: ")
                        etat = "Menu"
                        #fonction chercher num telephone depenses Total des dépenses
                    case 'r':
                        etat = "Depenses"
                    case 'q':
                        clear_terminal()
                        print("Merci et au revoir!")
                        time.sleep(0.5)
                        exit(0)
                    case _:
                        is_wrong = True 

            case "EC":
                clear_terminal()
                print_title("Empreintes Carbone Clients")
                print_body(1,"Forfait jusqu'à ce jour")
                print_body(2,"Appareils")
                print_body(3,"Réparations")
                print_body(4,"Total des empreintes carbone")
                print_body("r","Retourner au menu précédent")
                print_body("q", "Quitter le programme")
                print_end()
                if is_wrong:
                    is_wrong = False
                    print(f"\033[91m'{choix}' n'est pas une option.\033[0m")
                choix = input("Veuillez saisir votre choix: ")
                match choix:
                    case "":
                        pass
                    case '1':
                        etat = "EC_Forfait"
                    case '2':
                        etat = "EC_App"
                    case '3':
                        etat = "EC_Rep"
                    case '4':
                        etat = "EC_Tout"
                    case 'r':
                        etat = "Requetes"
                    case 'q':
                        clear_terminal()
                        print("Merci et au revoir!")
                        time.sleep(0.5)
                        exit(0)
                    case _:
                        is_wrong = True 
            case "EC_Forfait":
                clear_terminal()
                print_title("Forfait jusqu'à ce jour")
                print_clients()
                if is_wrong:
                    is_wrong = False
                    print(f"\033[91m'{choix}' n'est pas une option.\033[0m")
                choix = input("Veuillez saisir votre choix: ")
                match choix:
                    case "":
                        pass
                    case '1':
                        clear_terminal()
                        emp_forfaits_clients(conn_db)
                        input("\nAppuyez sur n'importe quelle touche pour continuer: ")
                        etat = "Menu"
                        #fonction afficher tout e.c. forfait
                    case '2':
                        nom = demande_nom()
                        emp_forfaits_clients(conn_db,nom_client=nom)
                        input("\nAppuyez sur n'importe quelle touche pour continuer: ")
                        etat = "Menu"
                        #fonction chercher nom e.c. forfait
                    case '3':
                        prenom = demande_prenom()
                        emp_forfaits_clients(conn_db,prenom_client=prenom)
                        input("\nAppuyez sur n'importe quelle touche pour continuer: ")
                        etat = "Menu"
                        #fonction chercher prenom e.c. forfait
                    case '4':
                        num = demande_numero()
                        emp_forfaits_clients(conn_db,num_tel_client=num)
                        input("\nAppuyez sur n'importe quelle touche pour continuer: ")
                        etat = "Menu"
                        #fonction chercher num e.c. forfait
                    case 'r':
                        etat = "EC"
                    case 'q':
                        clear_terminal()
                        print("Merci et au revoir!")
                        time.sleep(0.5)
                        exit(0)
                    case _:
                        is_wrong = True 
            case "EC_App":
                clear_terminal()
                print_title("Appareils")
                print_clients()
                if is_wrong:
                    is_wrong = False
                    print(f"\033[91m'{choix}' n'est pas une option.\033[0m")
                choix = input("Veuillez saisir votre choix: ")
                match choix:
                    case "":
                        pass
                    case '1':
                        clear_terminal()
                        emp_appareils_clients(conn_db)
                        input("\nAppuyez sur n'importe quelle touche pour continuer: ")
                        etat = "Menu"
                        #fonction afficher tout e.c. appareils
                    case '2':
                        nom = demande_nom()
                        emp_appareils_clients(conn_db,nom_client=nom)
                        input("\nAppuyez sur n'importe quelle touche pour continuer: ")
                        etat = "Menu"
                        #fonction chercher nom e.c. appareils
                    case '3':
                        prenom = demande_prenom()
                        emp_appareils_clients(conn_db,prenom_client=prenom)
                        input("\nAppuyez sur n'importe quelle touche pour continuer: ")
                        etat = "Menu"
                        #fonction chercher prenom e.c. appareils
                    case '4':
                        num = demande_numero()
                        emp_appareils_clients(conn_db,num_tel_client=num)
                        input("\nAppuyez sur n'importe quelle touche pour continuer: ")
                        etat = "Menu"
                        #fonction chercher num e.c. appareils
                    case 'r':
                        etat = "EC"
                    case 'q':
                        clear_terminal()
                        print("Merci et au revoir!")
                        time.sleep(0.5)
                        exit(0)
                    case _:
                        is_wrong = True 
            case "EC_Rep":
                clear_terminal()
                print_title("Réparations")
                print_clients()
                if is_wrong:
                    is_wrong = False
                    print(f"\033[91m'{choix}' n'est pas une option.\033[0m")
                choix = input("Veuillez saisir votre choix: ")
                match choix:
                    case "":
                        pass
                    case '1':
                        clear_terminal()
                        emp_reparations_clients(conn_db)
                        input("\nAppuyez sur n'importe quelle touche pour continuer: ")
                        etat = "Menu"
                        #fonction afficher tout e.c. Réparations
                    case '2':
                        nom = demande_nom()
                        emp_reparations_clients(conn_db,nom_client=nom)
                        input("\nAppuyez sur n'importe quelle touche pour continuer: ")
                        etat = "Menu"
                        #fonction chercher nom e.c. Réparations
                    case '3':
                        prenom = demande_prenom()
                        emp_reparations_clients(conn_db,prenom_client=prenom)
                        input("\nAppuyez sur n'importe quelle touche pour continuer: ")
                        etat = "Menu"
                        #fonction chercher prenom e.c. Réparations
                    case '4':
                        num = demande_numero()
                        emp_reparations_clients(conn_db,num_tel_client=num)
                        input("\nAppuyez sur n'importe quelle touche pour continuer: ")
                        etat = "Menu"
                        #fonction chercher num e.c. Réparations
                    case 'r':
                        etat = "EC"
                    case 'q':
                        clear_terminal()
                        print("Merci et au revoir!")
                        time.sleep(0.5)
                        exit(0)
                    case _:
                        is_wrong = True 
            case "EC_Tout":
                clear_terminal()
                print_title("Total des empreintes carbone")
                print_clients()
                if is_wrong:
                    is_wrong = False
                    print(f"\033[91m'{choix}' n'est pas une option.\033[0m")
                choix = input("Veuillez saisir votre choix: ")
                match choix:
                    case "":
                        pass
                    case '1':
                        clear_terminal()
                        emp_totale_client(conn_db)
                        input("\nAppuyez sur n'importe quelle touche pour continuer: ")
                        etat = "Menu"
                        #fonction afficher tout e.c. Total des empreintes carbone
                    case '2':
                        nom = demande_nom()
                        emp_totale_client(conn_db,nom_client=nom)
                        input("\nAppuyez sur n'importe quelle touche pour continuer: ")
                        etat = "Menu"
                        #fonction chercher nom e.c. Total des empreintes carbone
                    case '3':
                        prenom = demande_prenom()
                        emp_totale_client(conn_db,prenom_client=prenom)
                        input("\nAppuyez sur n'importe quelle touche pour continuer: ")
                        etat = "Menu"
                        #fonction chercher prenom e.c. Total des empreintes carbone 
                    case '4':
                        num = demande_numero()
                        emp_totale_client(conn_db,num_tel_client=num)
                        input("\nAppuyez sur n'importe quelle touche pour continuer: ")
                        etat = "Menu"
                        #fonction chercher num e.c. Total des empreintes carbone
                    case 'r':
                        etat = "EC"
                    case 'q':
                        clear_terminal()
                        print("Merci et au revoir!")
                        time.sleep(0.5)
                        exit(0)
                    case _:
                        is_wrong = True 

            case "techniciens_type":
                clear_terminal()
                typee = input("Veuillez saisir le type d'appareil: ")
                techniciens_non_reparent_x(conn_db,typee)
                input("\nAppuyez sur n'importe quelle touche pour continuer: ")
                etat = "Menu"
                # techniciens qui ne reparent pas le type d'appareil x
            case "ec_moyenne":
                clear_terminal()
                client_plus_produisant(conn_db)
                input("\nAppuyez sur n'importe quelle touche pour continuer: ")
                etat = "Menu"
                #conso emp > moyenne(tout conso emp)

            case "Insert":
                clear_terminal()
                print_title("Insérer une donnée")
                print_body(1,"Ajouter un client")
                print_body(2,"Ajouter un appareil")
                print_body("r","Retourner au menu précédent")
                print_body("q", "Quitter le programme")
                print_end() 
                if is_wrong:
                    is_wrong = False
                    print(f"\033[91m'{choix}' n'est pas une option.\033[0m")
                choix = input("Veuillez saisir votre choix: ")
                match choix:
                    case "":
                        pass
                    case '1':
                        etat = "aj_client"
                    case '2':
                        etat = "aj_app"
                    case 'r':
                        etat = "Menu"
                    case 'q':
                        clear_terminal()
                        print("Merci et au revoir!")
                        time.sleep(0.5)
                        exit(0)
                    case _:
                        is_wrong = True

            case "aj_client": #Menu -> Insert -> aj_client
                clear_terminal()
                while True:
                    try:
                        num = int(input("Numéro de téléphone du client: "))
                        break
                    except ValueError:
                        print("\033[91mNuméro non valide!\033[0m")
                nom = input("Nom du client: ")
                prenom = input("Prénom du client: ")
                addr = input("Adresse du client: ")
                while True:
                    try:
                        num_forfait = int(input("Numéro de forfait du client: "))
                        break
                    except ValueError:
                        print("\033[91mNuméro de forfait non valide!\033[0m")
                is_added = ajouter_client(conn_db,num_tel_client = num,nom_client=nom,prenom_client=prenom,addresse_client=addr,num_forfait=num_forfait) #function de jad
                if is_added:
                    print("\033[92mClient ajouté à la base de donnée\033[0m")
                input("\nAppuyez sur n'importe quelle touche pour continuer: ")
                etat = "Menu"
                clear_terminal()

            case "aj_app": #Menu -> Insert -> aj_app
                clear_terminal()
                while True:
                    try:
                        num = int(input("Numéro de l'appareil du client: "))
                        break
                    except ValueError:
                        print("\033[91mNuméro non valide!\033[0m")
                modele = input("Modèle appareil: ")
                while True:
                    try:
                        est_neuf = int(input("Appareil neuf (1), ou reconditionné(0): "))
                        break
                    except ValueError:
                        print("\033[91mNuméro de forfait non valide!\033[0m")
                while est_neuf != 1 and est_neuf !=0:
                    while True:
                        try:
                            est_neuf = int(input("\033[91mMettre 0 ou 1! \033[0mAppareil neuf (1), ou reconditionné(0): "))
                            break
                        except ValueError:
                            print("\033[91mNuméro de forfait non valide!\033[0m")
                typa = input("Type appareil (Montre Connectée, Tablette, Téléphone, TV): ")
                while typa != "Montre Connectée" and typa != "Tablette" and typa != "Téléphone" and typa != "TV":
                    typa = input("\033[91mChoisir un des choix possible! \033[0mType appareil (Montre Connectée, Tablette, Téléphone, TV): ")
                while True:
                    try:
                        prix = float(input("Prix: "))
                        break
                    except ValueError:
                        print("\033[91mPrix non valide!\033[0m")
                while True:
                    try:
                        ec = float(input("Empreinte Carbone: "))
                        break
                    except ValueError:
                        print("\033[91mE.C. non valide!\033[0m")
                while True:
                    try:
                        numtel = int(input("Numéro de téléphone du client: "))
                        break
                    except ValueError:
                        print("\033[91mNuméro non valide!\033[0m")
                is_added = ajouter_appareil(conn_db,num_apareil=num,modele_appareil=modele,est_neuf_appareil=est_neuf,type_appareil=typa,prix_appareil=prix,emp_carbone_appareil=ec,num_tel_client=numtel) #function de jad
                if is_added:
                    print("\033[92mAppareil ajouté à la base de donnée\033[0m")
                input("\nAppuyez sur n'importe quelle touche pour continuer: ")
                etat = "Menu"
                clear_terminal()
            
            case "Supprimer":
                clear_terminal()
                print_title("Supprimer une donnée")
                print_body(1,"Supprimer un client et ses appareils")
                print_body(2,"Supprimer un appareil et ses réparations")
                print_body("r","Retourner au menu précédent")
                print_body("q", "Quitter le programme")
                print_end()
                if is_wrong:
                    is_wrong = False
                    print(f"\033[91m'{choix}' n'est pas une option.\033[0m")
                choix = input("Veuillez saisir votre choix: ")
                match choix:
                    case "":
                        pass
                    case '1':
                        clear_terminal()
                        while True:
                            try:
                                numtel = int(input("Numéro de téléphone du client: "))
                                break
                            except ValueError:
                                print("\033[91mNuméro non valide!\033[0m")
                        supprimer_client(conn_db,numtel)
                        print("\033[92mClient supprimé de la base de donnée\033[0m")
                        input("Appuyez sur n'importe quelle touche pour continuer: ")
                        etat = "Menu"
                    case '2':
                        clear_terminal()
                        while True:
                            try:
                                numtel = int(input("Numéro de l'appareil: "))
                                break
                            except ValueError:
                                print("\033[91mNuméro non valide!\033[0m")
                        supprimer_appareil(conn_db,numtel)
                        print("\033[92mAppareil supprimé de la base de donnée\033[0m")
                        input("Appuyez sur n'importe quelle touche pour continuer: ")
                        etat = "Menu"
                    case 'r':
                        etat = "Menu"
                    case 'q':
                        clear_terminal()
                        print("Merci et au revoir!")
                        time.sleep(0.5)
                        exit(0)
                    case _:
                        is_wrong = True
                
            case "Modif":
                clear_terminal()
                print_title("Modifier une donnée")
                print_body(1,"Modifier la limite de consomation d'un forfait")
                print_body("r","Retourner au menu précédent")
                print_body("q", "Quitter le programme")
                print_end()
                if is_wrong:
                    is_wrong = False
                    print(f"\033[91m'{choix}' n'est pas une option.\033[0m")
                choix = input("Veuillez saisir votre choix: ")
                match choix:
                    case "":
                        pass
                    case '1':
                        clear_terminal()
                        while True:
                            try:
                                numforf = int(input("Numéro du forfait: "))
                                break
                            except ValueError:
                                print("\033[91mNuméro non valide!\033[0m")
                        while True:
                            try:
                                lim = int(input("Limite de consomation en GB: "))
                                break
                            except ValueError:
                                print("\033[91mLimite non valide!\033[0m")
                        is_added = modifier_limite_forfait(conn_db,numforf,lim)
                        if is_added:
                            print("\033[92mLmite de consomation modifié dans la base de donnée\033[0m")
                        input("Appuyez sur n'importe quelle touche pour continuer: ")
                        etat = "Menu"
                    case 'r':
                        etat = "Menu"
                    case 'q':
                        clear_terminal()
                        print("Merci et au revoir!")
                        time.sleep(0.5)
                        exit(0)
                    case _:
                        is_wrong = True



            case "Afficher_table":
                clear_terminal()
                print_title("Afficher une table")
                print_body(1,"Clients")
                print_body(2,"Forfaits")
                print_body(3,"Appareils")
                print_body(4,"Techniciens")
                print_body(5,"Interventions")
                print_body(6,"Réparations")
                print_body("r","Retourner au menu précédent")
                print_body("q", "Quitter le programme")
                print_end()
                if is_wrong:
                    is_wrong = False
                    print(f"\033[91m'{choix}' n'est pas une option.\033[0m")
                choix = input("Veuillez saisir votre choix: ")
                match choix:
                    case "":
                        pass
                    case '1':
                        clear_terminal()
                        afficher_table(conn_db, 1)
                        input("\nAppuyez sur n'importe quelle touche pour continuer: ")
                        etat = "Menu"
                    case '2':
                        clear_terminal()
                        afficher_table(conn_db, 2)
                        input("\nAppuyez sur n'importe quelle touche pour continuer: ")
                        etat = "Menu"
                    case '3':
                        clear_terminal()
                        afficher_table(conn_db, 3)
                        print("\033[91m\nBug affichage des caractères français! On peut pas fixer ça.\033[0m")
                        input("Appuyez sur n'importe quelle touche pour continuer: ")
                        etat = "Menu"
                    case '4':
                        clear_terminal()
                        afficher_table(conn_db, 4)
                        input("\nAppuyez sur n'importe quelle touche pour continuer: ")
                        etat = "Menu"
                    case '5':
                        clear_terminal()
                        afficher_table(conn_db, 5)
                        input("\nAppuyez sur n'importe quelle touche pour continuer: ")
                        etat = "Menu"
                    case '6':
                        clear_terminal()
                        afficher_table(conn_db, 6)
                        input("\nAppuyez sur n'importe quelle touche pour continuer: ")
                        etat = "Menu"
                    case 'r':
                        etat = "Menu"
                    case 'q':
                        clear_terminal()
                        print("Merci et au revoir!")
                        time.sleep(0.5)
                        exit(0)
                    case _:
                        is_wrong = True



            case _:
                print(f"{etat} is not an etat ?!?!?")   
                exit(1)   

def main():
    """Establishes a connection with the database and starts the menu navigation"""
    clear_terminal()
    db_file = "data/clementine_tables.db"

    conn = db.creer_connexion(db_file)
    conn.set_trace_callback(None)
    print("Made with ♥ by Jad & Sam")
    time.sleep(0.2)
    if conn == None:
        print("\033[91mImpossible d'ouvrir le fichier de base de données.\033[0m")
        time.sleep(1)
        exit(1)
    db.mise_a_jour_bd(conn, "data/creation_tables.sql")
    db.mise_a_jour_bd(conn, "data/data_inserts.sql")
    print("\033[1;32mBase de données initialisée\033[0m")
    time.sleep(0.5)
    clear_terminal()

    menus(conn_db=conn)


if __name__ == "__main__":
    clear_terminal()
    main()