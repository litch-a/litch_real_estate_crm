# models/contact_log.py
from extensions import db
from datetime import datetime

class ContactLog(db.Model):
    __tablename__ = 'contact_logs'

    id = db.Column(db.Integer, primary_key=True)
    agent_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    lead_id = db.Column(db.Integer, db.ForeignKey('leads.id'), nullable=True)
    contact_method = db.Column(db.String(50), nullable=False)  # e.g., phone, email
    notes = db.Column(db.Text)
    contacted_at = db.Column(db.DateTime, default=datetime.utcnow)

    agent = db.relationship('User', foreign_keys=[agent_id], backref='contact_logs_sent')
    client = db.relationship('User', foreign_keys=[client_id], backref='contact_logs_received')
    lead = db.relationship('Lead', backref='contact_logs')