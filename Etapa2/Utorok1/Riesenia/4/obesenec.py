# Random -> pseudo nahodnost
# from <library/module> import <funkcia>
from random import choice
# Hra obesenec

# 1. nacitanie slova
slovnik_slov = ["autobus", "lavica", "rebrik", "jedlicka", "stolicka"]
slovo = choice(slovnik_slov)
dlzka = len(slovo)

# chceme to mat ako string/zoznam
# hladane_slovo by mal byt zoznam
# aby sme ho mohli lahko menit
hladane_slovo = list(dlzka * "_")
print(dlzka * "_ ")
pocet_zivotov = 8
zoznam_pismen = []

# 2. vstup pismena a doplnenie
# Chyba kontrola ci nam uzivatel skutocne zadal
# pismeno
pismeno = input("Zadaj pismeno: ")
if pismeno in slovo:
    # Pozriem sa, ci som toto pismeno este nehadal
    if pismeno not in zoznam_pismen:
        zoznam_pismen.append(pismeno)
    else:
        # continue
        pass
    # 
    for i in range(len(slovo)):
        if pismeno == slovo[i]:
            hladane_slovo[i] = pismeno
else:
    # Ak sa pismeno nenachadza v slove
    # Stratime zivot
    pocet_zivotov = pocet_zivotov - 1

print(hladane_slovo)
print(pocet_zivotov)

# 3. Koniec
# vyriesme pocet_zivotov
