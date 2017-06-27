--- SQL database for Legend of the Five Rings Characters

/* 

Examples to fill database:

INSERT INTO "clan" VALUES(<id>,'<clan-name>');
INSERT INTO "family" VALUES(<id>,'<family-name>','<family-attribute>',<clan-id>); 
INSERT INTO "school" VALUES(<id>,'<school-name>','<school-attribute>','<school-type>',<clan-id>);
INSERT INTO "forename" VALUES(<id>,'<forename>','<gender>');

*/

PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;

--- Clans

DROP TABLE IF EXISTS clan;

CREATE TABLE clan (
        id INTEGER NOT NULL,
        name VARCHAR(64),
	PRIMARY KEY (id), 
	UNIQUE (name)
);

INSERT INTO "clan" VALUES(1,'Clan1');
INSERT INTO "clan" VALUES(2,'Clan2');



--- Families

DROP TABLE IF EXISTS family;

CREATE TABLE family (
	id INTEGER NOT NULL, 
	name VARCHAR(64),
	attribute VARCHAR(64),	
	clan_id INTEGER, 
	PRIMARY KEY (id), 
	UNIQUE (name),
        CHECK (attribute IN ('Stamina','Willpower','Strength','Perception', 'Reflexes', 'Awareness', 'Agility', 'Intelligence', 'Void')),	
	FOREIGN KEY(clan_id) REFERENCES clan (id)
);

INSERT INTO "family" VALUES(1,'Family1','Strength',1);
INSERT INTO "family" VALUES(2,'Family2','Stamina',1);

INSERT INTO "family" VALUES(3,'Family3','Reflexes',2);



--- Schools

DROP TABLE IF EXISTS school;

CREATE TABLE school (
	id INTEGER NOT NULL, 
	name VARCHAR(64),
	attribute VARCHAR(64),
	type VARCHAR(64),
	clan_id INTEGER, 
	PRIMARY KEY (id), 
	UNIQUE (name),
        CHECK (attribute IN ('Stamina','Willpower','Strength','Perception', 'Reflexes', 'Awareness', 'Agility', 'Intelligence', 'Void')),
	CHECK (type IN ('Bushi', 'Shugenja', 'Courtier', 'Monk', 'Artisan', 'Ninja')),
	FOREIGN KEY(clan_id) REFERENCES clan (id)
);


INSERT INTO "school" VALUES(1,'School1','Intelligence','Bushi',1);

INSERT INTO "school" VALUES(2,'School2','Awareness','Courtier',2);
INSERT INTO "school" VALUES(3,'School3','Perception','Shugenja',2);



--- Forename

DROP TABLE IF EXISTS forename;

CREATE TABLE forename (
        id INTEGER NOT NULL,
        name VARCHAR(64),
	gender VARCHAR(64),
	PRIMARY KEY (id), 
	UNIQUE (name),
	CHECK (gender IN ('Male', 'Female'))	
);

INSERT INTO "forename" VALUES(1,'Name1','Male');
INSERT INTO "forename" VALUES(2,'Name2','Female');



--- Samurai

DROP TABLE IF EXISTS samurai;

CREATE TABLE samurai (
        id INTEGER NOT NULL,
        gender VARCHAR(64),
	clan_id INTEGER,
 	family_id INTEGER,
 	school_id INTEGER,
	forename_id INTEGER,
	notes TEXT,
	PRIMARY KEY (id),
 	CHECK (gender IN ('Male', 'Female'))
 	FOREIGN KEY(clan_id) REFERENCES clan (id)
	FOREIGN KEY(family_id) REFERENCES family (id)
	FOREIGN KEY(school_id) REFERENCES school (id)
	FOREIGN KEY(forename_id) REFERENCES forename (id)			
);

			    	 
			    	 
COMMIT;			    	 
