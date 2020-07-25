from models import Show, Artist, Venue
from config import db

def get_shows():
    shows = Show.query.all()
    return shows

def create(data):

    artist = Artist.query.get(data.get('artist_id'))
    venue = Venue.query.get(data.get('venue_id'))

    new_show = Show(
        start_time=data.get('start_time'),
        artist_name=artist.name,
        artist_image_link=artist.image_link,
        venue_name=venue.name,
        venue_image_link=venue.image_link
    )


    new_show.venue = venue
    artist.venues.append(new_show)

    db.session.add(new_show)
    db.session.commit()

    return new_show.id