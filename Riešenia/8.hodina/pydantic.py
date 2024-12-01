# Pydantic musime mat nainstalovany
from pydantic import BaseModel

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class User2(BaseModel):
    name: str
    age: int

us1 = User("Ivan", 25)
us2 = User("Peter", "55")

user1 = User2("Ivan", 25)
# Nam hodi validacnu chybu
user2 = User2("Peter", "55")
