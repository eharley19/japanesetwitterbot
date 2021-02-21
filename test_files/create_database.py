from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from bs4 import BeautifulSoup
import pykakasi

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jm_dict.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entry_id = db.Column(db.String(30))
    kana = db.Column(db.String(100))
    kanji = db.Column(db.String(100))
    romaji = db.Column(db.String(100))
    definition = db.Column(db.String(100))

if __name__ == "__main__":
    db.create_all()

print("Reading File")

with open('JMdict_e.xml', 'r', encoding="UTF-8") as f:
    kks = pykakasi.kakasi()
    contents = f.read()
    soup = BeautifulSoup(contents, "lxml")  
    words = []
    excluded_categories = [
        "&sl;",
        "&derog;",
        "&vulg;"
    ]

    entries = soup.findAll('entry')

    for word in entries:
        # import pdb; pdb.set_trace()
        kanji = None
        kana = None
        definition = None
        romaji = None

        if word.find('misc'):
            misc = word.find('misc')
            if misc.string in excluded_categories:
                continue

        # Check to see if we have a kanji element
        if word.find('k_ele'):
            # If we do, extract its inner value
            kanji = word.find('k_ele').find('keb').string

        # Check to see if we have a kana element
        if word.find('r_ele'):
            # If we do, extract its inner value
            kana = word.find('r_ele').find('reb').string
            romaji = kks.convert(kana)[0]['hepburn']


        # Check to see if we have a sense element
        if word.find('sense'):
            # If we do, extract its inner value
            definition = word.find('sense').find('gloss').string

        words.append(
            Word(
                entry_id=word.find('ent_seq').string,
                kanji=kanji,
                kana=kana,
                romaji=romaji,
                definition=definition
            )
        )

    db.session.bulk_save_objects(words)
    db.session.commit()
    