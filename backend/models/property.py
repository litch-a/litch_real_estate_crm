from extensions import db
from datetime import datetime

class Property(db.Model):
    __tablename__ = 'properties'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text)
    address = db.Column(db.String(255))
    price = db.Column(db.Numeric, nullable=False)
    bedrooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)
    square_footage = db.Column(db.Integer)
    category = db.Column(db.String(50))
    status = db.Column(db.String(20), default='available')
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    images = db.relationship('PropertyImage', backref='property', lazy=True)