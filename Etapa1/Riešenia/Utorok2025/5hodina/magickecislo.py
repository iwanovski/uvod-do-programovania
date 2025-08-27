# Kniznica Random
# musime
# 1. Import celej kniznice
# import random

# 2. Importuje iba veci, ktore zadate
from random import randint

# randint(a, b) = a <= CISLO <= b

magicke_cislo = randint(1, 100)
# Budeme hadat cislo, ktore si predtym vymyslime
cislo = int(input("Zadaj cislo:"))
# Budeme sa pytat pomocou inputu, ked zadame
# vacsie cislo, tak nam napise "tvoje cislo je vacsie"
# mensie ....
while cislo != magicke_cislo:
    if cislo > magicke_cislo:
        print("Tvoje cislo je vacsie")
    else:
        print("Tvoje cislo je mensie")
    cislo = int(input("Zadaj cislo:"))
print("Gratulujem, uhadol si cislo")    
