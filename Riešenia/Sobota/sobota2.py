# Úlohy z druhého kurzu zo soboty

# Výpis hello world
print("Hello World")

# Vytvorenie premennej s výpisom
meno = "Ivan"
print(meno)

# Vstup
meno = input("Zadaj svoje meno: ")
print("Ahoj", meno)

# Vek - ciselny typ
vek = int(input("Zadaj svoj vek: "))
print("Tvoj vek je",vek)
print("O 10 rokov budes mat",vek+10)

# Podmienky
if vek > 17:
    print("Dospely")
elif vek < 13:
    print("Dieta")
else:
    print("Teen")

# Definicia funkcie
def pozdrav(meno):
    print("Ahoj",meno)
pozdrav("Peter")

# Cykly
for i in range(10):
    print("Hello World")

for i in range(5):
    print(i)

# Zoznamy
zoznam = [1,2,3,4]
print(zoznam)

# pridanie cisla na koniec
zoznam.append(6)
print(zoznam)

# pridanie cisla na zaciatok = index 0
zoznam.insert(0,8)
print(zoznam)

# dlzka zoznamu
print(len(zoznam))

# prvok na indexe 1, teda na druhej pozicii
print(zoznam[1])
