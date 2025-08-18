from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from extensions import db
from models.lead import Lead
from models.user import User

lead_bp = Blueprint('lead_bp', __name__)

#Admin - only route
@lead_bp.route('/', methods=['GET'])
@jwt_required()
def get_leads():
    return jsonify({"message": "List of leads"})

# Admin-only route to assign lead to agent
@lead_bp.route('/assign/<int:lead_id>', methods=['POST'])
@jwt_required()
def assign_lead(lead_id):
    current_user = User.query.get(get_jwt_identity())
    if current_user.role != 'admin':
        return jsonify({'error': 'Unauthorized'}), 403

    data = request.get_json()
    agent_id = data.get('agent_id')

    if not agent_id:
        return jsonify({'error': 'Agent ID is required'}), 400

    agent = User.query.get(agent_id)
    if not agent or agent.role != 'agent':
        return jsonify({'error': 'Invalid agent ID'}), 404

    lead = Lead.query.get_or_404(lead_id)
    lead.assigned_agent_id = agent_id
    db.session.commit()

    return jsonify({'message': f'Lead {lead.id} assigned to agent {agent.name}'}), 200


#Public route - No JWT required
@lead_bp.route('/submit', methods=['POST'])
def submit_lead():
    data = request.get_json()

    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')
    message = data.get('message')
    property_id = data.get('property_id')

    # Basic validation
    if not name or not property_id:
        return jsonify({'error': 'Name and property ID are required'}), 400

    new_lead = Lead(
        name=name,
        email=email,
        phone=phone,
        message=message,
        property_id=property_id
    )

    db.session.add(new_lead)
    db.session.commit()

    return jsonify({'message': 'Lead submitted successfully'}), 201

