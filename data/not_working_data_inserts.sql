INSERT INTO Appareils (num_appareil, modele_appareil, est_neuf_appareil, type_appareil, prix_appareil, emp_carbone_appareil, num_tel_client) VALUES
(1, 'Moulinex', 1, 'Friteuse', 899.99, 5.3, 0124556789); -- Friteuse n'est pas dans TypeAppareil

INSERT INTO Clients (num_tel_client, nom_client, prenom_client, adresse_client, date_inscription_client, num_forfait) VALUES
(0124556789, 'Hajj Assaf', 'Sam', '34 Gare de Lyon', '2021-02-25', 12); -- Un tel numero de telephone deja existe

INSERT INTO Interventions (num_reparation, num_technicien, prix_intervention, emp_carbone_intervention, commentaire_interventon) VALUES
(1, 11, 1599.99, 3.2, 'Tried to rob the company'); -- un technicien qui n'existe pas