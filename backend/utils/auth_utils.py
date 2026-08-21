import jwt
import os
from functools import wraps
from flask import request, jsonify
from backend.models import User

SECRET_KEY = os.getenv("SECRET_KEY")


def token_required(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		token = None
		if "Authorization" in request.headers:
			token = request.headers["Authorization"].split(" ")[1]

		if not token:
			return jsonify({"error": "Token missing"}), 401

		try:
			data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
			current_user = User.query.get(data["user_id"])
		except jwt.ExpiredSignatureError:
			return jsonify({"error": "Token expired"}), 401
		except jwt.InvalidTokenError:
			return jsonify({"error": "Invalid token"}), 401

		return f(current_user, *args, **kwargs)
	return decorated