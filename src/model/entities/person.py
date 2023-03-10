from src.model.config.base import Base
from sqlalchemy import Column, String, Integer

class Person(Base):
    __tablename__ = "persons"

    name = Column(String, primary_key=True) 
    age = Column(Integer, unique=True, nullable=False)
    address =  Column(String, nullable=False) 
    profession =  Column(String, nullable=False)

    def __repr__(self) -> str:
        return f"{ self.name, self.age, self.address, self.profession }"