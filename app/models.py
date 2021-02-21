from app import db

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ent_seq = db.Column(db.Integer, unique=True)
    kanji_element = db.relationship('KanjiElement')
    reading_element = db.relationship('ReadingElement')
    sense = db.relationship('Sense')

class KanjiElement(db.Model):
    entry_id = db.Column(db.Integer, db.ForeignKey('entry.id'))

class KanjiElementInfo(db.Model):
    kanji_element_id = db.Column(db.Integer, db.ForeignKey('kanji_element.id'))
    value = db.Column(db.String(100))

class ReadingElement(db.Model):
    entry_id = db.Column(db.Integer, db.ForeignKey('entry.id'))

class Sense(db.Model):
    entry_id = db.Column(db.Integer, db.ForeignKey('entry.id'))