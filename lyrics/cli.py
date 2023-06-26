import argparse
import logging

import crawler
import models
import utils
import web

import sqlalchemy as sa
from sqlalchemy.orm import Session

logger = utils.get_logger()

"""for parsing the CL arguments when running the lyrics appln.
use argparse module to define and parse the arguments"""
def parse():
    parser = argparse.ArgumentParser(prog = "lyrics",description = "Offline song lyrics browser")
    
    parser.add_argument("-d", "--debug", help = "Display detailed debug", action="store_true", default=False)
    
    subparsers = parser.add_subparsers(dest="command")
    """add a subparser for the web command, which runs the web server"""
    subparsers.add_parser("web", help = "Run web server")

    subparsers.add_parser("listartists", help = "List of artists in the system")
    subparsers.add_parser("initdb", help = "Initialise the database")
    crawl_parser = subparsers.add_parser("crawl", help = "Crawl lyrics")

    crawl_parser.add_argument("--nartists", help="Number of artists to crawl (Default : %(default)s)", type=int, 
    default=8)

    crawl_parser.add_argument("--ntracks", help="Number of tracks to crawl per artist (Default : %(default)s)",
    type=int,
    default=5)

    args = parser.parse_args()
    """it returns the parsed  argument, used to determine the desired command"""
    return args

def handle_listartists(args):
    db = models.init_db(web.app, "postgresql:///students")
    with web.app.app_context():
        artists = db.session.execute(db.select(models.Artist)).scalars()
        for idx,artist in enumerate(artists, start=1):
            print (f"{idx}. {artist.name}")

def handle_initdb(args):
    db = models.init_db(web.app, "postgresql:///students")
    with web.app.app_context():
        db.drop_all()
        db.create_all()

"""sets up the database connection and 
initiates the crawling process to scrape lyrics from  website 
based on the provided URL, number of artists, and number of tracks."""

def handle_crawl(args):
    db = models.init_db(web.app, "postgresql:///students")
    crawler.crawl("https://www.songlyrics.com/top-artists-lyrics.html", 
                    args.nartists, 
                    args.ntracks)

def handle_test(args):
    engine = sa.create_engine("postgresql:///students", echo=True)
    query= sa.select(models.Artists)
    with Session(engine) as sess:
        results = sess.scalars(query)
        for artist in results:
            print (artist.name)
            for song in artist.songs:
                print("   ", song.name)

""" function initializes the database and
 starts the Flask development server to run the web application. 
It sets the host, port, and debug mode for the server."""
def handle_web(args):
    db = models.init_db(web.app, "postgresql:///students")
    """Starts the Flask development server to run the web application."""
    web.app.run(host="0.0.0.0", port=8000, debug=True)



def main():
    commands = {"listartists" : handle_listartists,
                "initdb"  : handle_initdb ,
                "crawl" : handle_crawl,
                "web" : handle_web}

    args = parse()
    utils.setup_logger(args.debug)
    commands[args.command](args)

if __name__ == "__main__":
    main()
