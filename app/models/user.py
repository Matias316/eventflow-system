from app.services.db import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    phone = db.Column(db.String(32), nullable=True)

    reservations = db.relationship("Reservation", back_populates="user", cascade="all, delete")

    def __repr__(self):
        return f"<User {self.email}>"
