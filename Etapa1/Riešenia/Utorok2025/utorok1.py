# Vytvorenie premennej
# nazov = hodnota
slova = "Hello World"

# Vypis do konzole
# print = funkcia, ktora nam vypis to co dame do zatvoriek do konzole
# print je nazov tejto funkcie, zavolame ju pomocou zatvoriek
print(slova)
print(10)

# Vstup z konzole
print("Zadaj svoje meno: ")
meno = input()
print(meno)

# Na vstup sluzi funkcia input

priezvisko = input("Zadaj svoje priezvisko ")
print(priezvisko)

# Do premennych ukladame premenne roznych typov
# Pozname dva zakladne typy
# 1. cele cislo - typ int
# 2. retazec znakov (slovo) - typ str, piseme v uvodzovkach a je
# zelenou farbou 

# Ciselny vstup
vek = int(input("Zadaj vek: "))
# musime pouzit funkciu int, aby sme si z retazca urobili cislo

print(meno, priezvisko, vek)
print("O 10 rokov budem mat", vek+10)

# Podmienky
# vetvime nas kod - na zaklade porovnania/vyrazu, sa kod moze chovat rozne
# podmienka ma tvar
# if <vyraz>: urob nieco
# else: urob nieco ine
# Priklad - vek
if vek < 30:
    # Pozor na odsadenie po dvojbodke - pomocou TAB
    print("Mas menej ako 30")
else:
    print("Mas viac ako alebo rovno 30")
