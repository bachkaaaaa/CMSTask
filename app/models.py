from . import db

class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(100), nullable=False)
    word_example_sentence = db.Column(db.String(255))
    translation = db.Column(db.String(100), nullable=False)
    example_sentence = db.Column(db.String(255))

