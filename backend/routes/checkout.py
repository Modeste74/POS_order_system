from flask import Blueprint, jsonify, request, current_app
import stripe
from backend.models import Order
from backend.database import db

checkout_bp = Blueprint("checkout", __name__)

@checkout_bp.route("/create-payment-intent", methods=["POST"])
def create_payment_intent():
    data = request.json
    order_id = data.get("order_id")
    order = Order.query.get(order_id)

    if not order:
        return jsonify({"error": "Order not found"}), 404
    
    if order.status != "PENDING":
        return jsonify({"error": "Order already processed"}), 400

    try:
        stripe.api_key = current_app.config["STRIPE_SECRET_KEY"]

        # Create a PaymentIntent
        intent = stripe.PaymentIntent.create(
            amount=int(round(order.total * 100)), # Stripe in cents
            currency="usd",
            payment_method_types=["card"],
        )

        # Update order status
        order.status = "PAID"
        db.session.commit()

        return jsonify({
            "client_secret": intent.client_secret,
            "order": order.to_dict()
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500