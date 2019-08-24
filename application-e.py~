import os

from flask import Flask, session, render_template, request, url_for
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

def index():
    return render_template("index.html")

# create a list for usernames
usernames = []

# Provide access to user data
@app.route("/", methods=["POST"])
def login():
    username = request.form.get("username") # create a variable for the username in the form
    password = request.form.get("password") # create a variable for the password in the form
    if session.get("usernames") is None:    # check if the current session has a user who logged in
        session["usernames"] = []           # create a new session for the user
        try:
            db.execute("UPDATE TABLE usernames WHERE (username = username) AND (password = password)") 
            message = "Welcome to the Book App {username}!"
            return render_template("login.html", message=message, username=session["username"])     # welcome the new user
            if request.method == "POST": 
                username = request.form.get("username") # retrieve the user's username for the variable username
                session["usernames"].append(username)   # retrieve the session for the returning user
                username = db.execute("SELECT * FROM usernames WHERE (username = username) AND (password = password)").fetchone
                return render_template("login.html", username=session["username"])
            db.commit()

# create an app that returns the webpage for a boook when the ISBN is entered into the URL
@app.route("/<int:book_isbn>", methods=["POST", "GET"])
        def index(book_isbn):
        book_isbn = db.execute("SELECT isbn FROM books WHERE "book_isbn" = :isbn").fetchone,
            ({"isbn": isbn, "title": title, "author": author, "year": year})
            return render_template("book_isbn.html", isbn={isbn}, title={title}, author={author}, year={year})
            db.commit()

# create an app that returns the search results entered in the search field
@app.route("/", methods=["POST"])
    def search(search):
        search = request.form.get("search") # retrieve the search query
        try: if db.execute("SELECT * FROM books WHERE isbn LIKE %{search}%", {"search":, search}).rowcount == 0:
                except ValueError: 
                search_message="No ISBN matches your search."
                return render_template("error.html", search_message=search_message) # return a template that none of the searches were found
            elif db.execute("SELECT * FROM books WHERE title LIKE %{search}%", {"search":, search_isbn}).rowcount == 0:
                except ValueError: 
                search_message="No title matches your search."
                return render_template("error.html", search_message=search_message) # return a template that none of the searches were found
            elif db.execute("SELECT * FROM books WHERE author LIKE %{search}%", {"search":, search_isbn}).rowcount == 0:
                except ValueError: 
                search_message="No author matches your search."
                return render_template("error.html", search_message=search_message) # return a template that none of the searches were found
                # 
                return render_template("search.html", search=search)
        db.commit()

# gather the reviews that a user has made for a book

@app.route("/<int:isbn>/reviews", methods=["POST", "GET"])
    def review(isbn)
        
        db.execute("SELECT isbn, title, author, review FROM books JOIN reviews ON books.isbn = reviews.isbn WHERE isbn = {"isbn"}").fetchone,
            ({"isbn": isbn, "title": title, "author": author, "year": year, "review": review})
            return render_template("book_isbn.html", isbn={isbn}, title={title}, author={author}, year={year}, review={review})
            db.commit()

if __name__ == "__main__":
    main()
