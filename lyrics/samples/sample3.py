import sqlalchemy as sa
"""basic database operations using SQLAlchemy. 
It shows how to establish a connection to the database, 
execute SQL queries, perform transactions,
and retrieve data from the database."""

engine = sa.create_engine("postgresql:///students", echo=True)  

conn = engine.connect()
result = conn.execute(sa.text("SELECT * from artists"))
for i in result:
    print (i)
conn.close()


with engine.connect() as conn:
    result = conn.execute(sa.text("INSERT INTO artists (name) VALUES ('Megadeth')"))
    conn.commit() # Without this, the transaction will be rolled back.
                          

with engine.connect() as conn:
    result = conn.execute(sa.text("SELECT * from artists where name = :a"), {"a": "Metallica"})
    for i in result:
        print (i)
