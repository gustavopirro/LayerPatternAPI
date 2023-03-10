from typing import Type

from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.views_interface import ViewInterface
from src.controller.interface.crud_interface import CrudInterface

class PersonCreateView(ViewInterface):
    def __init__(self, controller: Type[CrudInterface]) -> None:
        self.__controller = controller

    def handle(self, http_request: Type[HttpRequest]) -> Type[HttpResponse]:
        try:
            body = http_request.body
            request_data = body["person"]

            response = self.__controller.run(request_data)

            return HttpResponse(status_code=200, body={ "response": response })
        except Exception as exception:
            return HttpResponse(status_code=500, body={ "error": str(exception) })
