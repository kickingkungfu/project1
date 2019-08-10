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
  SET rating = :rating
  WHERE isbn = :isbn
  AND isbn = UNIQUE;
  # include a link to the review for a book
  @app.route("/int:isbn"/review)
  def review()
    return rendertemplate("review.html", "isbn":=isbn) # include an href to the url page for the books reviews using url_for('review')
  
# search database for a book
@app.route("/")
def search():
  request.form.getlist("search")
  
  # Make sure the book is available - review the forms section of the Flask video near the end at 1:24 
  try:
    if db.execute("SELECT * FROM books  
      WHERE isbn OR title OR author = %{search}%", {"search": search}).rowcount == 0:
    except ValueError:
      return render_template("error.html", message="Your request is not available.  Please double check.")
    db.execute("SELECT * FROM books
      WHERE isbn OR title OR author = %search%", {"search": search}).fetchall() = searches[]: # create a list of the searches to be fed into the template where a div is created for each of the results
      return render_template("results.html", search=searches)
      db.commit()
      
  
# print out the information for a book

@app.route ("/<int:index>")
def info(index):
    try:
      db.execute("SELECT * FROM books WHERE {index} = isbn").rowcount == 0:  #see if isbn exists
    except ValueError:
      return render_template("error.html", message="Invalid ISBN.")
    db.execute("FROM books SELECT isbn, title, author, year WHERE {index} = isbn").fetchall()
      for book in books
        return render_template("isbn.html" isbn={books.isbn}, titl={books.title}, author={books.author}, year={books.year})
      
      
      
      
