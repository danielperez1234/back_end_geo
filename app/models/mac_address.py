from app import db

class Mac_address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mac_address = db.Column(db.String(20))