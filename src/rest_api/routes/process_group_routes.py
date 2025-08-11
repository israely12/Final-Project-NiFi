from flask import Blueprint, jsonify
from src.rest_api.client_provider import client
from src.nifi_modules.create_process_group import create_process_group
from src.nifi_modules.get_process_group_by_id import get_process_group_by_id

process_group_bp = Blueprint("process_group", __name__)

@process_group_bp.route("/create", methods=["POST"])
def create_pg_route():
    result = create_process_group(client)
    return jsonify(result)

@process_group_bp.route("/", methods=["GET"])
def get_pg_route():
    result = get_process_group_by_id(client)
    return jsonify(result)
