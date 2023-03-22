from cerberus import Validator
from src.errors.bad_request_exception import BadRequestException

person_validator = Validator({
    "person": {
        "type": "dict",
        "schema": {
            "name": { "type": "string", "required": True, "empty": False },
            "age": { "type": "integer", "required": True, "empty": False },
            "address": { "type": "string", "required": True, "empty": False },
            "profession": { "type": "string", "required": True, "empty": False },
        }
    },
})

def validate_data(data):
    response = person_validator.validate(data)

    if response is False:
        raise BadRequestException(f"Bad request received, please correct the following errors:", person_validator.errors) 
