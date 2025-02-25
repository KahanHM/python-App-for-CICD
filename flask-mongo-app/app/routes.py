from flask import Blueprint, request, jsonify
from app.database import mongo

user_bp = Blueprint('user', __name__)

@user_bp.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    if not data.get("name") or not data.get("email"):
        return jsonify({"error": "Missing fields"}), 400

    mongo.db.users.insert_one(data)
    return jsonify({"message": "User added successfully"}), 201

@user_bp.route('/get_users', methods=['GET'])
def get_users():
    users = list(mongo.db.users.find({}, {"_id": 0}))
    return jsonify(users)
