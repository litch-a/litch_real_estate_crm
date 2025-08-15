from extensions import db

class ClientPreference(db.Model):
    __tablename__ = 'client_preferences'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    min_price = db.Column(db.Numeric)
    max_price = db.Column(db.Numeric)
    bedrooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)
    category = db.Column(db.String(50))
    location = db.Column(db.String(100))