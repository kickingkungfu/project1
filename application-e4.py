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

@app.route("/")
def index():
    return render_template("index.html")

users = []

@app.route("/", methods=["GET", "POST"])
def login():
    # Check the session is empty, create the session and get form information.
    if session.get("users") is None:
        session["users"]
        user = request.form.get("username")
        password = request.form.get("password")
	#Make sure the user exists
    if request.method == "POST":
        user = request.form.get("username")
        password = request.form.get("password")
        db.execute("SELECT * FROM users WHERE username = :username", {"username": user}).rowcount == 0:
	return render_template("login.html", message="Invalid username and/or password.")
    elif db.execute("SELECTdb.execute("INSERT INTO users (user, password) VALUES (:user, password)",
		{"user": username, "password": password})
	db.commit()
		return render_template("enter.html", message="Welcome to the BOOK APP {user}!")
   
@app.route("/logout")
def logout():
    session.pop("username", None)
    return render_template("logout.html", message="You are now logged out!")

if __name__ == "__main__":
    main()
