

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



