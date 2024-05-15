from os import system, name

def clear_terminal():
    # For Windows
    if name == 'nt':
        _ = system('cls')
    # For Unix/Linux/MacOS
    else:
        _ = system('clear')

def print_title(txt, line = 54):
    line = int(line)
    length = len(txt)
    nb_dash = round((line - length - 2) / 2)
    #print(length + 2 + nb_dash * 2)
    if length + 2 + nb_dash * 2 > line:
        print("\033[1;38;2;255;121;0m-" * (nb_dash-1), end="")
    else:
        if length + 2 + nb_dash * 2 < line:
            print("\033[1;38;2;255;121;0m-",end='')
        print("\033[1;38;2;255;121;0m-" * nb_dash, end="")
    print("",txt,"",end="")
    print("\033[1;38;2;255;121;0m-" * nb_dash, end="")
    print("\033[0m")


def print_end(line = 54):
    line = int(line)
    print("\033[1;38;2;255;121;0m","-" * line,"\033[0m",sep='') 
    print

def print_body(c, txt):
    print("\033[1;33m",c,". \033[0m",txt,sep='')

def print_table(rows, desc):
    """ - rows:  une listes des tuples ex: [(1,2,3), (2,3,4),....]
        - desc: une liste qui contient des 7-tuples contenant des informations sur les attributs
    """
    # affichage de la premiere colonne qui contient les attributs   
    liste_longeur_attribut = []
    for t in desc:
        if t == desc[-1]:
            print(t[0])
            liste_longeur_attribut.append(len(t[0])+2)
        else:
            print(t[0], " | ", sep = "", end = "")
            liste_longeur_attribut.append(len(t[0])+2)
            if t == desc[0]:
                liste_longeur_attribut[-1] -= 1

    n_tirets = sum(liste_longeur_attribut) + len(desc) - 1
    print("-" * n_tirets)

    for row in rows:
        for i in range(len(row)):
            element = row[i]
            if type(element) == float:
                element = round(element,2)
            if row[i] == row[-1]:
                print(" ", element, " "*(liste_longeur_attribut[i]-len(str(element)) - 2), sep = "", end = "")
            else:
                print(" ", element, " "*(liste_longeur_attribut[i]-len(str(element)) - 2), " |", sep = "", end = "")
        print()

def print_clients():
    """print pour eviter la redondance"""
    print_body(1,"Afficher pour tous les clients")
    print_body(2,"Rechercher par nom du client")
    print_body(3,"Rechercher par prénom du client")
    print_body(4,"Rechercher par numéro de téléphone du client")
    print_body("r","Retourner au menu précédent")
    print_body("q", "Quitter le programme")
    print_end()

def demande_nom():
    clear_terminal()
    print("Veuillez saisir le nom à rechercher: ",end="")
    i = input()
    clear_terminal()
    return i

def demande_prenom():
    clear_terminal()
    print("Veuillez saisir le prénom à rechercher: ",end="")
    i = input()
    clear_terminal()
    return i

def demande_numero():
    clear_terminal()
    print("Veuillez saisir le numéro de téléphone à rechercher: ",end="")
    i = input()
    clear_terminal()
    return i

