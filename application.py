import os

from flask import Flask, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    books = db.execute("SELECT title, author, publication year, ISBN number, review count, average score FROM books").fetchall
    for book in books:
        print(f"{book.title} to {book.title}, {book.author}, {book.publication_year}, {book.ISBN}, {book.reviews}, {book.score}")

@app.route("/")
def index():
    return "Project 1: TODO"
