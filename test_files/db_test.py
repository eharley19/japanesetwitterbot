from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from bs4 import BeautifulSoup

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jm_dict.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ent_seq = db.Column(db.Integer, unique=True)
    kanji_element = db.relationship('KanjiElement', backref='entry')
    reading_element = db.relationship('ReadingElement', backref='entry')
    sense = db.relationship('Sense', backref='entry')

class KanjiElement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    keb = db.Column(db.String(100))
    entry_id = db.Column(db.Integer, db.ForeignKey('entry.id'))
    kanji_element_info = db.relationship('KanjiElementInfo')

class KanjiElementInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kanji_element = db.Column(db.Integer, db.ForeignKey('kanji_element.id'))
    value = db.Column(db.String(100))

class ReadingElement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entry_id = db.Column(db.Integer, db.ForeignKey('entry.id'))
    value = db.Column(db.String(100))

class Sense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entry_id = db.Column(db.Integer, db.ForeignKey('entry.id'))
    value = db.Column(db.String(100))

db.create_all()

with open('JMdict_e.xml', 'r') as f:
    contents = f.read()
    soup = BeautifulSoup(contents, "lxml")

    print("Started object creation")
    entries = []
    kanji_elements = []
    for entry in soup.findAll("entry"):
        entry_as_int = int(entry.find_next('ent_seq').string)
        entry_to_store = Entry(ent_seq=entry_as_int)
        entries.append(entry_to_store)

        for kanji_element in entry.find_all('k_ele'):
            keb = kanji_element.find_next('keb').string
            if keb:
                kanji_element_to_store = KanjiElement(entry_id=None, keb=keb)
                kanji_elements.append(kanji_element_to_store)
    db.session.bulk_save_objects(entries)
    db.session.bulk_save_objects(kanji_elements)
    print("Ended, now committing")
    db.session.commit()
    print("Done committing")