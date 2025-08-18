from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from utils.decorators import role_required


agent_bp = Blueprint('agent_bp', __name__)

@agent_bp.route('/', methods=['GET'])
@jwt_required()
@role_required("agent")
def get_agents():
    return jsonify({"message": "List of agents"})