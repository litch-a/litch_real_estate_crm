# models/client_agent.py
from extensions import db
from datetime import datetime

class ClientAgent(db.Model):
    __tablename__ = 'client_agent'

    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    agent_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    assigned_at = db.Column(db.DateTime, default=datetime.utcnow)

    client = db.relationship('User', foreign_keys=[client_id], backref='assigned_agent')
    agent = db.relationship('User', foreign_keys=[agent_id], backref='assigned_clients')