# Cykly
# Cyklus s pevnym poctom opakovani
# FOR cyklus
for pocitadlo in range(5):
    #if j == 1:
        #continue
    print(pocitadlo)
    if pocitadlo == 1:
        continue
    print("Prikaz v cykle")
    if pocitadlo == 3:
        break

# Typy int, string, bool, float (desatinne cislo), None

# Zlozene typy
# zoznam / list/array
zoznam = [1,4,5,8,9,4,6]
print(zoznam)
# range(5) - na pozadi vrati [0,1,2,3,4]

# Cyklus s neznamym poctom opakovani
# WHILE cyklus
# while <vyraz>:
# V inom jazyku
# for (i = 0, i++, i < 5)
i = 0
while i < 5:
    print(i)
    print("Prikaz v cykle")
    i = i + 1

vstup = ""
while vstup != "Koniec":
    vstup = input("Zadaj vstup: ")

# Napiste sucet dvoch cisel pomocou cyklu FOR/WHILE
# ale nemozte pouzit sucet cislo1 + cislo2
def cyklovy_sucet(cislo1, cislo2):
    # Nemozem pouzit
    # return cislo1 + cislo2
    # Potrebujem cyklus
    vysledok = cislo1
    for i in range(cislo2):
        vysledok = vysledok + 1
    return vysledok


