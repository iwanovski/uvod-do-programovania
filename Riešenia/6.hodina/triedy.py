

zoznam = [1, 2, 3, 5, 8]

slovnik = {"meno":"Ivan", "priezvisko": "Havran"}
print(slovnik)
def predstav_cloveka(slovnik):
    print(slovnik["meno"])

predstav_cloveka(slovnik)

class Clovek():
    def __init__(self, meno, priezvisko, vek):
        print("Vytvoril som objekt")
        self.meno = meno
        self.priezvisko = priezvisko
        self.vek = vek

        self.vodicak = self.vrat_vodicak()

    def __eq__(self, obj):
        return self.meno == obj.meno

    def predstav_cloveka(self):
        print("Volam sa",self.meno,self.priezvisko)

    def vrat_vodicak(self):
        # Vypiste meno + priezvisko + vek
        # Vypiste ktore skupiny mozem mat ako vodicak
        # ziadne = vek menej ako 15
        # A = 15-16
        # B = 17-xx
        print(self.meno,self.priezvisko,self.vek)
        vodicak = "ziadny"
        if self.vek > 14 and self.vek < 17:
            vodicak = "A"
        elif self.vek >= 17:
            vodicak = "AB"
        return vodicak
        

clovek = Clovek("Peter", "Havran", 5)
print(type(clovek))
clovek2 = Clovek("Ivan", "Havran", 25)

print(clovek.meno)
clovek.predstav_cloveka()
# clovek.vrat_vodicak()
print(clovek.vodicak)



# print(clovek == clovek2)
