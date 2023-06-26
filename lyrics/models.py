from flask_sqlalchemy import SQLAlchemy

import web

db = SQLAlchemy()

"""for initializing db connection using SQLAlchemy library with flask application .
2 parameters - app:flask, uri: for connecting to db
"""

def init_db(app, db_uri=""):
    try:
        app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
        db.init_app(app)
    except RuntimeError:
        pass
    return db

"""ORM allows to work python object instead of writing raw SQL queries
object creation,updating, deletion and translate  them into appropriate SQL statements"""

"""These models represent the structure of the corresponding db tables"""

"""one to many relationship from artists to tracks and many to one relatioship
 from tracks to artist using foreign key constraints and the relationship attribute of SQLAlchemy"""   
""" provide a convenient way to interact with the data in the db using SQLAlchemy ORM"""

class Artist(db.Model):
    __tablename__ = "artists"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    tracks = db.relationship("Tracks", back_populates="artist")


class Tracks(db.Model):
    __tablename__ = "tracks"
    id = db.Column(db.Integer, primary_key = True)
    artist_id = db.Column(db.Integer, db.ForeignKey("artists.id"))
    name = db.Column(db.String(200))
    lyrics = db.Column(db.Text())
    artist = db.relationship("Artist", back_populates="tracks")
    


"""check if the artist already exists in db, ! create new artists and tracks objects
  and add them to the session and commit changes to db using SQLAlchemy session mgmt"""  

"""SQLAlchemy library is used as the ORM to interact with the postgreSQL db"""
def save_track_to_db(artist_name, track_name, lyrics, db=db):
    with web.app.app_context():
        artist = db.session.scalar(db.select(Artist).filter(Artist.name == artist_name))
        if not artist:
            artist = Artist(name = artist_name)
        track = Tracks(name = track_name, lyrics = lyrics, artist=artist)
        db.session.add_all([artist, track])
        db.session.commit()




    


