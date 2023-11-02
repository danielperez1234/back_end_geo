from flask import Blueprint, request, jsonify
from models.mac_address import Mac_address
from app import db

mac_address_bp = Blueprint('mac_address', __name__)