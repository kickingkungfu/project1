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

# Set up database (creates separate sessions for different users)
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    b = open("books.csv")
    reader = csv.reader(b)
    for ISBN, title, author, published in reader:
        db.execute("INSERT INTO books (ISBN, title, author, published) VALUE (:ISBN, :title, :author, :published)",
        {"ISBN": ISBN, "title": title, "author": author, "published": published})
    db.commit()
        

#Prompt user for the ISBN
book_ISBN = int(input("/nISBN: "))
book = db.execute("SELECT ISBN, title, author, published FROM books WHERE ISBN = :ISBN",
        {"ISBN": book_ISBN}).fetchone()

#make sure ISBN is valid
if ISBN is None:
    print("Error: No such ISBN.")
    return

#Provide book information
        books = db.execute("SELECT title, author, published, ISBN, review count, average score FROM books").fetchall
    for book in books:
        print(f"{book.title} to {book.title}, {book.author}, {book.publication_year}, {book.ISBN}, {book.reviews}, {book.score}")

#Get ISBN information
ISBN = request.form.get ("ISBN")
try:
    ISBN_id = int(request.form.get("ISBN_id"))
except ValueError:
    return render_template("error.html", message="No such ISBN.  Please try again")

#Make sure review does not exist
if db.execute("SELECT * FROM books WHERE ISBN_id = :ISBN", {"ISBN_id": ISBN}).rowcount == 0:
    render_template("error.html", message="No such ISBN available.")
db.execute("INSERT INTO books (ISBN_id


#Provide access to user data
def login():
    username = db.execute("SELECT * FROM users WHERE (username = username) AND (password = password)");

@app.route("/")
def index():
    return "Project 1: TODO"


