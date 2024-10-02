from flask import Blueprint, jsonify, request
from .service import UserService

user_bp = Blueprint('user', __name__)

@user_bp.route('/users', methods=['GET'])
def get_users():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    
    paginated_users = UserService.get_paginated_users(page, per_page)
    
    return jsonify(paginated_users)

@user_bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = UserService.get_user(id)
    if user:
        return jsonify(user.to_dict())
    return jsonify({"error": "User not found"}), 404

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = UserService.create_user(data)
    return jsonify(new_user.to_dict()), 201

@user_bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.json
    updated_user = UserService.update_user(id, data)
    if updated_user:
        return jsonify(updated_user.to_dict())
    return jsonify({"error": "User not found"}), 404

@user_bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    if UserService.delete_user(id):
        return '', 204
    return jsonify({"error": "User not found"}), 404