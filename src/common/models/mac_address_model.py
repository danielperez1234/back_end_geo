from data_connection import db

class MACAddress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mac_address = db.Column(db.String(17), unique=True, nullable=False)

    def _init_(self, mac_address):
        self.mac_address = mac_address
