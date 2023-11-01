from flask import Blueprint, request, jsonify
from models.style import Style
from app import db

style_bp = Blueprint('style', __name__)

"""
    Autor: Josue Meza Lozano
    Descripción: Crea un nuevo estilo.
    Fecha: 2023-10-31
    """
# Método para crear un estilo
@style_bp.route('/', methods=['POST'])
def create_style():
    try:
        # Se obtienen los datos de la petición
        data = request.get_json()
        name = data['name']
        # Se crea el nuevo estilo
        new_style = Style(name=name)
        db.session.add(new_style)
        # Se confirman los cambios
        db.session.commit()
        # Se retorna un mensaje de éxito
        return jsonify({'message': 'Estilo creado exitosamente'}), 200
    # Si ocurre un error, se retorna un mensaje de error 400
    except:
        return jsonify({'message': 'Error al crear el estilo'}), 400

"""
    Autor: Josue Meza Lozano
    Descripción: Obtiene todos los estilos.
    Fecha: 2023-10-31
    """
# Método para obtener todos los estilos
@style_bp.route('/', methods=['GET'])
def get_styles():
    try:
        # Se obtienen todos los estilos de la base de datos
        styles = Style.query.all()
        return jsonify([{'id': style.id, 'name': style.name} for style in styles]), 200
    # Si ocurre un error, se retorna un mensaje de error 404
    except:
        return jsonify({'message': 'Estilos no encontrados'}), 404

"""
    Autor: Josue Meza Lozano
    Descripción: Obtiene un estilo por su id.
    Fecha: 2023-10-31
    """
# Método para obtener un estilo por su id
@style_bp.route('/<int:id>', methods=['GET'])
def get_style(id):
    try:
        # Se obtiene el estilo de la base de datos por su id
        style = Style.query.get(id)
        # Si el estilo existe, se retorna en formato JSON
        if style:
            return jsonify({'id': style.id, 'name': style.name})
        # Si no existe, se retorna un mensaje de error 404
        else:
            return jsonify({'message': 'Estilo no encontrado'}), 404
        # Si ocurre un error, se retorna un mensaje de error 404
    except:
        return jsonify({'message': 'Error al obtener el estilo'}), 500

"""
    Autor: Josue Meza Lozano
    Descripción: Modifica un estilo por su id.
    Fecha: 2023-10-31
    """
# Método para actualizar un estilo por su id
@style_bp.route('/<int:id>', methods=['PUT'])
def update_style(id):
    try:
        # Se obtiene el estilo de la base de datos por su id
        style = Style.query.get(id)
        # Si el estilo existe, se actualiza
        if style:
            # Se obtienen los datos de la petición
            data = request.get_json()
            style.name = data.get('name', style.name)
            # Se confirman los cambios
            db.session.commit()
            return jsonify({'message': 'Estilo actualizado exitosamente'})
        else:
            # Si no existe, se retorna un mensaje de error 404
            return jsonify({'message': 'Estilo no encontrado'}), 404
    # Si ocurre un error, se retorna un mensaje de error 500
    except:
        return jsonify({'message': 'Error al actualizar el estilo'}), 500

"""
    Autor: Josue Meza Lozano
    Descripción: Elimina un estilo por su id.
    Fecha: 2023-10-31
    """
# Método para eliminar un estilo por su id
@style_bp.route('/<int:id>', methods=['DELETE'])
def delete_style(id):
    try:
        # Se obtiene el estilo de la base de datos por su id
        style = Style.query.get(id)
        # Si el estilo existe, se elimina
        if style:
            db.session.delete(style)
            # Se confirman los cambios
            db.session.commit()
            return jsonify({'message': 'Estilo eliminado exitosamente'})
        # Si no existe, se retorna un mensaje de error 404
        else:
            return jsonify({'message': 'Estilo no encontrado'}), 404
    # Si ocurre un error, se retorna un mensaje de error 500
    except:
        return jsonify({'message': 'Error al eliminar el estilo'}), 500
