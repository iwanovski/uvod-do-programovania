
from pydantic import BaseModel


# Budeme si chciet vytvarat
# uzivatelov, ktory budu
# mat meno,priezvisko,vek,id


uzivatel = {
    "meno": "Ivan",
    "priezvisko": "Havran",
    "vek": 26
}
print(uzivatel)
uzivatel2 = {
    "meno": "Peter",
    "priezvisko": "Havran",
    "vek": 45,
    "adresa": "Hronska"
}
# zvys_vek(uzivatel)
# vek = vek + 1
# uzivatel["vek"] = uzivatel["vek"] + 1
# Triedy
class Uzivatel():
    def __init__(self, meno, priezvisko, vek):
        if type(meno) != type(""):
            raise Exception()
        self.meno = meno
        self.priezvisko = priezvisko
        self.vek = vek

    def __str__(self):
        return f"{self.meno}, {self.vek}, {self.priezvisko}"

    # 1. zapuzdrenie
    # vyuzivaju sa funkcie
    def zvys_vek(self):
        self.vek = self.vek + 1

# Validacna trieda
class Uzivatel2(BaseModel):
    meno: str
    priezvisko: str
    vek: int

uzivatel2 = Uzivatel2(meno="Ivan",priezvisko="Havran",vek=26)
uzivatel3 = Uzivatel2(meno="Ivan",priezvisko="Havran",vek="26h")
    

# Objekt = jedna instancia triedy
user = Uzivatel("Ivan","Havran",26)
user2 = Uzivatel(26, "Havran", "Ivan")
# 1. zapuzdrenie
# toto by mi v inom jazyku neslo
user.vek = user.vek + 1
user.zvys_vek()
print(user.vek)
print(user)

user2 = Uzivatel("Peter", "Havran", 45)

# 1. zapuzdrenie (encapsulation)
# - priamy pristup k datam nebude existovat
# - alebo bude existovat s kontrolou

# 2. dedicnost (inheritance)
# - triedy medzi sebou dokazu dedit

# Zoologicka zahrada
# budeme tam mat viacej druhov zvierat

class Animal():
    def __init__(self, meno):
        self.meno = meno

    def vydaj_zvuk(self):
        print("Zvuk")

# 4. keby je Animal abstraktna
# tak toto mi zlyha
animal1 = Animal("Jozef")
animal1.vydaj_zvuk()

class Dog(Animal):
    def vydaj_zvuk(self):
        print("Hau")
        
dog1 = Dog("Dunco")
dog1.vydaj_zvuk()

class Cat(Animal):
    def __init__(self, meno, rasa):
        super().__init__(meno)
        self.rasa = rasa
        
    def vydaj_zvuk(self):
        print("Mnau")
        
cat1 = Cat("Garfield", "egyptska macka")
cat1.vydaj_zvuk()

# 3. polymorfizmus (polymorphism)
# - triedy si dokazu prepisovat funkcie
# ktore maju oddedene

# 4. abstrakcia (abstraction)
# - niektore triedy mozu byt abstraktne
# abstraktne znamena, ze nemozeme z nich
# vytvarat objekty


