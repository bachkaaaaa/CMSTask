import json
from app import db
from app.models import Word

def load_initial_data():
    with open("db/sm1_new_kap1.json", "r") as f:
        data = json.load(f)
    for item in data:
        word = Word(
            word=item['wordFirstLang'],
            translation=item['wordSecondLang'],
            example_sentence=item.get('sentenceSecondLang', '')
        )
        db.session.add(word)
    db.session.commit()

