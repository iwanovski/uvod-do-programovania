# Opakovanie funkcie + podmienky

# 1. priklad - funkcia, ktora nam vydeli dve cisla a vrati vysledok

def vydel(cislo1, cislo2):
    if cislo2 == 0:
        # Nulou nedelime
        print("Nulou nedelime")
    else:
        return cislo1 / cislo2

print(vydel(15,3))
vydel(8,0)

# 2. priklad - vrat na aky vodicak mam podla veku narok
# menej ako 16 rokov = ziadny
# 16-17 = A
# 18+ = AB

vek = int(input("Zadaj svoj vek: "))
if vek < 16:
    print("Ziadny")
elif vek >= 16 and vek < 18:
    # Pomocou AND spajame dva vyrazy, oba musia platit
    # Keby pouzijeme OR, musi platit aspon jeden z nich
    print("A")
else:
    print("AB")

# WHILE CYKLUS
# Namiesto poctu kolko krat sa ma nieco vykonavat,
# while cyklus sa vykonava dovtedy, kym plati vyraz
# Ukazka

cislo = 0
while cislo < 5:
    print(cislo)
    # Nezabudnime menit hodnotu ktoru porovname, inak moze
    # vzniknut nekonecny cyklus
    cislo += 1

# 3. Priklad - jednoducha hra uhadni cislo
# Hadame dovtedy, kym netrafime spravne cislo
# Cislo ktore hadame doteraz nastavime vzdy pred spustenim
hadane_cislo = 54
cislo = int(input("Zadaj cislo: "))
while hadane_cislo != cislo:
    if cislo > hadane_cislo:
        print("Cislo ktore si zadal je prilis velke")
    else:
        print("Cislo ktore si zadal je prilis male")
    cislo = int(input("Zadaj cislo: "))
print("Gratulujem, uhadol si cislo")

