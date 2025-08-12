from flask import Blueprint, jsonify, request
from src.rest_api.client_provider import client
from src.nifi_modules.create_process_group import create_process_group
from src.nifi_modules.get_process_group_by_id import get_process_group_by_id
from src.nifi_modules.update_process_group_name import update_process_group_name
from src.nifi_modules.create_full_process_group_setup import create_full_process_group_setup


process_group_bp = Blueprint("process_group", __name__)

@process_group_bp.route("/create", methods=["POST"])
def create_pg_route():
    result = create_process_group(client)
    return jsonify(result)

@process_group_bp.route("/", methods=["GET"])
def get_pg_route():
    result = get_process_group_by_id(client)
    return jsonify(result)

@process_group_bp.route("/update-name", methods=["PUT"])
def update_pg_name_route():
    data = request.get_json()
    new_name = data.get("new_name")
    if not new_name:
        return jsonify({"error": "new_name is required"}), 400

    result = update_process_group_name(client, new_name)
    return jsonify(result)

@process_group_bp.route("/create-with-ports", methods=["POST"])
def create_pg_with_ports_route():
    result = create_full_process_group_setup(client)
    return jsonify(result)