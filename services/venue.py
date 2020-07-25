from models import Venue, Show
from config import db
from sqlalchemy import func
from datetime import datetime


def get_venues():
    venues_distinct_areas = Venue.query.distinct(Venue.city, Venue.state).all()
    data = []
    for venue in venues_distinct_areas:

        upcoming_shows = db.session.query(
            Show.venue_id, func.count('*').label('num_upcoming_shows')
        ).filter(Show.start_time > datetime.now()).group_by(Show.venue_id).subquery()

        area_venues = db.session.query(
            Venue,
            upcoming_shows.c.num_upcoming_shows
        ).filter(
            Venue.city == venue.city,
            Venue.state == venue.state
        ).outerjoin(
            upcoming_shows,
            Venue.id == upcoming_shows.c.venue_id
        )

        data.append({
            "city": venue.city,
            "state": venue.state,
            "venues": [
                {
                    'id': venue.id,
                    'name': venue.name,
                    'num_upcoming_shows': shows_count if shows_count is not None else 0
                }
                for venue, shows_count in area_venues
            ]
        })

    return data

def get_venue(id):
    venue = Venue.query.get(id)
    upcoming_shows = [show for show in venue.shows if show.start_time > datetime.now()]
    past_shows = [show for show in venue.shows if show.start_time < datetime.now()]
    data = {
    **venue.__dict__,
    'upcoming_shows': upcoming_shows,
    'upcoming_shows_count': len(upcoming_shows),
    'past_shows': past_shows,
    'past_shows_count': len(past_shows)
    }

    return data

def create(data):
    new_venue = Venue(
      name=data.get('name'),
      genres=data.getlist('genres'),
      address=data.get('address'),
      city=data.get('city'),
      state=data.get('state'),
      phone=data.get('phone'),
      website=data.get('website'),
      facebook_link=data.get('facebook_link')
    )

    db.session.add(new_venue)
    db.session.commit()

    return new_venue.id


def search(keyword):

    '''Return query.'''

    return Venue.query.filter(Venue.name.ilike(f'%{keyword}%'))