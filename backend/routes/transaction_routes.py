from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

transaction_bp = Blueprint('transaction_bp', __name__)

@transaction_bp.route('/', methods=['GET'])
@jwt_required()
def get_transactions():
    return jsonify({"message": "List of transactions"})