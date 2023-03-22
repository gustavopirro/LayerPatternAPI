from src.errors.error_handler import ErrorHandler
from src.model.config.connection import DBConnectionHandler
from src.model.entities.person import Person
from sqlalchemy.exc import IntegrityError
from src.errors.entity_already_exists_exception import EntityAlreadyExistsException

class PersonsRepository:
    def list(self):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Person).all()
                return data
            except Exception as exception:
                db.session.rollback()
                raise exception

    def insert(self, name, age, address, profession):
        with DBConnectionHandler() as db:
            try:
                data_insert = Person(name=name, age=age, address=address, profession=profession)
                db.session.add(data_insert)
                db.session.commit()
            except IntegrityError:
                raise EntityAlreadyExistsException("This entity id already exists at the database!")
            except Exception as exception:
                db.session.rollback()
                ErrorHandler(exception) 
    
    def delete(self, name):
        with DBConnectionHandler() as db:
            try:
                person = db.session.query(Person).filter_by(name=name)
                if not person.count():
                    raise Exception('Person not found')
                person.delete()
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception
