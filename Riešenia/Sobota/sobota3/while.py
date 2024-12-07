# For cyklus
# Vykoname prikazy urcity pocet krat
#for i in range(10):
    #print("Hello")


# While cyklus
# Vykonavaj prikazy kym plati vyraz
i = 0
while i < 10:
    print(i)
    # Pozor na nekonecny cyklus, keby zakomentujeme zvysenie cisla
    i += 1

# Hra - uhadni nahodne vygenerovane cislo

# Pouzijeme vstavanu kniznicu z Pythonu - random
from random import randint
# z kniznie random sme naimportovali funkciu randint

cislo = randint(1, 100)
moje_cislo = int(input("Zadaj cislo: "))
while cislo != moje_cislo:
    if moje_cislo > cislo:
        print("Zadal si prilis velke cislo")
    else:
        print("Zadal si prilis male cislo")
    moje_cislo = int(input("Zadaj cislo: "))
print("Gratulujem, uhadol si cislo")
