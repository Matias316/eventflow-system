from app.services.db import db

class Location(db.Model):
    __tablename__ = "locations"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    city = db.Column(db.String(64), nullable=False)
    country = db.Column(db.String(64), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)

    events = db.relationship("Event", back_populates="location", cascade="all, delete")

    def __repr__(self):
        return f"<Location {self.name} ({self.city}, {self.country})>"
