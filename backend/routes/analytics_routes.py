from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

analytics_bp = Blueprint('analytics_bp', __name__)

@analytics_bp.route('/', methods=['GET'])
@jwt_required()
def get_analytics():
    return jsonify({"message": "Analytics dashboard"})