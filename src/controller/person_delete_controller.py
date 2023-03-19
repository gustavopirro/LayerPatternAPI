from src.model.repository.person_repository import PersonsRepository

class PersonDeleteController:
    
    def run(self, name):
        PersonsRepository().delete(name)