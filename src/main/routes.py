from flask import Blueprint, request, jsonify

from src.main.adapter.request_adapter import request_adapter
from src.main.composer.person_create_composer import person_create_composer
from src.model.entities.person import Person
routes_bp = Blueprint("api_routes", __name__)


def mock_person():
    return Person('mock person', 30, 'mock address', 'mock profession')

@routes_bp.route("/", methods=["POST"])
def person_create():
    return str(mock_person())
    # http_response = request_adapter(request, person_create_composer())
    # return jsonify(http_response.body), http_response.status_code

@routes_bp.route("/", methods=["GET"])
def person_list():
    return [str(mock_person()) for i in range(0, 10)]
    # http_response = request_adapter(request, person_create_composer())
    # return jsonify(http_response.body), http_response.status_code
