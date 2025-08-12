from flask import Blueprint, jsonify, request
from src.rest_api.client_provider import client
from src.nifi_modules.create_output_port import create_output_port

output_port_bp = Blueprint("output_port", __name__)

@output_port_bp.route("/create", methods=["POST"])
def create_output_port_route():
    result = create_output_port(client)
    return jsonify(result)
