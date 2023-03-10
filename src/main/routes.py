from flask import Blueprint, request, jsonify

from src.main.adapter.request_adapter import request_adapter
from src.main.composer.person_create_composer import person_create_composer
from src.main.composer.person_list_composer import person_list_composer
routes_bp = Blueprint("api_routes", __name__)


@routes_bp.route("/", methods=["POST"])
def person_create():
    http_response = request_adapter(request, person_create_composer())
    return jsonify(http_response.body), http_response.status_code

@routes_bp.route("/", methods=["GET"])
def person_list():
    http_response = request_adapter(request, person_list_composer())
    return jsonify(http_response.body), http_response.status_code
