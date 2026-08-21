from flask import Blueprint, request, jsonify
from backend.models import Product
from backend.database import db


product_bp = Blueprint("products", __name__)

@product_bp.route("/", methods=["GET"])
def get_products():
    products = Product.query.all()
    return jsonify([p.to_dict() for p in products])

@product_bp.route("/", methods=["POST"])
def add_product():
    data = request.json
    new_product = Product(
        name=data["name"],
        price=data["price"],
        stock=data.get("stock", 0)
    )

    db.session.add(new_product)
    db.session.commit()
    return jsonify(new_product.to_dict()), 201