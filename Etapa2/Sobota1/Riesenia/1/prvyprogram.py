# Konstanty 
MENO2 = 45

# Definicie funkcie
# viacako0 = nazov funkcie
# cislo = argument funkcie
def viacako0(cislo):
    if int(cislo) > 0:
        print("Zadal si cislo vacsie ako 0")
    else:
        print("Zadal si cislo mensie/rovne 0")

def porovnavac(cislo1, cislo2):
    viacako0(cislo1)
    viacako0(cislo2)

# print - funkcia od Pythonu,
# obsahuje ine prikazy

# () - sluzia na zavolanie
# funkcie

# typ informacie - hovoria
# pocitacu, ako si interpretovat
# 01 (znaky)

# "" - typ string - retazec
# zhluk pismen,cisel,specialnych
# znakov

# premenna = sposob ulozenia hodnoty
# na dalsie pouzitie
# staticke premenna -> konstanty
# <nazov> = (priradenie) <hodnota>
meno = "Ivan"
# dynamicka premmena -> dokazem menit jej hodnotu

# typ int = cele cislo
cislo = 5

print("Hello World")
print(cislo)
print(meno)
print("488wq3*")

cislo = cislo + 2
print(cislo)

cislo = "sedem"
print(cislo)

"Havran"

# argument (vstup) funkcie
# funkcia moze vyzadovat
# nejake argumenty na svoje
# fungovanie

print()
print("Havran")
print(meno,"Havran")

# moja poznamka

# Vstup
# input = funkcia na nacitanie vstupu
# z konzoly
vstup = input("Zadaj meno:")
priezvisko = input("Zadaj priezvisko: ")
print("Ahoj", vstup, priezvisko)

# vyraz = o com vieme jasne
# povedat, ci to je pravda alebo nie

# typ bool = False/True
# vyraz sa vzdy vyhodnoti na jedno
# z tychto dvoch

# Podmienky
# podmienime vykonanie kodu
# nejakym vyrazom

# vstup sa vzdy nacitava ako retazec
# ak ho chceme pouzit inak
# musim spravit tzv. pretypovanie
# pretypovanie nie je bezpecna operacia
# moze skoncit s chybou
cislo = input("Zadaj cislo")
# print("Premenna ma typ", type(cislo))
if int(cislo) > 0:
    print("Zadal si cislo vacsie ako 0")
else:
    print("Zadal si cislo mensie/rovne 0")
print("Koniec programu")
    
# Vlastne funkcie
# motivacia rovnaka ako pri funkciach
# vytvorite "skratku" pre viacej prikazov
viacako0(45)
viacako0(-85)

# Volanie funkcie
print("Koniec programu2")










