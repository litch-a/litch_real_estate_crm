from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.user import User
from models.lead import Lead
from extensions import db
from models.client_agent import ClientAgent
from werkzeug.security import generate_password_hash

client_bp = Blueprint('client_bp', __name__)

@client_bp.route('/', methods=['GET'])
@jwt_required()
def get_clients():
    return jsonify({"message": "List of clients"})

@client_bp.route('/create_from_lead/<int:lead_id>', methods=['POST'])
@jwt_required()
def create_client_from_lead(lead_id):
    current_user = User.query.get(get_jwt_identity())
    if current_user.role not in ['admin', 'agent']:
        return jsonify({'error': 'Unauthorized'}), 403

    lead = Lead.query.get_or_404(lead_id)

    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    if User.query.filter_by(email=lead.email).first():
        return jsonify({'error': 'Client with this email already exists'}), 409

    new_client = User(
        name=lead.name,
        email=lead.email,
        role='client'
    )
    new_client.set_password(password)

    db.session.add(new_client)
    db.session.flush()  # Get new_client.id before commit

    # Link client to agent
    agent_id = current_user.id if current_user.role == 'agent' else lead.assigned_agent_id
    if not agent_id:
        return jsonify({'error': 'No agent assigned to this lead'}), 400

    link = ClientAgent(client_id=new_client.id, agent_id=agent_id)
    db.session.add(link)

    db.session.commit()

    return jsonify({'message': 'Client account created and linked to agent'}), 201

