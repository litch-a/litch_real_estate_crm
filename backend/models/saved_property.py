# models/saved_property.py
from extensions import db
from datetime import datetime

class SavedProperty(db.Model):
    __tablename__ = 'saved_properties'

    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    property_id = db.Column(db.Integer, db.ForeignKey('properties.id'), nullable=False)
    saved_at = db.Column(db.DateTime, default=datetime.utcnow)

    client = db.relationship('User', backref='saved_properties')
    property = db.relationship('Property', backref='saved_by_clients')