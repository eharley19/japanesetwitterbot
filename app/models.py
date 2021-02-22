from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from bs4 import BeautifulSoup

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