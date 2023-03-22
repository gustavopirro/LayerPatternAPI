from src.view.http_types.http_response import HttpResponse


class ErrorHandler:

    def __init__(self, exception):
        self.response = self.handle_error(exception)

    def handle_error(self, error):
        if type(error).__name__ == 'BadRequestException':
            return HttpResponse(403, {'response': f'{str(error)} {error.errors}'})
        if type(error).__name__ == 'EntityAlreadyExistsException':
            return HttpResponse(403, {'response': str(error)})
        else:
            return HttpResponse(500, {'response': 'Ocorreu um erro'})
        
