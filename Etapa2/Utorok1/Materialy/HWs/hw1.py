# Uloha 1
# Napiste spravne podmienku, aby v premennej vodicak
# boli ulozene ktore vsetky vodicaky moze clovek na zaklade veku
# mat.
# Pre jednoduchost
# 14 a menej rokov = vysledok ma byt ""
# 15 a 16 = A
# 17 a viac = AB
vek1 = 15
vek2 = 18

# Vas kod piste do tejto casti
# Kod by mal obsahovat dve podmienky ktore budu obsahovat vetvu else (a pripade elif alebo dvakrat else if)
if vek1 > 0:
    vodicak1 = ""

if vek2 > 0:
    vodicak2 = ""

# Koniec casti na Vas kod

# Testy
assert vek1 == 15
assert vek2 == 18
assert vodicak1 == "A"
assert vodicak2 == "AB"



# Uloha 2
# Napiste podmienku, ktora na zaklade cisla v premennej (cislo1,cislo2,cislo3)
# Vrati do premennej znamienko ci je cislo Pozitivne, Negativne alebo 0
cislo1 = -4
cislo2 = 0
cislo3 = 44
vysledok = ""
# Vas kod piste do tejto casti
# Ak Vam prejde prvy test, skopirujte podmienku za testy a upravne premennu
if cislo1 > 0:
    vysledok = "Pozitivne"

assert cislo1 == -4
assert vysledok == "Negativne"

# Druha podmienka

assert cislo2 == 0
assert vysledok == "Zero"


# Tretia podmienka

assert cislo3 == 44
assert vysledok == "Pozitivne"
# Koniec casti na Vas kod


print("Vsetky testy uspesne presli")