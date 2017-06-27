from gmt import db

class Clan(db.Model):
    __tablename__ = "clan"
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(64), unique=True)

    def __init__(self, name):
        self.name = username

    def __repr__(self):
        return '<%i. Clan %s>' % (self.id, self.name)

class Family(db.Model):
    __tablename__ = "family"
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(64), unique=True)
    attribute = db.Column('attribute', db.Enum('Stamina','Willpower','Strength','Perception', 'Reflexes', 'Awareness', 'Agility', 'Intelligence', 'Void'))
    clan_id = db.Column('clan_id', db.Integer, db.ForeignKey('clan.id'))

    # Relationships
    clan = db.relationship('Clan', foreign_keys=clan_id)

    def __init__(self, name, attribute, clan_id):
        self.name = name
        self.attribute = attribute
        self.clan_id = clan_id

    def __repr__(self):
        return '<%i. Family %s>' % (self.id, self.name)

class School(db.Model):
    __tablename__ = "school"
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(64), unique=True)
    attribute = db.Column('attribute', db.Enum('Stamina','Willpower','Strength','Perception', 'Reflexes', 'Awareness', 'Agility', 'Intelligence', 'Void'))
    type = db.Column('type', db.Enum('Bushi', 'Shugenja', 'Courtier', 'Monk', 'Artisan', 'Ninja'))
    clan_id = db.Column('clan_id', db.Integer, db.ForeignKey('clan.id'))

    # Relationships
    clan = db.relationship('Clan', foreign_keys=clan_id)

    def __init__(self, name, attribute, type, clan_id):
        self.name = name
        self.attribute = attribute
        self.type = type
        self.clan_id = clan_id

    def __repr__(self):
        return '<%i. School %s>' % (self.id, self.name)

class Forename(db.Model):
    __tablename__ = "forename"
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(64), unique=True)
    gender = db.Column('gender', db.Enum('Male', 'Female'))

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __repr__(self):
        return '<%i. Name %s (%s)>' % (self.id, self.name, self.gender)
        

class Samurai(db.Model):
    __tablename__ = "samurai"
    id = db.Column('id', db.Integer, primary_key=True)
    gender = db.Column('gender', db.Enum('Male', 'Female'))
    clan_id = db.Column('clan_id', db.Integer, db.ForeignKey('clan.id'))
    family_id = db.Column('family_id', db.Integer, db.ForeignKey('family.id'))
    school_id = db.Column('school_id', db.Integer, db.ForeignKey('school.id'))
    forename_id =  db.Column('forename_id', db.Integer, db.ForeignKey('forename.id'))
    notes = db.Column('notes', db.Text)

    # Relationships
    clan = db.relationship('Clan', foreign_keys=clan_id)
    family = db.relationship('Family', foreign_keys=family_id)
    school = db.relationship('School', foreign_keys=school_id)
    forename = db.relationship('Forename', foreign_keys=forename_id)
    
    def __init__(self, gender, clan_id, family_id, school_id, forename_id):
        self.gender = gender
        self.clan_id = clan_id
        self.family_id = family_id
        self.school_id = school_id
        self.forename_id = forename_id
        self.notes = ""

    def __repr__(self):
        return '<%i. Samurai %s, %s (%s) of the %s Clan>' % \
            (self.id, self.family.name, self.forename.name, self.gender, self.clan.name)
