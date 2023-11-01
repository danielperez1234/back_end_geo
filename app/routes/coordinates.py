from flask import Blueprint, request, jsonify
from models.coordinates import Coordinates
from app import db

coordinate_bp = Blueprint('coordinate', __name__)

@coordinate_bp.route('/', methods=['POST'])
def create_coordinate():
    data = request.get_json()
    latitude = data['latitude']
    longitude = data['longitude']

    new_coordinate = Coordinates(latitude=latitude, longitude=longitude)
    db.session.add(new_coordinate)
    db.session.commit()

    return jsonify({'message': 'Coordenada creada exitosamente'})

@coordinate_bp.route('/', methods=['GET'])
def get_coordinates():
    coordinates = Coordinates.query.all()
    return jsonify([{'latitude': coord.latitude, 'longitude': coord.longitude} for coord in coordinates])

@coordinate_bp.route('/<int:id>', methods=['GET'])
def get_coordinate(id):
    coordinate = Coordinates.query.get(id)
    if coordinate:
        return jsonify({'latitude': coordinate.latitude, 'longitude': coordinate.longitude})
    else:
        return jsonify({'message': 'Coordenada no encontrada'}), 404

@coordinate_bp.route('/<int:id>', methods=['PUT'])
def update_coordinate(id):
    coordinate = Coordinates.query.get(id)

    if coordinate:
        data = request.get_json()
        coordinate.latitude = data.get('latitude', coordinate.latitude)
        coordinate.longitude = data.get('longitude', coordinate.longitude)

        db.session.commit()
        return jsonify({'message': 'Coordenada actualizada exitosamente'})
    else:
        return jsonify({'message': 'Coordenada no encontrada'}), 404

@coordinate_bp.route('/<int:id>', methods=['DELETE'])
def delete_coordinate(id):
    coordinate = Coordinates.query.get(id)

    if coordinate:
        db.session.delete(coordinate)
        db.session.commit()
        return jsonify({'message': 'Coordenada eliminada exitosamente'})
    else:
        return jsonify({'message': 'Coordenada no encontrada'}), 404
