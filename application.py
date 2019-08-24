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

@app.route("/", methods=["GET", "POST"])
def index():
	return render_template("index.html", message="Welcome to the Book APP!")

@app.route("/login", methods=["GET", "POST"])
def login_page():
		return render_template("login.html", message="Please log into your account.")

@app.route("/create_account", methods=["POST", "GET"])
def create_account():
	return render_template("create_account.html", user=session["users"], message="Please create a username and password")

users = []
passwords = []

@app.route("/user", methods=["POST", "GET"])
def user():
	if request.method == "GET":
		return render_template("login.html", message="Please log into your account.")
	elif request.method =="POST":
		session["users"] = []
		session["password"] = []
		username = request.form.get("username")
		password = request.form.get("password")
		session["username"].append(username)
		session["password"].append(password)
		return render_template("books.html", user=session["users"])
			
@app.route("/books", methods=["POST", "GET"])
def books():
	if method is "POST":
#Make sure the user exists
		return render_template("books.html", message="Welcome to the Book APP!")
	else:
		return render_template("books.html", message="You are already logged in.")

   
@app.route("/logout")
def logout():
	session.pop("username", None)
	return render_template("logout.html", message="You are now logged out!")

if __name__ == "__main__":
    main()
