from app import db

class Coordinates(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  lat = db.Column(db.Float)
  lon = db.Column(db.Float)