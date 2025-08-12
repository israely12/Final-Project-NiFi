from flask import Blueprint, jsonify
from src.rest_api.client_provider import client
from src.nifi_modules.create_connection import create_connection
from configuration import DEST_PG_ID, DEST_PORT_ID, SOURCE_PORT_ID, SOURCE_PG_ID, PROCESS_GROUP_CANVAS_ID

connection_bp = Blueprint("connection", __name__)

@connection_bp.route("/create", methods=["POST"])
def create_connection_route():
    result = create_connection(client, PROCESS_GROUP_CANVAS_ID, SOURCE_PORT_ID, SOURCE_PG_ID, DEST_PORT_ID, DEST_PG_ID)
    return jsonify(result)
