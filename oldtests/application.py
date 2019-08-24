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

# Prompt user for the ISBN
book_isbn = int(input("/nISBN: "))
book = db.execute("SELECT isbn, title, author, year FROM books WHERE isbn = :isbn",
        {"isbn": book_isbn}).fetchone()

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
db.execute("INSERT INTO books (ISBN_id "

# create a list for usernames
usernames = []

# Provide access to user data
@app.route("/", methods=["POST"])
def login():
    user = request.form.get("username") #create a variable for the username in the form
    password = request.form.get("password") #create a variable for the password in the form
    if session.get("usernames") is None:
        session["usernames"] = []
    if request.method == "POST":
        username = request.form.get("username")
        session["usernames"].append(username)
        username = db.execute("SELECT * FROM usernames WHERE (username = username) AND (password = password)");
    return render_template("login.html", user=user, password=password)

@app.route("/")
def index():
    return render_template("homepage.html")


