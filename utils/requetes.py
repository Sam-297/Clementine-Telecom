from utils import db
from utils.interface import *
import sqlite3


def prix_forfait_client(conn, num_tel_client = None, nom_client = None, prenom_client = None):
    """
    Affiche la somme payée par chaque client sur sa forfait depuis son date d'inscription

    :param conn: Connexion à la base de données
    """
    if [num_tel_client, nom_client, prenom_client].count(None) < 2:
        print("Erreur parametres: prix_forfait_client")
        exit(1)

    cur = conn.cursor()
    if num_tel_client != None: 
        cur.execute("""
                    SELECT num_tel_client, nom_client, prenom_client, Forfaits.num_forfait, prix_forfait * ((strftime('%Y', 'now') - strftime('%Y', date_inscription_client)) * 12 + -- prix forfaits seuls
                    (strftime('%m', 'now') - strftime('%m', date_inscription_client))) AS total_payé
                    FROM Forfaits JOIN Clients USING (num_forfait)
                    WHERE num_tel_client = ?;
                    """,[num_tel_client])
    elif nom_client != None:
        cur.execute("""
                    SELECT num_tel_client, nom_client, prenom_client, Forfaits.num_forfait, prix_forfait * ((strftime('%Y', 'now') - strftime('%Y', date_inscription_client)) * 12 + -- prix forfaits seuls
                    (strftime('%m', 'now') - strftime('%m', date_inscription_client))) AS total_payé
                    FROM Forfaits JOIN Clients USING (num_forfait)
                    WHERE nom_client = ?;
                    """,[nom_client])
    elif prenom_client != None:
        cur.execute("""
                    SELECT num_tel_client, nom_client, prenom_client, Forfaits.num_forfait, prix_forfait * ((strftime('%Y', 'now') - strftime('%Y', date_inscription_client)) * 12 + -- prix forfaits seuls
                    (strftime('%m', 'now') - strftime('%m', date_inscription_client))) AS total_payé
                    FROM Forfaits JOIN Clients USING (num_forfait)
                    WHERE prenom_client = ?;
                    """,[prenom_client])
    else:
        cur.execute("""
                    SELECT num_tel_client, nom_client, prenom_client, Forfaits.num_forfait, prix_forfait * ((strftime('%Y', 'now') - strftime('%Y', date_inscription_client)) * 12 + -- prix forfaits seuls
                    (strftime('%m', 'now') - strftime('%m', date_inscription_client))) AS total_payé
                    FROM Forfaits JOIN Clients USING (num_forfait);
                    """)


    rows = cur.fetchall()
    desc = cur.description
    print_table(rows, desc)

def prix_appareils_client(conn, num_tel_client = None, nom_client = None, prenom_client = None):
    """
    Affiche la somme payée par chaque client sur ses appareils

    :param conn: Connexion à la base de données
    """
    if [num_tel_client, nom_client, prenom_client].count(None) < 2:
        print("Erreur parametres: prix_appareils_client")
        exit(1)
    cur = conn.cursor()
    if num_tel_client != None:
        cur.execute("""
                    SELECT num_tel_client, nom_client, prenom_client, SUM(prix_appareil) AS total_payé -- prix appareils seuls
                    FROM Clients JOIN Appareils USING(num_tel_client)
                    GROUP BY num_tel_client, nom_client, prenom_client
                    HAVING num_tel_client = ?;
                    """, [num_tel_client])
    elif nom_client != None:
        cur.execute("""
                    SELECT num_tel_client, nom_client, prenom_client, SUM(prix_appareil) AS total_payé -- prix appareils seuls
                    FROM Clients JOIN Appareils USING(num_tel_client)
                    GROUP BY num_tel_client, nom_client, prenom_client
                    HAVING nom_client = ?;
                    """, [nom_client])
    elif prenom_client != None:
        cur.execute("""
                    SELECT num_tel_client, nom_client, prenom_client, SUM(prix_appareil) AS total_payé -- prix appareils seuls
                    FROM Clients JOIN Appareils USING(num_tel_client)
                    GROUP BY num_tel_client, nom_client, prenom_client
                    HAVING prenom_client = ?;
                    """, [prenom_client])
    else:
        cur.execute("""
                    SELECT num_tel_client, nom_client, prenom_client, SUM(prix_appareil) AS total_payé -- prix appareils seuls
                    FROM Clients JOIN Appareils USING(num_tel_client)
                    GROUP BY num_tel_client, nom_client, prenom_client
                    """)

    rows = cur.fetchall()
    desc = cur.description
    print_table(rows, desc)


def prix_reparations_client(conn, num_tel_client = None, nom_client = None, prenom_client = None):
    """
    Affiche la somme payée par chaque client sur toutes ses reparations

    :param conn: Connexion à la base de données
    """
    if [num_tel_client, nom_client, prenom_client].count(None) < 2:
        print("Erreur parametres: prix_appareils_client")
        exit(1)
    cur = conn.cursor()
    if num_tel_client != None:
        cur.execute("""
                    SELECT num_tel_client, nom_client, prenom_client, SUM(prix_reparation) AS total_payé-- prix Reparations
                    FROM Clients JOIN Appareils USING(num_tel_client)
                    JOIN Reparations USING(num_appareil)
                    GROUP BY num_tel_client, nom_client, prenom_client
                    HAVING num_tel_client = ?;
                    """,[num_tel_client])
    elif nom_client != None:
        cur.execute("""
                    SELECT num_tel_client, nom_client, prenom_client, SUM(prix_reparation) AS total_payé-- prix Reparations
                    FROM Clients JOIN Appareils USING(num_tel_client)
                    JOIN Reparations USING(num_appareil)
                    GROUP BY num_tel_client, nom_client, prenom_client
                    HAVING nom_client = ?;
                    """,[nom_client])
    elif prenom_client != None:
        cur.execute("""
                    SELECT num_tel_client, nom_client, prenom_client, SUM(prix_reparation) AS total_payé-- prix Reparations
                    FROM Clients JOIN Appareils USING(num_tel_client)
                    JOIN Reparations USING(num_appareil)
                    GROUP BY num_tel_client, nom_client, prenom_client
                    HAVING prenom_client = ?;
                    """,[prenom_client])
    else:
        cur.execute("""
                    SELECT num_tel_client, nom_client, prenom_client, SUM(prix_reparation) AS total_payé-- prix Reparations
                    FROM Clients JOIN Appareils USING(num_tel_client)
                    JOIN Reparations USING(num_appareil)
                    GROUP BY num_tel_client, nom_client, prenom_client;
                    """)

    rows = cur.fetchall()
    desc = cur.description
    print_table(rows, desc)


def emp_forfaits_clients(conn, num_tel_client = None, nom_client = None, prenom_client = None):
    """
    Affiche la somme d'empreintes carbone par chaque client sur sa forfait depuis de sa date d'inscription

    :param conn: Connexion à la base de données
    """
    if [num_tel_client, nom_client, prenom_client].count(None) < 2:
        print("Erreur parametres: prix_appareils_client")
        exit(1)
    cur = conn.cursor()
    if num_tel_client != None:
        cur.execute("""
                    SELECT num_tel_client, nom_client, prenom_client, Forfaits.num_forfait, emp_carbone_forfait* ((strftime('%Y', 'now') - strftime('%Y', date_inscription_client)) * 12 + -- e.c. forfaits seuls
                    (strftime('%m', 'now') - strftime('%m', date_inscription_client))) AS total_ec
                    FROM Forfaits JOIN Clients USING (num_forfait)
                    WHERE num_tel_client = ?;
                    """, [num_tel_client])
    elif nom_client != None:
        cur.execute("""
                    SELECT num_tel_client, nom_client, prenom_client, Forfaits.num_forfait, emp_carbone_forfait* ((strftime('%Y', 'now') - strftime('%Y', date_inscription_client)) * 12 + -- e.c. forfaits seuls
                    (strftime('%m', 'now') - strftime('%m', date_inscription_client))) AS total_ec
                    FROM Forfaits JOIN Clients USING (num_forfait)
                    WHERE nom_client = ?;
                    """, [nom_client])
    elif prenom_client != None:
        cur.execute("""
                    SELECT num_tel_client, nom_client, prenom_client, Forfaits.num_forfait, emp_carbone_forfait* ((strftime('%Y', 'now') - strftime('%Y', date_inscription_client)) * 12 + -- e.c. forfaits seuls
                    (strftime('%m', 'now') - strftime('%m', date_inscription_client))) AS total_ec
                    FROM Forfaits JOIN Clients USING (num_forfait)
                    WHERE prenom_client = ?;
                    """, [prenom_client])
    else:
        cur.execute("""
                    SELECT num_tel_client, nom_client, prenom_client, Forfaits.num_forfait, emp_carbone_forfait* ((strftime('%Y', 'now') - strftime('%Y', date_inscription_client)) * 12 + -- e.c. forfaits seuls
                    (strftime('%m', 'now') - strftime('%m', date_inscription_client))) AS total_ec
                    FROM Forfaits JOIN Clients USING (num_forfait);
                    """)

    rows = cur.fetchall()
    desc = cur.description
    print_table(rows, desc)


def emp_appareils_clients(conn, num_tel_client = None, nom_client = None, prenom_client = None):
    """
    Affiche la somme d'empreintes carbone par chaque client de tous ses appareils

    :param conn: Connexion à la base de données
    """
    if [num_tel_client, nom_client, prenom_client].count(None) < 2:
        print("Erreur parametres: prix_appareils_client")
        exit(1)

    cur = conn.cursor()
    if num_tel_client != None:
        cur.execute("""
                    SELECT num_tel_client, nom_client, prenom_client, SUM(emp_carbone_appareil) AS total_ec -- e.c. appareils seuls
                    FROM Clients JOIN Appareils USING(num_tel_client)
                    GROUP BY num_tel_client, nom_client, prenom_client
                    HAVING num_tel_client = ?;
                    """, [num_tel_client])
    elif nom_client != None:
        cur.execute("""
                    SELECT num_tel_client, nom_client, prenom_client, SUM(emp_carbone_appareil) AS total_ec -- e.c. appareils seuls
                    FROM Clients JOIN Appareils USING(num_tel_client)
                    GROUP BY num_tel_client, nom_client, prenom_client
                    HAVING nom_client = ?;
                    """, [nom_client])
    elif prenom_client != None:
        cur.execute("""
                    SELECT num_tel_client, nom_client, prenom_client, SUM(emp_carbone_appareil) AS total_ec -- e.c. appareils seuls
                    FROM Clients JOIN Appareils USING(num_tel_client)
                    GROUP BY num_tel_client, nom_client, prenom_client
                    HAVING prenom_client = ?;
                    """, [prenom_client])
    else:
        cur.execute("""
                    SELECT num_tel_client, nom_client, prenom_client, SUM(emp_carbone_appareil) AS total_ec -- e.c. appareils seuls
                    FROM Clients JOIN Appareils USING(num_tel_client)
                    GROUP BY num_tel_client, nom_client, prenom_client;
                    """)

    rows = cur.fetchall()
    desc = cur.description
    print_table(rows, desc)


def emp_reparations_clients(conn, num_tel_client = None, nom_client = None, prenom_client = None):
    """
    Affiche la somme d'empreintes carbone par chaque client de toutes ses reparations

    :param conn: Connexion à la base de données
    """
    if [num_tel_client, nom_client, prenom_client].count(None) < 2:
        print("Erreur parametres: prix_appareils_client")
        exit(1)
    cur = conn.cursor()
    if num_tel_client != None:
        cur.execute("""
                    SELECT num_tel_client, nom_client, prenom_client, SUM(emp_carbone_reparation) AS total_ec -- e.c. Reparations seuls
                    FROM Clients JOIN Appareils USING(num_tel_client)
                    JOIN Reparations USING(num_appareil)
                    GROUP BY num_tel_client, nom_client, prenom_client
                    HAVING num_tel_client = ?;
                    """, [num_tel_client])
    elif nom_client != None:
        cur.execute("""
                    SELECT num_tel_client, nom_client, prenom_client, SUM(emp_carbone_reparation) AS total_ec -- e.c. Reparations seuls
                    FROM Clients JOIN Appareils USING(num_tel_client)
                    JOIN Reparations USING(num_appareil)
                    GROUP BY num_tel_client, nom_client, prenom_client
                    HAVING nom_client = ?;
                    """, [nom_client])
    elif prenom_client != None:
        cur.execute("""
                    SELECT num_tel_client, nom_client, prenom_client, SUM(emp_carbone_reparation) AS total_ec -- e.c. Reparations seuls
                    FROM Clients JOIN Appareils USING(num_tel_client)
                    JOIN Reparations USING(num_appareil)
                    GROUP BY num_tel_client, nom_client, prenom_client
                    HAVING prenom_client = ?;
                    """, [prenom_client])
    else:
        cur.execute("""
                    SELECT num_tel_client, nom_client, prenom_client, SUM(emp_carbone_reparation) AS total_ec -- e.c. Reparations seuls
                    FROM Clients JOIN Appareils USING(num_tel_client)
                    JOIN Reparations USING(num_appareil)
                    GROUP BY num_tel_client, nom_client, prenom_client;
                    """)
        
    rows = cur.fetchall()
    desc = cur.description
    print_table(rows, desc)



def emp_totale_client(conn, num_tel_client = None, nom_client = None, prenom_client = None):
    """
    Affiche la somme d'empreintes carbone pour chaque client

    :param conn: Connexion à la base de données
    """
    if [num_tel_client, nom_client, prenom_client].count(None) < 2:
        print("Erreur parametres: prix_appareils_client")
        exit(1)
    cur = conn.cursor()

    if num_tel_client != None:
        cur.execute("""
                    WITH Empreinte_forfait_par_client AS (
                        SELECT num_tel_client, emp_carbone_forfait * ((strftime('%Y', 'now') - strftime('%Y', date_inscription_client)) * 12 + 
                            (strftime('%m', 'now') - strftime('%m', date_inscription_client))) AS emp_carbone_forfait_totale
                            FROM Forfaits JOIN Clients USING (num_forfait)
                    ), Empreinte_appareil_par_client AS(
                        SELECT num_tel_client, SUM(emp_carbone_appareil) AS emp_carbone_appareil_totale -- e.c. appareils seuls
                        FROM Clients JOIN Appareils USING(num_tel_client)
                        GROUP BY num_tel_client
                    ), Empreinte_reparations_par_client AS (
                        SELECT num_tel_client, SUM(emp_carbone_reparation) AS emp_carbone_reparation_totale-- empreintes Reparations
                        FROM Clients JOIN Appareils USING(num_tel_client)
                        JOIN Reparations USING(num_appareil)
                        GROUP BY num_tel_client
                    )
                    SELECT num_tel_client, nom_client, prenom_client, emp_carbone_forfait_totale + emp_carbone_appareil_totale + emp_carbone_reparation_totale AS emp_carbone_totale
                    FROM Empreinte_forfait_par_client JOIN Empreinte_appareil_par_client USING (num_tel_client) JOIN Clients USING (num_tel_client)
                        JOIN Empreinte_reparations_par_client USING (num_tel_client)
                    WHERE num_tel_client = ?;
                    """, [num_tel_client])
    elif nom_client != None:
        cur.execute("""
                    WITH Empreinte_forfait_par_client AS (
                        SELECT num_tel_client, emp_carbone_forfait * ((strftime('%Y', 'now') - strftime('%Y', date_inscription_client)) * 12 + 
                            (strftime('%m', 'now') - strftime('%m', date_inscription_client))) AS emp_carbone_forfait_totale
                            FROM Forfaits JOIN Clients USING (num_forfait)
                    ), Empreinte_appareil_par_client AS(
                        SELECT num_tel_client, SUM(emp_carbone_appareil) AS emp_carbone_appareil_totale -- e.c. appareils seuls
                        FROM Clients JOIN Appareils USING(num_tel_client)
                        GROUP BY num_tel_client
                    ), Empreinte_reparations_par_client AS (
                        SELECT num_tel_client, SUM(emp_carbone_reparation) AS emp_carbone_reparation_totale-- empreintes Reparations
                        FROM Clients JOIN Appareils USING(num_tel_client)
                        JOIN Reparations USING(num_appareil)
                        GROUP BY num_tel_client
                    )
                    SELECT num_tel_client, nom_client, prenom_client, emp_carbone_forfait_totale + emp_carbone_appareil_totale + emp_carbone_reparation_totale AS emp_carbone_totale
                    FROM Empreinte_forfait_par_client JOIN Empreinte_appareil_par_client USING (num_tel_client) JOIN Clients USING (num_tel_client)
                        JOIN Empreinte_reparations_par_client USING (num_tel_client)
                    WHERE nom_client = ?;
                    """, [nom_client])
    elif prenom_client != None:
        cur.execute("""
                    WITH Empreinte_forfait_par_client AS (
                        SELECT num_tel_client, emp_carbone_forfait * ((strftime('%Y', 'now') - strftime('%Y', date_inscription_client)) * 12 + 
                            (strftime('%m', 'now') - strftime('%m', date_inscription_client))) AS emp_carbone_forfait_totale
                            FROM Forfaits JOIN Clients USING (num_forfait)
                    ), Empreinte_appareil_par_client AS(
                        SELECT num_tel_client, SUM(emp_carbone_appareil) AS emp_carbone_appareil_totale -- e.c. appareils seuls
                        FROM Clients JOIN Appareils USING(num_tel_client)
                        GROUP BY num_tel_client
                    ), Empreinte_reparations_par_client AS (
                        SELECT num_tel_client, SUM(emp_carbone_reparation) AS emp_carbone_reparation_totale-- empreintes Reparations
                        FROM Clients JOIN Appareils USING(num_tel_client)
                        JOIN Reparations USING(num_appareil)
                        GROUP BY num_tel_client
                    )
                    SELECT num_tel_client, nom_client, prenom_client, emp_carbone_forfait_totale + emp_carbone_appareil_totale + emp_carbone_reparation_totale AS emp_carbone_totale
                    FROM Empreinte_forfait_par_client JOIN Empreinte_appareil_par_client USING (num_tel_client) JOIN Clients USING (num_tel_client)
                        JOIN Empreinte_reparations_par_client USING (num_tel_client)
                    WHERE prenom_client = ?;
                    """, [prenom_client])
    else:
        cur.execute("""
                    WITH Empreinte_forfait_par_client AS (
                        SELECT num_tel_client, emp_carbone_forfait * ((strftime('%Y', 'now') - strftime('%Y', date_inscription_client)) * 12 + 
                            (strftime('%m', 'now') - strftime('%m', date_inscription_client))) AS emp_carbone_forfait_totale
                            FROM Forfaits JOIN Clients USING (num_forfait)
                    ), Empreinte_appareil_par_client AS(
                        SELECT num_tel_client, SUM(emp_carbone_appareil) AS emp_carbone_appareil_totale -- e.c. appareils seuls
                        FROM Clients JOIN Appareils USING(num_tel_client)
                        GROUP BY num_tel_client
                    ), Empreinte_reparations_par_client AS (
                        SELECT num_tel_client, SUM(emp_carbone_reparation) AS emp_carbone_reparation_totale-- empreintes Reparations
                        FROM Clients JOIN Appareils USING(num_tel_client)
                        JOIN Reparations USING(num_appareil)
                        GROUP BY num_tel_client
                    )
                    SELECT num_tel_client, nom_client, prenom_client, emp_carbone_forfait_totale + emp_carbone_appareil_totale + emp_carbone_reparation_totale AS emp_carbone_totale
                    FROM Empreinte_forfait_par_client JOIN Empreinte_appareil_par_client USING (num_tel_client) JOIN Clients USING (num_tel_client)
                        JOIN Empreinte_reparations_par_client USING (num_tel_client);
                    """)
    rows = cur.fetchall()
    desc = cur.description
    print_table(rows, desc)

def prix_total_client(conn, num_tel_client = None, nom_client = None, prenom_client = None):
    """
    Affiche la somme totale payé par chaque client

    :param conn: Connexion à la base de données
    """
    if [num_tel_client, nom_client, prenom_client].count(None) < 2:
        print("Erreur parametres: prix_appareils_client")
        exit(1)
    cur = conn.cursor()

    if num_tel_client != None:
        cur.execute("""
                    WITH Prix_forfait_par_client AS (
                        SELECT num_tel_client, prix_forfait * ((strftime('%Y', 'now') - strftime('%Y', date_inscription_client)) * 12 + 
                            (strftime('%m', 'now') - strftime('%m', date_inscription_client))) AS prix_forfait_totale
                        FROM Forfaits JOIN Clients USING (num_forfait)
                    ), Prix_appareil_par_client AS(
                        SELECT num_tel_client, SUM(prix_appareil) AS prix_appareil_totale -- e.c. appareils seuls
                        FROM Clients JOIN Appareils USING(num_tel_client)
                        GROUP BY num_tel_client
                    ), Prix_reparations_par_client AS (
                        SELECT num_tel_client, SUM(prix_reparation) AS prix_reparation_totale-- empreintes Reparations
                        FROM Clients JOIN Appareils USING(num_tel_client)
                        JOIN Reparations USING(num_appareil)
                        GROUP BY num_tel_client
                    )
                    SELECT num_tel_client, nom_client, prenom_client, prix_forfait_totale + prix_appareil_totale + prix_reparation_totale AS prix_totale
                    FROM Prix_forfait_par_client JOIN Prix_appareil_par_client USING (num_tel_client) JOIN Clients USING (num_tel_client)
                    JOIN Prix_reparations_par_client USING (num_tel_client)
                    WHERE num_tel_client = ?;

                    """, [num_tel_client])
    elif nom_client != None:
        cur.execute("""
                    WITH Prix_forfait_par_client AS (
                        SELECT num_tel_client, prix_forfait * ((strftime('%Y', 'now') - strftime('%Y', date_inscription_client)) * 12 + 
                            (strftime('%m', 'now') - strftime('%m', date_inscription_client))) AS prix_forfait_totale
                        FROM Forfaits JOIN Clients USING (num_forfait)
                    ), Prix_appareil_par_client AS(
                        SELECT num_tel_client, SUM(prix_appareil) AS prix_appareil_totale -- e.c. appareils seuls
                        FROM Clients JOIN Appareils USING(num_tel_client)
                        GROUP BY num_tel_client
                    ), Prix_reparations_par_client AS (
                        SELECT num_tel_client, SUM(prix_reparation) AS prix_reparation_totale-- empreintes Reparations
                        FROM Clients JOIN Appareils USING(num_tel_client)
                        JOIN Reparations USING(num_appareil)
                        GROUP BY num_tel_client
                    )
                    SELECT num_tel_client, nom_client, prenom_client, prix_forfait_totale + prix_appareil_totale + prix_reparation_totale AS prix_totale
                    FROM Prix_forfait_par_client JOIN Prix_appareil_par_client USING (num_tel_client) JOIN Clients USING (num_tel_client)
                    JOIN Prix_reparations_par_client USING (num_tel_client)
                    WHERE nom_client = ?;

                    """, [nom_client])
    elif prenom_client != None:
        cur.execute("""
                    WITH Prix_forfait_par_client AS (
                        SELECT num_tel_client, prix_forfait * ((strftime('%Y', 'now') - strftime('%Y', date_inscription_client)) * 12 + 
                            (strftime('%m', 'now') - strftime('%m', date_inscription_client))) AS prix_forfait_totale
                        FROM Forfaits JOIN Clients USING (num_forfait)
                    ), Prix_appareil_par_client AS(
                        SELECT num_tel_client, SUM(prix_appareil) AS prix_appareil_totale -- e.c. appareils seuls
                        FROM Clients JOIN Appareils USING(num_tel_client)
                        GROUP BY num_tel_client
                    ), Prix_reparations_par_client AS (
                        SELECT num_tel_client, SUM(prix_reparation) AS prix_reparation_totale-- empreintes Reparations
                        FROM Clients JOIN Appareils USING(num_tel_client)
                        JOIN Reparations USING(num_appareil)
                        GROUP BY num_tel_client
                    )
                    SELECT num_tel_client, nom_client, prenom_client, prix_forfait_totale + prix_appareil_totale + prix_reparation_totale AS prix_totale
                    FROM Prix_forfait_par_client JOIN Prix_appareil_par_client USING (num_tel_client) JOIN Clients USING (num_tel_client)
                    JOIN Prix_reparations_par_client USING (num_tel_client)
                    WHERE prenom_client = ?;

                    """, [prenom_client])
    else:
        cur.execute("""
                    WITH Prix_forfait_par_client AS (
                        SELECT num_tel_client, prix_forfait * ((strftime('%Y', 'now') - strftime('%Y', date_inscription_client)) * 12 + 
                            (strftime('%m', 'now') - strftime('%m', date_inscription_client))) AS prix_forfait_totale
                        FROM Forfaits JOIN Clients USING (num_forfait)
                    ), Prix_appareil_par_client AS(
                        SELECT num_tel_client, SUM(prix_appareil) AS prix_appareil_totale -- e.c. appareils seuls
                        FROM Clients JOIN Appareils USING(num_tel_client)
                        GROUP BY num_tel_client
                    ), Prix_reparations_par_client AS (
                        SELECT num_tel_client, SUM(prix_reparation) AS prix_reparation_totale-- empreintes Reparations
                        FROM Clients JOIN Appareils USING(num_tel_client)
                        JOIN Reparations USING(num_appareil)
                        GROUP BY num_tel_client
                    )
                    SELECT num_tel_client, nom_client, prenom_client, prix_forfait_totale + prix_appareil_totale + prix_reparation_totale AS prix_totale
                    FROM Prix_forfait_par_client JOIN Prix_appareil_par_client USING (num_tel_client) JOIN Clients USING (num_tel_client)
                    JOIN Prix_reparations_par_client USING (num_tel_client);
                    """)
    rows = cur.fetchall()
    desc = cur.description
    print_table(rows, desc)

def techniciens_non_reparent_x(conn, type_appareil):
    """
    Affiche les techniciens qui ne repare pas un certain type d'appareil

    :param conn: Connexion à la base de données
    :type_appareil
    """
    if type_appareil == None:
        print("Erreur parametre: techniciens_non_reparent")
        exit(1)
    cur = conn.cursor()
    cur.execute("""
                SELECT num_technicien, nom_technicien, prenom_technicien
                FROM Techniciens
                EXCEPT
                SELECT num_technicien, nom_technicien, prenom_technicien
                FROM Techniciens JOIN Interventions USING(num_technicien)
                JOIN Reparations USING (num_reparation) JOIN Appareils USING(num_appareil)
                WHERE type_appareil = ?;
                """, [type_appareil])
    rows = cur.fetchall()
    desc = cur.description
    print_table(rows, desc)


def client_plus_produisant(conn):
    """
    Affiche les techniciens qui ne repare pas un certain type d'appareil

    :param conn: Connexion à la base de données
    :type_appareil
    """
    cur = conn.cursor()
    cur.execute("""
                WITH Emp_Carbone_Client AS (
                    WITH Empreinte_forfait_par_client AS (
                        SELECT num_tel_client, emp_carbone_forfait * ((strftime('%Y', 'now') - strftime('%Y', date_inscription_client)) * 12 + 
                            (strftime('%m', 'now') - strftime('%m', date_inscription_client))) AS emp_carbone_forfait_totale
                        FROM Forfaits JOIN Clients USING (num_forfait)
                    ), Empreinte_appareil_par_client AS(
                        SELECT num_tel_client, SUM(emp_carbone_appareil) AS emp_carbone_appareil_totale -- e.c. appareils seuls
                        FROM Clients JOIN Appareils USING(num_tel_client)
                        GROUP BY num_tel_client
                    ), Empreinte_reparations_par_client AS (
                        SELECT num_tel_client, SUM(emp_carbone_reparation) AS emp_carbone_reparation_totale-- empreintes Reparations
                        FROM Clients JOIN Appareils USING(num_tel_client)
                        JOIN Reparations USING(num_appareil)
                        GROUP BY num_tel_client
                    )
                    SELECT num_tel_client, nom_client, prenom_client, emp_carbone_forfait_totale + emp_carbone_appareil_totale + emp_carbone_reparation_totale AS emp_carbone_totale
                    FROM Empreinte_forfait_par_client JOIN Empreinte_appareil_par_client USING (num_tel_client) JOIN Clients USING (num_tel_client)
                    JOIN Empreinte_reparations_par_client USING (num_tel_client)
                    ), Table_Moyenne_Emp AS(
                    SELECT AVG(emp_carbone_totale) AS Moyenne
                    FROM Emp_Carbone_Client
                )
                SELECT num_tel_client, nom_client, prenom_client, emp_carbone_totale
                FROM Emp_Carbone_Client, Table_Moyenne_Emp
                WHERE emp_carbone_totale > Moyenne;
                """)
    rows = cur.fetchall()
    desc = cur.description
    print_table(rows, desc)

def ajouter_client(conn, num_tel_client, nom_client, prenom_client, addresse_client, num_forfait):
    """
    ajouter un client dans la base de donnees
    """
    cur = conn.cursor()
    try:
        cur.execute("""
                INSERT INTO Clients (num_tel_client, nom_client, prenom_client, adresse_client, date_inscription_client, num_forfait) VALUES
                (?,?,?,?,DATE('now'),?);
                """, [num_tel_client, nom_client, prenom_client, addresse_client, num_forfait])
    except sqlite3.Error as e:
        print(f"\033[91mErreur: {e}\033[0m")
        return False
    return True
    

def ajouter_appareil(conn, num_apareil, modele_appareil, est_neuf_appareil, type_appareil, prix_appareil, emp_carbone_appareil, num_tel_client):
    """
    ajouter un appareil dans la base de donnees
    """
    try: 
        cur = conn.execute("""
            INSERT INTO Appareils (num_appareil, modele_appareil, est_neuf_appareil, type_appareil, prix_appareil, emp_carbone_appareil, num_tel_client) VALUES
            (?,?,?,?,?,?,?)
            """, [num_apareil, modele_appareil, est_neuf_appareil, type_appareil, prix_appareil, emp_carbone_appareil, num_tel_client])
    except sqlite3.Error as e:
        print(f"\033[91mErreur: {e}\033[0m")
        return False
    return True

def afficher_table(conn, table):
    cur = conn.cursor()
    if table == 1:
        cur.execute("""
                    SELECT *
                    FROM Clients;
                    """)
    elif table == 2:
        cur.execute("""
                    SELECT *
                    FROM Forfaits;
                    """)
    elif table == 3:
        cur.execute("""
                    SELECT *
                    FROM Appareils;
                    """)
    elif table == 4:
        cur.execute("""
                    SELECT *
                    FROM Techniciens;
                    """)
    elif table == 5:
        cur.execute("""
                    SELECT *
                    FROM Interventions;
                    """)
    elif table == 6:
        cur.execute("""
                    SELECT *
                    FROM Reparations;
                    """)
    else:
        print("Erreur!")
        exit(1)
    rows = cur.fetchall()
    desc = cur.description
    print_table(rows, desc)

def supprimer_client(conn, num_tel_client):
    cur = conn.cursor()
    try:
        cur.execute("""
                    DELETE FROM Clients 
                    WHERE num_tel_client = ?;
                    """,[num_tel_client])
    except sqlite3.Error as e:
        print(f"\033[91mErreur: {e}\033[0m")
        return False
    return True

def supprimer_appareil(conn, num_appareil):
    cur = conn.cursor()
    try:
        cur.execute("""
                    DELETE FROM Appareils 
                    WHERE num_appareil = ?;
                    """,[num_appareil])
    except sqlite3.Error as e:
        print(f"\033[91mErreur: {e}\033[0m")
        return False
    return True

def modifier_limite_forfait(conn, num_forfait, nouveau_limite):
    cur = conn.cursor()
    try:
        cur.execute("""
                    UPDATE Forfaits
                    SET lim_conso_forfait = ?
                    WHERE num_forfait = ?;
                    """,[nouveau_limite, num_forfait])
    except sqlite3.Error as e:
        print(f"\033[91mErreur: {e}\033[0m")
        return False
    return True
