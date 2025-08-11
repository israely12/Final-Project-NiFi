from flask import Blueprint, jsonify, request
from src.rest_api.client_provider import client
from src.nifi_modules.create_input_port import create_input_port

input_port_bp = Blueprint("input_port", __name__)

@input_port_bp.route("/create", methods=["POST"])
def create_input_port_route():
    result = create_input_port(client)
    return jsonify(result)
