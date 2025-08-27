

# typy: (jednoduche)
# str - retazce, string
# int - cele cisla, integer
# bool - True alebo False, boolean

# zoznamy - zlozeny typ
cislo1 = 1
cislo2 = 3
cislo3 = 5

# Zoznam troch integerov/cisel
zoznam_cisel = [1,3,5]
print(zoznam_cisel)

# Zoznamy su heterogenne
mix_zoznam = [1, True, "slovo"]
print(mix_zoznam)

# Prazdny zoznam
prazdny_zoznam = []

# Prvky v zozname su usporiadane
print(zoznam_cisel)
# Pridaj mi do zoznamu_cisel cislo 9
# append = pridanie na koniec zoznamu
# append(zoznam_cisel, 9)
zoznam_cisel.append(9)
print(zoznam_cisel)

# Standarna funkcia
# nie je naviazana na ziadny typ
print("Hello")

# Funkcie naviazene na typ
# typove funkcie
# <premmenna/hodnota typu>.<nazov_funkcie>()
print("Ivan".upper())

# Ovladanie zoznamu
# Remove
zoznam_cisel.remove(5)
print(zoznam_cisel)

# Pristup k konkretnemu prvku
# na pristup ku konkretnemu prvku
# nam sluzi INDEX
# INDEX = POZICIA - 1
# Vypis prvy prvok
print(zoznam_cisel[0])
# Vypis treti prvok
print(zoznam_cisel[2])

# print(zoznam_cisel[3])
# Pridanie na zaciatok
zoznam_cisel.insert(0, 45)
print(zoznam_cisel)

# Dlzka zoznamu = kolko prvko ma zoznam
print(len(zoznam_cisel))
print(len("IvanHavran"))

sucet = 0
sucet = zoznam_cisel[0] + zoznam_cisel[1] + zoznam_cisel[2] + zoznam_cisel[3]
print(sucet)

# For cyklus + zoznam
for i in range(15):
    # premenna i == pocitadlo
    # riadiaca premenna
    print(i)
    print("Hello")

# range(3)
# -> [0,1,2]

# range(5)
# -> [0,1,2,3,4]

# Sucet cisiel v zozname
sucet = 0
zoznam_cisel = []
print(zoznam_cisel)

for i in range(len(zoznam_cisel)):
    print("I", i)
    print("Prvok na indexe I", zoznam_cisel[i])
    sucet = sucet + zoznam_cisel[i]
    # sucet += zoznam_cisel[i]
print(sucet)

# Uloha
druhy_zoznam = [1,2,3,4,5,6,7,8,9,10]
# Vrat sucet parnych cisel zo zoznamu
sucet_parnych = 0

# PREPOUZIT
# cislo % 2 == 0
for i in range(len(druhy_zoznam)):
    cislo = druhy_zoznam[i]
    # Ak je cislo parne, len vtedy zvysim sucet
    if cislo % 2 == 0:
        sucet_parnych += druhy_zoznam[i]
print(sucet_parnych)






