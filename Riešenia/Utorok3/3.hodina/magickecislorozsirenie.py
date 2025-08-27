from random import randint

# Vytvorime si zoznam, v ktorom
# si budeme pamatat cisla, ktore
# sme uz skusili uhadnut
zoznam = []

# Hra na hadanie cisla
magicke_cislo = randint(1, 100)
cislo = int(input("Zadaj cislo"))
zoznam.append(cislo)
# Ako napisem ci sa vyrazy nerovnaju
while magicke_cislo != cislo:
    if cislo > magicke_cislo:
        print("Zadane cislo je vacsie")
    elif cislo < magicke_cislo:
        print("Zadane cislo je mensie")
    cislo = int(input("Zadaj cislo"))
    # Idem skontrolovat, ci uz cislo
    # ktore zadal, este neskusil
    if cislo in zoznam:
        print("Taketo cislo, ci uz hadal")
        print(zoznam)
    else:
        zoznam.append(cislo)
print("Uhadol si cislo")
