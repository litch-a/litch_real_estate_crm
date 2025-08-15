from extensions import db
from datetime import datetime

class User(db.Model):
    __tablename__='users'

    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100), nullable=False)
    email=db.Column(db.String(100), unique=True, nullable=False)
    password_hash=db.Column(db.Text, nullable=False)
    role=db.Column(db.DateTime, default=datetime.utcnow)

    properties=db.relationship('Property', backref='creator', lazy=True)