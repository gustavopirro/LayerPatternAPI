from src.controller.person_list_controller import PersonListController
from src.view.person_list_view import PersonListView

def person_list_composer():
    person_list_controller = PersonListController()
    person_list_view = PersonListView(person_list_controller)
    return person_list_view
