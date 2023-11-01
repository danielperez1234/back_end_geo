from flask import Blueprint, request, jsonify
from models.coordinates import Coordinates
from app import db

coordinate_bp = Blueprint('coordinate', __name__)

#Métodos para la API de coordenadas
#Se crea una nueva coordenada
@coordinate_bp.route('/', methods=['POST'])
def create_coordinate():
    try:
      #Se obtienen los datos de la petición
      data = request.get_json()
      latitude = data['latitude']
      longitude = data['longitude']

      #Se crea la nueva coordenada
      new_coordinate = Coordinates(latitude=latitude, longitude=longitude)
      #Se agrega la nueva coordenada a la base de datos
      db.session.add(new_coordinate)
      #Se confirman los cambios
      db.session.commit()
      #Se retorna un mensaje de éxito
      return jsonify({'message': 'Coordenada creada exitosamente'})
    except:
      #Si ocurre un error, se retorna un mensaje de error 400
      return jsonify({'message': 'Error al crear la coordenada'}), 400

#Se obtienen todas las coordenadas
@coordinate_bp.route('/', methods=['GET'])
def get_coordinates():
    try:
      #Se obtienen todas las coordenadas de la base de datos
      coordinates = Coordinates.query.all()
      #Se retornan las coordenadas en formato JSON
      return jsonify([{'latitude': coord.latitude, 'longitude': coord.longitude} for coord in coordinates])
    except:
      #Si ocurre un error, se retorna un mensaje de error 404
      return jsonify({'message': 'Coordenadas no encontradas'}), 404

#Se obtiene una coordenada por su id
@coordinate_bp.route('/<int:id>', methods=['GET'])
def get_coordinate(id):
    try:
      #Se obtiene la coordenada de la base de datos por su id
      coordinate = Coordinates.query.get(id)
      #Si la coordenada existe, se retorna en formato JSON
      if coordinate:
          return jsonify({'latitude': coordinate.latitude, 'longitude': coordinate.longitude})
      #Si no existe, se retorna un mensaje de error 404
      else:
          return jsonify({'message': 'Coordenada no encontrada'}), 404
    except:
      #Si ocurre un error, se retorna un mensaje de error 404
      return jsonify({'message': 'Coordenada no encontrada'}), 404

#Se actualiza una coordenada por su id
@coordinate_bp.route('/<int:id>', methods=['PUT'])
def update_coordinate(id):
    try:
      #se obtiene la coordenada de la base de datos por su id
      coordinate = Coordinates.query.get(id)
      #Si la coordenada existe, se actualiza
      if coordinate:
          #Se obtienen los datos de la petición
          data = request.get_json()
          coordinate.latitude = data.get('latitude', coordinate.latitude)
          coordinate.longitude = data.get('longitude', coordinate.longitude)
          #Se confirman los cambios
          db.session.commit()
          #Se retorna un mensaje de éxito
          return jsonify({'message': 'Coordenada actualizada exitosamente'})
      #Si no existe, se retorna un mensaje de error 404
      else:
          return jsonify({'message': 'Coordenada no encontrada'}), 404
    except:
      #Si ocurre un error, se retorna un mensaje de error 400
      return jsonify({'message': 'Error al actualizar la coordenada'}), 400

#Se elimina una coordenada por su id
@coordinate_bp.route('/<int:id>', methods=['DELETE'])
def delete_coordinate(id):
    try:
      #Se obtiene la coordenada de la base de datos por su id
      coordinate = Coordinates.query.get(id)
      #Si la coordenada existe, se elimina
      if coordinate:
          db.session.delete(coordinate)
          db.session.commit()
          return jsonify({'message': 'Coordenada eliminada exitosamente'})
      #Si no existe, se retorna un mensaje de error 404
      else:
          return jsonify({'message': 'Coordenada no encontrada'}), 404
    except:
      #Si ocurre un error, se retorna un mensaje de error 400
      return jsonify({'message': 'Error al eliminar la coordenada'}), 400
