from flask import Blueprint, jsonify, request
from .service import PaymentService

payment_bp = Blueprint('payment', __name__)

@payment_bp.route('/payments', methods=['GET'])
def get_payments():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    
    paginated_payments = PaymentService.get_paginated_payments(page, per_page)
    
    return jsonify(paginated_payments)

@payment_bp.route('/payments/<int:id>', methods=['GET'])
def get_payment(id):
    payment = PaymentService.get_payment(id)
    if payment:
        return jsonify(payment.to_dict())
    return jsonify({"error": "Payment not found"}), 404

@payment_bp.route('/payments', methods=['POST'])
def create_payment():
    data = request.json
    new_payment = PaymentService.create_payment(data)
    return jsonify(new_payment.to_dict()), 201

@payment_bp.route('/payments/<int:id>', methods=['PUT'])
def update_payment(id):
    data = request.json
    updated_payment = PaymentService.update_payment(id, data)
    if updated_payment:
        return jsonify(updated_payment.to_dict())
    return jsonify({"error": "Payment not found"}), 404

@payment_bp.route('/payments/<int:id>', methods=['DELETE'])
def delete_payment(id):
    if PaymentService.delete_payment(id):
        return '', 204
    return jsonify({"error": "Payment not found"}), 404