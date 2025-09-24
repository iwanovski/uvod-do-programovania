# Zoznamy + Slovniky
# zlozene datove struktury
# Ake znamky dostal student v skole
znamka = 1
znamka2 = 3
znamka3 = 4

znamky ="1 3 4"

zoznam_znamok = [1,3,4,8,65,8,5]
# kde jecislo 4
# 3. pozicia/miesto
print(zoznam_znamok)
# Pristup ku konkretnemu prvku
# INDEX = POZICIA - 1
# Vypis cislo 3
print(zoznam_znamok[1])

# Cykly
# Vypiste prvky zoznamu
# musite to zopakovat
# N - 1 krat (N == dlzka/pocet prvkov zoznamu)
for i in range(len(zoznam_znamok)):
    print("Index", i)
    print(zoznam_znamok[i])


zoznam_cisel = [1,2,3,4,5,6,7,8,9]
# Vypocitajte sucet parnych cisel
# v tomto zozname
sucet = 0
for i in range(len(zoznam_cisel)):
    cislo = zoznam_cisel[i]
    if cislo % 2 == 0: # test parnosti
        sucet = sucet + cislo
print(sucet) # 20

# Retazec -> nie je menitelny
test = "Ivan"
print(test)
print(test[0])
# test[0] = "i"
test = "ivan"
print(test)

# Zoznamy aj slovniky su menitelne/upravovatelne
zoznam3 = [1,2,3,4]
print(zoznam3)
zoznam3[0] = 9
print(zoznam3)

# Pridaj cislo do zoznamu
# append(zoznam3, 5)
# volanie pomocou .
# Volanie funkcie ktora je
# naviazana na konkretny typ

# Pridanie na koniec
zoznam3.append(5)
print(zoznam3)
# Odstranenie prvku
zoznam3.remove(3)
print(zoznam3)
# Pridanie na konkretny index
zoznam3.insert(1,55)
print(zoznam3)

# Slovniky
# zhromazduje viacej roznorodych informacii o nejakej
# jednej veci
# slovnik je neusporiadany
# funguje na zaklde dvojic KLUC a HODNOTA
# KLUC je potom unikatny
osoba_parametre = ["meno", "priezvisko"]
osoba_ako_zoznam = ["Ivan", "Havran"]

osoba = {"meno": "Ivan", "priezvisko": "Havran"}
print(osoba)
# Pristup ku klucu
print(osoba["meno"])
# Zmena kluca
osoba["meno"] = "Peter"
print(osoba["meno"])
print(len(osoba))
osoba["brat"] = "Peter"
print(osoba)

# Toto nie je standardny for cyklus
# for each cyklus
for kluc in osoba.keys():
    print("Kluc",kluc)
    print("Hodnota",osoba[kluc])

# Prechadzenie slovnika
for kluc, hodnota in osoba.items():
    print("Kluc",kluc)
    print("Hodnota",hodnota)


zoznam4 = [[1,2,3],[5,9]]
zame = {"meno": "Fero", "pozicia": "vratnik"}
zame2 = {"meno": "Eva", "pozicia": "manazer"}

# moji_zamestnanci = {"1": zame, "2": zame2}
moji_zamestnanci = [zame, zame2]
# id/r.c

# Priradenie
# ak ten kluc existuje, tak si ho prepisem
# slovnik[kluc] = hodnota

# Odstranenie
del osoba["priezvisko"]
print(osoba)



