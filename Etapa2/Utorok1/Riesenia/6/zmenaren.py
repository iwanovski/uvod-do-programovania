

# Suma v bankovach/minciach

# Dostanete nejaku sumu

# Mate vypocitat kolko akych bankoviek/minci
# potrebujete na jej vyplatenie

suma = int(input("Zadaj sumu: "))

# 500 - 1
pocet_bankoviek = [2,1,0,0,0,0,0,0,0]

# 22
# pouzit co najmensi b/c
# 22 = 5x4 + 2x1
# 22 = 2x10 + 2x1
# 22 = 1x20 + 1x2 NAJMENSI POCET

print(suma)
pouzite_bankovky = []


bankovky = [500,200,100,50,20,10,5,2,1]
slovnik_bankoviek = {"500": 0,
                     "200": 0,
                     "100": 0,
                     "50": 0,
                     "20": 0,
                     "10": 0,
                     "5": 0,
                     "2": 0,
                     "1": 0
                     }

def konvertuj(cislo):
    if cislo < 100 and cislo >= 10:
        cislo = str(cislo) + " "
    elif cislo < 10:
        cislo = str(cislo) + "  "
    return str(cislo)

for bankovka in bankovky:
    # Pokial mam bankovky/mince ktore viem pouzit, odratavam
    while suma >= bankovka:
        # Odrataj hodnotu od sumy
        suma = suma - bankovka
        # Zvys pocet pouzitych bankoviek/minci
        # Keby chceme zarovnat kluce
        # slovnik_bankoviek[konvertuj(bankovka)] += 1
        slovnik_bankoviek[str(bankovka)] += 1
        
    # Skonci skor ak je suma uz 0
    if suma == 0:
        break

for hodnota, pocet in slovnik_bankoviek.items():
    print("Bankovka", hodnota, "Pocet", pocet)


    




