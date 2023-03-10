from src.model.repository.person_repository import PersonsRepository

class PersonCreateController:
    
    def run(self, person_data):
        print(person_data)
        PersonsRepository().insert(
            person_data['name'], 
            person_data['age'], 
            person_data['address'], 
            person_data['profession']
        )