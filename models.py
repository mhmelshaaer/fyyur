from config import db
from sqlalchemy import Column, ARRAY, String

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Venue(db.Model):
    __tablename__ = 'venues'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    genres = Column(ARRAY(String))
    address = db.Column(db.String(120))
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    website = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String)
    image_link = db.Column(db.String(500))
    artists = db.relationship('Show', backref='artist_venue')
    shows = db.relationship('Show', backref='show_venue')


class Artist(db.Model):
    __tablename__ = 'artists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    genres = Column(ARRAY(String))
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    website = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String)
    image_link = db.Column(db.String(500))
    venues = db.relationship('Show', backref='venue_artist')
    shows = db.relationship('Show', backref='show_artist')


class Show(db.Model):
    __tablename__ = 'shows'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
    venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'))
    venue_name = db.Column(db.String)
    artist_name = db.Column(db.String)
    venue_image_link = db.Column(db.String(500))
    artist_image_link = db.Column(db.String(500))
    start_time = db.Column(db.DateTime)
    artist = db.relationship("Artist", backref="artist_venues")
    venue = db.relationship("Venue", backref="venue_artists")