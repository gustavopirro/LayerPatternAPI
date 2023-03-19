from typing import Type

from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.views_interface import ViewInterface
from src.controller.interface.crud_interface import CrudInterface

class PersonDeleteView(ViewInterface):
    def __init__(self, controller: Type[CrudInterface]) -> None:
        self.__controller = controller

    def handle(self, http_request: Type[HttpRequest]) -> Type[HttpResponse]:
        try:
            body = http_request.body
            person_name = body["name"]

            response = self.__controller.run(person_name)

            return HttpResponse(status_code=200, body={ "response": response })
        except Exception as exception:
            return HttpResponse(status_code=500, body={ "error": str(exception) })
