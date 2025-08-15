# models/viewing_request.py
from extensions import db
from datetime import datetime

class ViewingRequest(db.Model):
    __tablename__ = 'viewing_requests'

    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    property_id = db.Column(db.Integer, db.ForeignKey('properties.id'), nullable=False)
    requested_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), default='pending')  # pending, confirmed, cancelled
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    client = db.relationship('User', backref='viewing_requests')
    property = db.relationship('Property', backref='viewing_requests')