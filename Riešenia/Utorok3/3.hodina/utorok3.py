# Nacitanie vstavej kniznice
# 1.sposob nacitania
# nacitanie celej kniznice
# import random

# 2.sposob nacitania
# nacitanie konkretnej funkcie
# z vstavej kniznice
from random import randint

# For cyklus

print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")

for i in range(5):
    print("Hello")

# While cykly
# cyklus sa vykonava
# kym plati vyraz(podmienka)
# while <vyraz>:
i = 0
while i < 5:
    print("Hello from While")
    i = i + 1
print("Koniec programu")


# Hra na hadanie cisla
magicke_cislo = randint(1, 100)
cislo = int(input("Zadaj cislo"))
# Ako napisem ci sa vyrazy nerovnaju
while magicke_cislo != cislo:
    if cislo > magicke_cislo:
        print("Zadane cislo je vacsie")
    elif cislo < magicke_cislo:
        print("Zadane cislo je mensie")
    cislo = int(input("Zadaj cislo"))
print("Uhadol si cislo")
