DROP VIEW IF EXISTS Reparations;
DROP TABLE IF EXISTS Interventions;
DROP TABLE IF EXISTS Reparations_base;
DROP TABLE IF EXISTS Techniciens;
DROP TABLE IF EXISTS Appareils;
DROP TABLE IF EXISTS Clients;
DROP TABLE IF EXISTS Forfaits;

CREATE TABLE Forfaits (
    num_forfait INTEGER PRIMARY KEY NOT NULL,
    lim_conso_forfait INTEGER NOT NULL,
    prix_forfait REAL NOT NULL,
    emp_carbone_forfait REAL NOT NULL,
    reseau_forfait TypeReseau NOT NULL,
    CONSTRAINT ck1_forfait CHECK (num_forfait > 0),
    CONSTRAINT ck2_forfait CHECK (lim_conso_forfait > 0),
    CONSTRAINT enum_forfait CHECK (reseau_forfait IN ('4G','5G','6G'))
);

CREATE TABLE Clients (
    num_tel_client INTEGER PRIMARY KEY NOT NULL,
    nom_client TEXT NOT NULL,
    prenom_client TEXT NOT NULL,
    adresse_client TEXT NOT NULL,
    date_inscription_client DATE NOT NULL,
    num_forfait INTEGER NOT NULL,
    CONSTRAINT fk_client FOREIGN KEY (num_forfait) REFERENCES Forfaits(num_forfait) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT ck1_client CHECK (num_tel_client > 0) 
);

CREATE TABLE Appareils (
	num_appareil INTEGER PRIMARY KEY NOT NULL,
	modele_appareil TEXT NOT NULL,
	est_neuf_appareil BOOL NOT NULL,
	type_appareil TypeAppareil NOT NULL,
	prix_appareil REAL NOT NULL,
	emp_carbone_appareil REAL NOT NULL,
	num_tel_client INTEGER NOT NULL,
	CONSTRAINT fk_appareils FOREIGN KEY (num_tel_client) REFERENCES Clients(num_tel_client) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT ck1_appareils CHECK (type_appareil IN ('Montre Connectée','Tablette','Téléphone','TV')),
	CONSTRAINT ck2_appareils CHECK (num_appareil > 0)
	CONSTRAINT ck3_appareils CHECK (est_neuf_appareil = 0 OR est_neuf_appareil = 1)
);

CREATE TABLE Reparations_base (
	num_reparation INTEGER PRIMARY KEY NOT NULL,
	date_reparation DATE NOT NULL,
	num_appareil INTEGER NOT NULL,
	CONSTRAINT fk_reparations FOREIGN KEY (num_appareil) REFERENCES Appareils(num_appareil) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT ck_reparations CHECK (num_reparation > 0)
);	

CREATE TABLE Techniciens (
	num_technicien INTEGER PRIMARY KEY NOT NULL,
	nom_technicien TEXT NOT NULL,
	prenom_technicien TEXT NOT NULL,
	debut_contrat_technicien DATE NOT NULL,
	CONSTRAINT ck1_technicien CHECK (num_technicien > 0)
);

CREATE TABLE Interventions (
	num_reparation INTEGER NOT NULL,
	num_technicien INTEGER NOT NULL,
	prix_intervention REAL NOT NULL,
	emp_carbone_intervention REAL NOT NULL,
	commentaire_interventon TEXT NOT NULL,
	CONSTRAINT pk_interventions PRIMARY KEY (num_reparation, num_technicien),
	CONSTRAINT fk1_interventions FOREIGN KEY (num_technicien) REFERENCES Techniciens(num_technicien) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT fk2_interventions FOREIGN KEY (num_reparation) REFERENCES Reparations_base(num_reparation) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE VIEW Reparations (num_reparation, date_reparation, num_appareil, prix_reparation, emp_carbone_reparation) AS
    SELECT num_reparation, date_reparation, num_appareil, ROUND(SUM(prix_intervention), 2) AS prix_reparation, ROUND(SUM(emp_carbone_intervention), 2)AS emp_carbone_reparation
    FROM Reparations_base JOIN Interventions USING (num_reparation)
    GROUP BY num_reparation, date_reparation, num_appareil;