# 1. Nacitat nahodne slovo z suboru
from random import choice

def uhadol_si(slovo, hadane):
    for i in range(len(slovo)):
        if slovo[i] == hadane[i]:
            continue
        else:
            return False
    return True

slovo = ""
with open("slova.txt","r") as file:
    riadky = file.readlines()
    slovo = choice(riadky).rstrip()
    # print(slovo)

# 2. Vypisat pocet zivotov, okienka
# na slovo, (vytvorit premmene)
pocet_zivotov = 8
hadane = list("_" * len(slovo))
for i in range(len(hadane)):
    if slovo[i] == " ":
        hadane[i] = " "
print(" ".join(hadane))

# 3. Vytvorit logiku (game loop)
while pocet_zivotov > 0 and not uhadol_si(slovo, hadane):
    vstup = input("Zadaj pismeno: ")
    if vstup == "":
        pocet_zivotov -= 1
    if vstup in slovo:
        for i in range(len(slovo)):
            pismeno = slovo[i]
            if pismeno.lower() == vstup.lower():
                hadane[i] = slovo[i] # vstup
    else:
        pocet_zivotov -= 1
    print(" ".join(hadane))
    print("Pocet zivotov: ",pocet_zivotov)

# 4. Vytvorit pravidla, ked nasa hra
# skonci
if pocet_zivotov == 0:
    print("Prehral si, hladane slovo bolo", slovo)
else:
    print("Vyhral si")

