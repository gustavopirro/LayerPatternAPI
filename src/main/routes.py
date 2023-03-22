from flask import Blueprint, request, jsonify

from src.main.adapter.request_adapter import request_adapter
from src.main.composer.person_create_composer import person_create_composer
from src.main.composer.person_list_composer import person_list_composer
from src.main.composer.person_delete_composer import person_delete_composer
from src.validators.person_create_validator import validate_data
from src.errors.error_handler import ErrorHandler
from src.errors.bad_request_exception import BadRequestException
routes_bp = Blueprint("api_routes", __name__)


@routes_bp.route("/", methods=["POST"])
def person_create():
    try:
        validate_data(request.json)
        http_response = request_adapter(request, person_create_composer())
        return jsonify(http_response.body), http_response.status_code
    except BadRequestException as exception:
        response = ErrorHandler(exception).response
        return jsonify(response.body)

@routes_bp.route("/", methods=["GET"])
def person_list():
    http_response = request_adapter(request, person_list_composer())
    return jsonify(http_response.body), http_response.status_code

@routes_bp.route("/", methods=["DELETE"])
def person_delete():
    http_response = request_adapter(request, person_delete_composer())
    return jsonify(http_response.body), http_response.status_code
