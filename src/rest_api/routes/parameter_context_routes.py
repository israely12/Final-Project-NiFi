from flask import Blueprint, request, jsonify
from src.nifi_modules.create_parameter_context import create_parameter_context
from src.rest_api.client_provider import client

parameter_context_bp = Blueprint("parameter_context", __name__)

@parameter_context_bp.route("/create", methods=["POST"])
def create_parameter_context_route():
    data = request.get_json()

    name = data.get("name")
    description = data.get("description")
    parameters = data.get("parameters", [])

    result = create_parameter_context(
        client,
        name=name,
        description=description,
        parameters=parameters
    )
    return jsonify(result)
