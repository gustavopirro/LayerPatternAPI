from src.controller.person_delete_controller import PersonDeleteController
from src.view.person_delete_view import PersonDeleteView

def person_delete_composer():
    person_delete_controller = PersonDeleteController()
    person_delete_view = PersonDeleteView(person_delete_controller)
    return person_delete_view
