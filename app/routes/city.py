from flask import Blueprint, request, jsonify
from models.city import City
from app import db

city_bp = Blueprint('city', __name__)