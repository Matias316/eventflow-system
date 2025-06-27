from app.models.event import Event
from app.services.db import db

def test_event_model(app):
    with app.app_context():
        event = Event(id=1, title="Sample Event")
        db.session.add(event)
        db.session.commit()

        found = Event.query.filter_by(title="Sample Event").first()
        assert found is not None
        assert found.id == 1
