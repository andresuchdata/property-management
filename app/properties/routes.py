from flask import Blueprint, jsonify, request
from .service import PropertyService

property_bp = Blueprint('property', __name__)

@property_bp.route('/properties', methods=['GET'])
def get_properties():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    
    paginated_properties = PropertyService.get_paginated_properties(page, per_page)
    
    return jsonify(paginated_properties)

@property_bp.route('/properties/<int:id>', methods=['GET'])
def get_property(id):
    property = PropertyService.get_property(id)
    if property:
        return jsonify(property.to_dict())
    return jsonify({"error": "Property not found"}), 404

@property_bp.route('/properties', methods=['POST'])
def create_property():
    data = request.json
    new_property = PropertyService.create_property(data)
    return jsonify(new_property.to_dict()), 201

@property_bp.route('/properties/<int:id>', methods=['PUT'])
def update_property(id):
    data = request.json
    updated_property = PropertyService.update_property(id, data)
    if updated_property:
        return jsonify(updated_property.to_dict())
    return jsonify({"error": "Property not found"}), 404

@property_bp.route('/properties/<int:id>', methods=['DELETE'])
def delete_property(id):
    if PropertyService.delete_property(id):
        return '', 204
    return jsonify({"error": "Property not found"}), 404