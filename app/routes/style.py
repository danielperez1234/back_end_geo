from flask import Blueprint, request, jsonify
from models.style import Style
from app import db

style_bp = Blueprint('style', __name__)

@style_bp.route('/', methods=['POST'])
def create_style():
    data = request.get_json()
    name = data['name']

    new_style = Style(name=name)
    db.session.add(new_style)
    db.session.commit()

    return jsonify({'message': 'Estilo creado exitosamente'})

@style_bp.route('/', methods=['GET'])
def get_styles():
    styles = Style.query.all()
    return jsonify([{'id': style.id, 'name': style.name} for style in styles])

@style_bp.route('/<int:id>', methods=['GET'])
def get_style(id):
    style = Style.query.get(id)
    if style:
        return jsonify({'id': style.id, 'name': style.name})
    else:
        return jsonify({'message': 'Estilo no encontrado'}), 404

@style_bp.route('/<int:id>', methods=['PUT'])
def update_style(id):
    style = Style.query.get(id)

    if style:
        data = request.get_json()
        style.name = data.get('name', style.name)

        db.session.commit()
        return jsonify({'message': 'Estilo actualizado exitosamente'})
    else:
        return jsonify({'message': 'Estilo no encontrado'}), 404

@style_bp.route('/<int:id>', methods=['DELETE'])
def delete_style(id):
    style = Style.query.get(id)

    if style:
        db.session.delete(style)
        db.session.commit()
        return jsonify({'message': 'Estilo eliminado exitosamente'})
    else:
        return jsonify({'message': 'Estilo no encontrado'}), 404
