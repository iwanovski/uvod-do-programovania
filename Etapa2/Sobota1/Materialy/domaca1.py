# Uloha 1
# Napiste spravne podmienku, aby funkcia vodicak
# vratila ake vsetky vodicaki moze mat osoba podla veku
# Pre jednoduchost
# 14 a menej rokov = vysledok ma byt ""
# 15 a 16 = "A"
# 17 a viac = "AB"

# Vas kod piste do tejto casti
# Kod by mal obsahovat dve podmienky ktore budu obsahovat vetvu else (a pripade elif alebo dvakrat else if)
def vodicak(vek):
    return ""

# Koniec casti na Vas kod

# Testy
assert vodicak(10) == ""
assert vodicak(14) == ""
assert vodicak(15) == "A"
assert vodicak(19) == "AB"
assert vodicak(17) == "AB"
assert vodicak(31) == "AB"



# Uloha 2
# Napiste podmienku, ktora na zaklade cisla v vo funkcie znamienko
# Vrati ci je cislo Pozitivne, Negativne alebo 0
# Vas kod piste do tejto casti
# Ak Vam prejde prvy test, skopirujte podmienku za testy a upravne premennu
def znamienko(cislo):
    return ""

# Koniec casti na Vas kod

assert znamienko(-4) == "Negativne"
assert znamienko(-1232) == "Negativne"
assert znamienko(0) == "Zero"
assert znamienko(44) == "Pozitivne"
assert znamienko(4) == "Pozitivne"


print("Vsetky testy uspesne presli")