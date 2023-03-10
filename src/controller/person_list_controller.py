from src.model.repository.person_repository import PersonsRepository

class PersonListController:
    
    def run(self):
        queryset = PersonsRepository().list()
        response = self._serialize_response(queryset)
        return response
    
    def _serialize_response(self, queryset):
        result = []
        for q in queryset:
            result.append({'name': q.name, 
                           'age': q.age, 
                           'profession': q.profession, 
                           'address': q.address})
        return result