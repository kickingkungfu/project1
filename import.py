import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("books.csv")
    reader = csv.reader(f)
    for ISBN, title, author, published in reader:
        db.execute("INSERT INTO books (ISBN, title, author, published) VALUES (:ISBN, :title, :author, :published)",
                {"ISBN": ISBN, "title": title, "author": author, "published": published})
        print(f"The ISBN {ISBN} for the book {title} written by {author} in {published}.")
    db.commit

    __name__ == "__main__"
    main()
