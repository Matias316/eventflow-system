from app.models import Event, Location
from app.services.db import db

def test_event_model(app):
    with app.app_context():
        location = Location(id=1, name="CandleLight", city="CABA", country="Argentina", capacity=10000)
        db.session.add(location)
        db.session.commit()

        event = Event(id=1, title="Sample Event", location_id = 1)
        db.session.add(event)
        db.session.commit()

        found = Event.query.filter_by(title="Sample Event").first()
        assert found is not None
        assert found.id == 1
