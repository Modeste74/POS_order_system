from flask import Blueprint, request, jsonify
from backend.database import db
from backend.models import User
import jwt
import datetime
import os

auth_bp = Blueprint("auth", __name__)

SECRET_KEY = os.getenv("SECRET_KEY")


@auth_bp.route("/register", methods=["POST"])
def register():
	data = request.json
	if User.query.filter_by(email=data["email"]).first():
		return jsonify({"error": "Email already registered"}), 400

	user = User(username=data["username"], email=data["email"])
	user.set_password(data["password"])

	db.session.add(user)
	db.session.commit()
	return jsonify({"message": "User registered successfully"}), 201


@auth_bp.route("/login", methods=["POST"])
def login():
	data = request.json
	user = User.query.filter_by(email=data["email"]).first()
	if not user or not user.check_password(data["password"]):
		return jsonify({"error": "Invalid credentials"}), 401

	token = jwt.encode(
		{
			"user_id": user.id,
			"exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
		},
		SECRET_KEY,
		algorithm="HS256"
	)
	return jsonify({"token": token})