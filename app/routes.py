from flask import Blueprint, render_template,request,redirect,url_for
from app.models import Word
from app import db
from sqlalchemy import or_  # Add this import
from db.load_data import load_initial_data;

from db.load_data import load_initial_data;
app = Blueprint("app", __name__)
@app.before_app_request
def before_first():
    # Load initial data from the JSON file if not already loaded
    if not Word.query.first():  # Only load data if the database is empty
        load_initial_data()
@app.route("/")
def index():
    search_query = request.args.get('search', '')
    if search_query:
        words = Word.query.filter(
            or_(
                Word.word.like(f"%{search_query}%"),
                Word.translation.like(f"%{search_query}%")
            )
        ).all()
    else:
        words = Word.query.all()
    return render_template("index.html", words=words)

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_word(id):
    word = Word.query.get(id)
    if request.method == "POST":
        word.word = request.form["word"]
        word.word_example_sentence=request.form["word_example_sentence"]
        word.translation = request.form["translation"]
        word.example_sentence = request.form["example_sentence"]
        db.session.commit()
        return redirect(url_for("app.index"))
    
    return render_template("edit_word.html", word=word)

@app.route("/delete/<int:id>")
def delete_word(id):
    word = Word.query.get(id)
    db.session.delete(word)
    db.session.commit()
    return redirect(url_for("app.index"))
