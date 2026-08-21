from flask import Blueprint, request, jsonify
from backend.models import Order, Product
from backend.database import db
from backend.utils.auth_utils import token_required

order_bp = Blueprint("orders", __name__)

@order_bp.route("/", methods=["POST"])
@token_required
def create_order(current_user):
    data = request.json
    items = data["items"]
    # p_id = data

    total = 0
    for item in items:
        product = Product.query.get(item["id"])
        if not product or product.stock < item["qty"]:
            return jsonify({"error": "Invalid product or insufficient stock"}), 400
        
        total += product.price * item["qty"]
        product.stock -= item["qty"]
    
    new_order = Order(
        user_id=current_user.id,
        items=items,
        total=total,
        status="PENDING"
    )
    db.session.add(new_order)
    db.session.commit()

    return jsonify(new_order.to_dict()), 201


@order_bp.route("/<int:order_id>", methods=["GET"])
def get_order(order_id):
    order = Order.query.get(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404
    return jsonify(order.to_dict())


@order_bp.route("/get_orders", methods=["GET"])
@token_required
def get_orders(current_user):
    orders = Order.query.filter_by(user_id=current_user.id).all()
    return jsonify([
        {
            "id": o.id,
            "total": o.total,
            "status": o.status,
            "created_at": o.created_at
        }
        for o in orders
    ])