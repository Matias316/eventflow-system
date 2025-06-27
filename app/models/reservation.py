from app.services.db import db
from datetime import datetime, timezone

class Reservation(db.Model):
    __tablename__ = "reservations"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey("events.id"), nullable=False)

    status = db.Column(db.String(32), nullable=False, default="confirmed")
    reserved_at = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc))

    user = db.relationship("User", back_populates="reservations")
    event = db.relationship("Event", back_populates="reservations")

    def __repr__(self):
        return f"<Reservation user={self.user_id} event={self.event_id} status={self.status}>"
