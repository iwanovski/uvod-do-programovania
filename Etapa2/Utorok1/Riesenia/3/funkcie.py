# Uloha 2
def znamienko(cislo):
    if cislo > 0:
        vysledok = "Pozitivne"
    elif cislo == 0:
        vysledok = "Zero"
    else:
        vysledok = "Negativne"
    return vysledok

# Napiste podmienku, ktora na zaklade cisla v premennej (cislo1,cislo2,cislo3)
# Vrati do premennej znamienko ci je cislo Pozitivne, Negativne alebo 0
cislo1 = -4
cislo2 = 0
cislo3 = 44
vysledok = ""
# Vas kod piste do tejto casti
# Ak Vam prejde prvy test, skopirujte podmienku za testy a upravne premennu
vysledok = znamienko(cislo1)
assert cislo1 == -4
assert vysledok == "Negativne"

# Druha podmienka
# vysledok = moja_funkcia(cislo2)
vysledok = znamienko(cislo2)

assert cislo2 == 0
assert vysledok == "Zero"

# Tretia podmienka
vysledok = znamienko(cislo3)

assert cislo3 == 44
assert vysledok == "Pozitivne"
# Koniec casti na Vas kod


print("Vsetky testy uspesne presli")
