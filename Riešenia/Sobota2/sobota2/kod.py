# Pouzitie vstavenej kniznica
# Import funkcii
# import <nazov_kniznice>
# import random
# Import konkretnej funkcie
from random import randint


# Vypis hello world
print("Hello World")

print(45)

# Premenne
# nazov premmnej = hodnota
meno = "Ivan"
print(meno)
print(meno)
print(meno)

# Vstup
priezvisko = input()
print(meno, priezvisko)

# Vstup ciselneho typu
# Retazec -> Cislo (niekedy)
# Cislo -> Retazec
vek = input()
print(int(vek) + 10)

# Vystup (print)
# Premenne
# Vstup
# Konverzia typov

# Podmienky
# 3.typ - typ bool
# True/False
# if VYRAZ:
# telo podmienky
if int(vek) > 17:
    print("Mozes mat vodicak")
elif int(vek) > 15:
    print("Mozes mat motorku")
else:
    print("Nemozes mat vodicak")
    
# Vlastne funkcie
# 1. definicia funkcie =>
#    nazov + vstup + prikazy
# 2. volanie funkcie => nazov + ()
# def nazov funkcie():
# telo funkcie
# vstup do funkcie
def vypis_sucet(cislo1, cislo2):
    # print(int(cislo1) + int(cislo2))
    # Funkcie nam vedia vratit hodnotu
    return int(cislo1) + int(cislo2)

print("Zadaj cislo1")
cislo1 = input()
cislo2 = input("Zadaj cislo2")
vysledok = vypis_sucet(cislo1, cislo2)
print(vysledok)
print(cislo1)

# For cyklus
# Cyklus s pevnym poctom opakovani
for i in range(5):
    print("For cyklus")

# While cyklus
# while <vyraz>:
# urob nieco
pokusy = 1
print("Snaz sa uhadnut nezname cislo")
cislo = int(input("Zadaj cislo: "))
spravne_cislo = randint(1,100)
while cislo != spravne_cislo and pokusy != 8:
    print("Neuhadol si cislo")

    # 
    if pokusy < 4:
        print("Zostava ti", 8 - pokusy, "pokusov")
    elif pokusy < 7:
        print("Zostava ti", 8 - pokusy, "pokusy")
    else:
        print("Zostava ti", 8 - pokusy, "pokus")
        
    pokusy = pokusy + 1
    if cislo > spravne_cislo:
        print("Zadal si prilis velke cislo")
    else:
        print("Zadaj si prilis male cislo")
    #if pokusy == 8:
        #break
    cislo = int(input("Zadaj cislo: "))

if pokusy == 8:
    print("Dosli ti pokusy")
else:
    print("Gratulujem, uhadol si cislo")

# Break = ukonci cyklus
# continue = preskoc beh cyklu

















