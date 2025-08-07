from flask import Blueprint, jsonify
from src.rest_api.client_provider import client
from src.nifi_modules.create_funnel import create_funnel

funnel_bp = Blueprint("funnel", __name__)

@funnel_bp.route("/create", methods=["POST"])
def create_funnel_route():
    result = create_funnel(client)
    return jsonify(result)
