# Project 1

Web Programming with Python and JavaScript


# database for updating/adding reviews
@app.route ("/<int:book_isbn>/reviews")
def reviews():
  review = request.form.get("reviews")
    try:
      reviews = varchar(request.form.get("review")
    except ValueError:
      return render_template("error.html", message="Invalid ISBN.")
      
      
      
      
# select book to review


UPDATE reviews
  SET score = :score
  WHERE isbn = :isbn
  AND isbn = UNIQUE;
  
# search database for a book
@app.route("/")
def search():
  request.form.getlist("search")
# Make sure the book is available
    if db.execute("SELECT * FROM books
      WHERE isbn OR title OR author = %search%", {"search": search}).rowcount == 0:
      return render_template("error.html", message="Your request is not available.  Please double check.")
    db.execute("SELECT * FROM books
      WHERE isbn OR title OR author = %search%", {"search": search}).fetchall():
      db.commit()
      return render_template("results.html")
      
  
# print out the information for a book
books db.execute("SELECT isbn, title, author, year FROM books").fetchall()
  FOR book in books
    print(f"{book.isbn}, 
.execute("SELECT origin, destination, duration FROM flights").fetchall() # execute this SQL command and return all of the results
  for flight in flights
      print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.") # for every flight, print out the flight info
  
