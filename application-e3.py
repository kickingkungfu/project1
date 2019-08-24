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

@app.route("/", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    if request.method == 'POST':
            session['username'] = request.form['username']
            db.execute("INSERT INTO users (username, password) VALUES (:username, :password)")
            db.commit()
            return render_template("login.html", message="Welcome to the Book APP {username}!")
    elif db.execute("SELECT * FROM users WHERE ('username' = username) AND ('password' = password)")
    return render_template("login.html", message="Welcome back to the Book APP {username}")
        db.commit()
   
@app.route("/logout")
def logout():
    session.pop("username", None)
    return render_template("logout.html", message="You are now logged out!")

if __name__ == "__main__":
    main()
