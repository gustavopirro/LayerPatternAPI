from src.controller.person_create_controller import PersonCreateController
from src.view.person_create_view import PersonCreateView

def person_create_composer():
    person_create_controller = PersonCreateController()
    person_create_view = PersonCreateView(person_create_controller)
    return person_create_view
