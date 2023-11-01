from app import db

class detail_attraction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200))
    size = db.Column(db.String(50))
    tecnique_id = db.Column(db.Integer, db.ForeignKey('tecnique.id'))
    material_id = db.Column(db.Integer, db.ForeignKey('material.id'))
    style_id = db.Column(db.Integer, db.ForeignKey('style.id'))
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'))
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'))
