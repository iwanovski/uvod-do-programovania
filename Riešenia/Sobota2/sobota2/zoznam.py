

# Funkcie naviazane na typ
# lower()

# Funkcie sa volaju pomocou .nazov() notacie
print("MoEECVEACawcawcaWWAcAW".lower())

# Zoznamy = prva komplexnejsia struktura

zoznam = [1, 5, 6, 8]
# mix_zoznam = [1, "test", 5, "test2"

prazdny = []
# Pridanie na koniec zoznamu
prazdny.append(4)
print(prazdny)
# Pridanie na konkretne miesto
prazdny.insert(0, 1)
print(prazdny)
# Odstranenie hodnoty zo zoznamu
prazdny.remove(1)
print(prazdny)

# Dlzka zoznamu
print(len(zoznam))

# Pozicia vs. index
# index = pozicia - 1

print(zoznam[2])
print(zoznam[0])

# Posledny prvok
print(zoznam[len(zoznam)-1])

zoznam3 = [4,8,9,5,2]
# range(5) => [0,1,2,3,4]
# range(8) => [0,1,2,3,4,5,6,7]
for i in range(5):
    print(i)
    print("Hello")

sucet_prvkov = zoznam3[0] + zoznam3[1] + zoznam3[2]

for i in range(len(zoznam3)):
    print(zoznam3[i])

# Sucet prvkov zoznamu
sucet = 0
for i in range(len(zoznam3)):
    sucet = sucet + zoznam3[i]
print(sucet)

# Sucet prvkov zoznamu, ktore su vacsie ako 5
sucet = 0
for i in range(len(zoznam3)):
    prvok = zoznam3[i]
    if prvok > 5:
        sucet = sucet + prvok
print(sucet)



