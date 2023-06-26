import sqlalchemy as sa
from sqlalchemy.orm import Session

"""establishes a connection to the "students" database, 
creates a session using SQLAlchemy's Session object,
executes a parameterized SQL query to retrieve specific rows
from the "artists" table, and prints the results."""

engine = sa.create_engine("postgresql:///students", echo=True)  

statement = sa.text("SELECT id,name FROM artists WHERE name = :a")

with Session(engine) as sess:
    results = sess.execute(statement, {"a" : "Metallica"})
    for i in results:
        print (i)
