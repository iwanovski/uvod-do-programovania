# Co je to slovnik
from random import randint

# mnozina dvojic - KLUC - HODNOTA

slovnik = {}
slovnik = {"meno": "Ivan", "priezvisko": "Havran"}
slovnik.get("meno")
slovnik["meno"]
print(slovnik)
slovnik["meno"] = "Peter"
slovnik["priezvisko"] = "Peter"
print(slovnik)
print(slovnik.keys())
print(slovnik.values())

# Spocitaj pocet jednotlivych pismen v retazci

retazec = "DnesJePiatehoNovembra"
pismena = []
pocet_pismen = []

slovnik = {}

for pismeno in retazec.lower():
    if pismeno in slovnik.keys():
        # uz som videl to pismeno
        slovnik[pismeno] += 1
        # ind = pismena.index(pismeno)
        # pocet_pismen[ind] += 1
    else:
        # este som nevidel toto pismeno
        # pismena.append(pismeno)
        # pocet_pismen.append(1)
        slovnik[pismeno] = 1
    
    
print(slovnik)
print(pismena)
print(pocet_pismen)

# I - 1
# V - 2
for kluc, hodnota in slovnik.items():
    print(kluc.upper(),"-",hodnota)

slovnik = {
    "meno": "Ivan",
    "priezvisko": "Havran",
    "adresa": {"ulica": "Legionarska",
               "cislo": "10",
               "mesto": "Bratislava"},
}



