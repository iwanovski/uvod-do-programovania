
# Print = vypis do konzole
# "" = typ retazec (string)

print("Ahoj Svet")

# Premenna
# <nazov> = <hodnota>
meno = "Ivan"
print(meno)

# Hodnotu premennej vieme menit
meno = "Peter"
print(meno)

# SPECIALNE PRE PYTHON
# Premenna moze zmenit svoj
# typ
meno = 10
print(meno)

# Vstup od uzivatela
# Na vstup nam sluzi funkcia input

# Nacitame od uzivatela meno
# a pozdravime ho naspat
meno = input("Zadaj meno")
print("Ahoj", meno)

# Funkcia int
# z retazca urobi cislo
vek = int(input("Zadaj vek"))
print(vek)

# Podmienky
# vyraz = nieco o com vieme povedat
# ci to je pravda alebo nie
# priklad ludksej reci
# "Dnes svieti slnko"

# priklad v kode
# "Mas viac ako 18 rokov"

# if <vyraz>:
# <telo podmienky>

# Ak je tvoj vek viac ako 30
# vypis na vystup
# Mam viac ako 30
if vek > 30:
    print("Mam viac ako 30")
elif vek == 30:
    print("Mam 30")
# Ak nemam 30
# vypis Mas menej ako 30
else:
    print("Mam menej ako 30")

# funkcie
# 1. vstavane funkcie - print, input...
#print()
# 2. nase vlastne funkcie -
# 3. (stiahnutelne funkcie) - ...

# Vlastne funkcie
# defincia != volanie
# vytvorme funkciu, ktora zoberie
# na vstup dve cisla
# a vrati ich sucet


# Definicia funkcie
# def <nazov>():
# <telo funkcie>
def sucet(cislo1, cislo2):
    # print(cislo1 + cislo2)
    return cislo1 + cislo2
    # return None

# Volanie funkcie
vysledok = sucet(9, 8)
print(vysledok)

# Cykly
# 1. cykly s pevnym poctom opakovani
# for cykly
# nejaky prikaz sa vykona nejaky pocet
# krat
# for i in range(<pocet opakovani>):
# <telo cyklu>
for i in range(9):
    vysledok = sucet(15, 24)
    print(vysledok)

# 2. cyklus, ktory nema vopred dany
# pocet opakovani
# while cyklus





