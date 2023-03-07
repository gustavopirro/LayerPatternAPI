class Person:
    
    def __init__(self, name: str, age: int, address: str, profession: str) -> None:
        self.name = name 
        self.age = age 
        self.address = address 
        self.profession = profession

    def __str__(self) -> str:
        return f"{self.name}, {self.age}, {self.address}, {self.profession}"