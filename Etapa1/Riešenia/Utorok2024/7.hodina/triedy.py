class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sounds(self):
        print("Animal",self.name, "makes sounds")

# Dedenie od triedy Animal
class Dog(Animal):
    def __init__(self, name, age, race):
        super().__init__(name,age)
        self.race = race

    def make_sounds(self):
        print("Dog",self.name,"barks")


animal = Animal("Rex", 15)
animal.make_sounds()

dog = Dog("Dunco", 10, "retriever")
dog.make_sounds()
