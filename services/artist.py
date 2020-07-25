
from models import Artist
from config import db
from datetime import datetime

def get_all():
    return Artist.query.all()

def get_artist(id):
  artist = Artist.query.get(id)
  upcoming_shows = [show for show in artist.shows if show.start_time > datetime.now()]
  past_shows = [show for show in artist.shows if show.start_time < datetime.now()]
  data = {
    **artist.__dict__,
    'upcoming_shows': upcoming_shows,
    'upcoming_shows_count': len(upcoming_shows),
    'past_shows': past_shows,
    'past_shows_count': len(past_shows)
  }

  return data

def search(keyword):

    '''Return query.'''

    return Artist.query.filter(Artist.name.ilike(f'%{keyword}%'))

def create(data):

    new_artist = Artist(
      name=data.get('name'),
      genres=data.getlist('genres'),
      city=data.get('city'),
      state=data.get('state'),
      phone=data.get('phone'),
      website=data.get('website'),
      facebook_link=data.get('facebook_link')
    )

    db.session.add(new_artist)
    db.session.commit()

    return new_artist.id