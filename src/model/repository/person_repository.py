from src.model.config.connection import DBConnectionHandler
from src.model.entities.person import Person

class PersonsRepository:
    def select(self):
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
            except Exception as exception:
                db.session.rollback()
                raise exception