from flask import Blueprint, request, jsonify
from models.property import Property
from extensions import db
from flask_jwt_extended import jwt_required, get_jwt_identity


property_bp = Blueprint("property_bp", __name__)

# GET /properties/ → list all
@property_bp.route("/", methods=["GET"])
@jwt_required()
def get_properties():
    user_id = get_jwt_identity()
    properties = Property.query.filter_by(created_by=int(user_id)).all()
    data = [
        {
            "id": p.id,
            "title": p.title,
            "description": p.description,
            "address": p.address,
            "price": float(p.price),
            "bedrooms": p.bedrooms,
            "bathrooms": p.bathrooms,
            "square_footage": p.square_footage,
            "category": p.category,
            "status": p.status,
            "created_by": p.created_by,
            "created_at": p.created_at.isoformat()
        } for p in properties
    ]
    return jsonify({"message": "List of properties", "data": data})

# POST /properties/ → create new
@property_bp.route("/", methods=["POST"])
@jwt_required()
def create_property():
    data = request.get_json()
    user_id = get_jwt_identity()

    #Basic validation

    title = data.get('title')
    price = data.get('price')

    if not title or not title.strip():
        return jsonify({'error': 'Title is required'}), 400
    
    if price is None:
        return jsonify({'error': 'Price is required'}), 400
    
    try:
        price = float(price)
        if price < 0:
            return jsonify({'error': 'Price must be non-negative'}), 400
        
    except ValueError:
        return jsonify({'error': 'Price must be a valid number'}), 400
    

    #Proceed with property creation    
    new_property = Property(
        title=title.strip(),
        description=data.get("description"),
        address=data.get("address"),
        price=price,
        bedrooms=data.get("bedrooms"),
        bathrooms=data.get("bathrooms"),
        square_footage=data.get("square_footage"),
        category=data.get("category"),
        status=data.get("status", "available"),
        created_by=int(user_id)  # will be secured later via auth
    )
    db.session.add(new_property)
    db.session.commit()

    return jsonify({"message": "Property created successfully", "id": new_property.id}), 201

# GET /properties/<id> → get one
@property_bp.route("/<int:id>", methods=["GET"])
@jwt_required()

def get_property(id):
    user_id = get_jwt_identity()
    property = Property.query.get_or_404(id)

    if property.created_by != int(user_id):
        return jsonify({"error": "Unauthorized"}), 403
    
    return jsonify({
        "id": property.id,
        "title": property.title,
        "description": property.description,
        "address": property.address,
        "price": float(property.price),
        "bedrooms": property.bedrooms,
        "bathrooms": property.bathrooms,
        "square_footage": property.square_footage,
        "category": property.category,
        "status": property.status,
        "created_by": property.created_by,
        "created_at": property.created_at.isoformat()
    })

# PUT /properties/<id> → update
@property_bp.route("/<int:id>", methods=["PUT"])
@jwt_required()
def update_property(id):

    user_id = get_jwt_identity()
    property = Property.query.get_or_404(id)

    if property.created_by!=int(user_id):
        return jsonify({"error": "Unauthorized"}), 403
    
    data = request.get_json()

    # Optional: validate price if provided
    price = data.get("price")
    if price is not None:
        try:
            price = float(price)
            if price < 0:
                return jsonify({"error": "Price must be non-negative"}), 400
            property.price = price
        except ValueError:
            return jsonify({"error": "Price must be a valid number"}), 400

    # Update other fields
    property.title = data.get("title", property.title)
    property.description = data.get("description", property.description)
    property.address = data.get("address", property.address)
    #property.price = data.get("price", property.price)
    property.bedrooms = data.get("bedrooms", property.bedrooms)
    property.bathrooms = data.get("bathrooms", property.bathrooms)
    property.square_footage = data.get("square_footage", property.square_footage)
    property.category = data.get("category", property.category)
    property.status = data.get("status", property.status)
    db.session.commit()
    return jsonify({"message": "Property updated"})

# DELETE /properties/<id> → delete
@property_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_property(id):
    user_id = get_jwt_identity()
    property = Property.query.get_or_404(id)

    if property.created_by != int(user_id):
        return jsonify({"error": "Unauthorized"}), 403

    db.session.delete(property)
    db.session.commit()
    return jsonify({"message": "Property deleted successfully"}), 200