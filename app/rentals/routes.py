from flask import Blueprint, jsonify, request
from .service import RentalService

rental_bp = Blueprint('rental', __name__)

@rental_bp.route('/rentals', methods=['GET'])
def get_rentals():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    
    paginated_rentals = RentalService.get_paginated_rentals(page, per_page)
    
    return jsonify(paginated_rentals)

@rental_bp.route('/rentals/<int:id>', methods=['GET'])
def get_rental(id):
    rental = RentalService.get_rental(id)
    if rental:
        return jsonify(rental.to_dict())
    return jsonify({"error": "Rental not found"}), 404

@rental_bp.route('/rentals', methods=['POST'])
def create_rental():
    data = request.json
    new_rental = RentalService.create_rental(data)
    return jsonify(new_rental.to_dict()), 201

@rental_bp.route('/rentals/<int:id>', methods=['PUT'])
def update_rental(id):
    data = request.json
    updated_rental = RentalService.update_rental(id, data)
    if updated_rental:
        return jsonify(updated_rental.to_dict())
    return jsonify({"error": "Rental not found"}), 404

@rental_bp.route('/rentals/<int:id>', methods=['DELETE'])
def delete_rental(id):
    if RentalService.delete_rental(id):
        return '', 204
    return jsonify({"error": "Rental not found"}), 404