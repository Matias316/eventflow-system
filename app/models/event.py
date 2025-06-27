from app.services.db import db
from datetime import datetime, timezone

class Event(db.Model):
        
    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc))
    location_id = db.Column(db.Integer, db.ForeignKey("locations.id"), nullable=False)
    location = db.relationship("Location", back_populates="events")

    reservations = db.relationship("Reservation", back_populates="event", cascade="all, delete")


    def __repr__(self):
        return f"<Event {self.title} @ {self.date}>"