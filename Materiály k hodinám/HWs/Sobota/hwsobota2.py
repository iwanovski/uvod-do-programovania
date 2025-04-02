# 1. Úloha
# Naprogramujte funkciu najvacsie, ktora Vam vrati
# najvacsie cislo, ake sa nachadza v zozname cisel na vstupe
def najvacsie(zoznam_cisel):
    return 0

# Testy - ak naprogramujete funkciu spravne
# tento kod vam nehodi chybu
assert najvacsie([1,2,5,3,1,3,6,7,4,3,2,5,6,4,3]) == 7
assert najvacsie([-1, -5, -3, -8]) == -1
assert najvacsie([100, 50, 200, 150]) == 200
assert najvacsie([0, 0, 0, 0]) == 0

# 2. Úloha
# Naprogramujte funkciu iba_parne, ktora Vam vrati
# sucet parnych cisel v zozname
# POMOCKA:
# ci je cislo parne zistim porovnanim
# if cislo % 2 == 0:
def iba_parne(zoznam_cisel):
    return 0


# Testy - ak naprogramujete funkciu spravne
# tento kod vam nehodi chybu
assert iba_parne([2, 4, 6, 8]) == 20
assert iba_parne([1, 3, 5, 7]) == 0
assert iba_parne([1, 2, 3, 4, 5, 6]) == 12
assert iba_parne([-2, -4, -6, -8]) == -20
assert iba_parne([-1, -2, -3, -4, -5, -6]) == -12
assert iba_parne([0, 0, 0, 0]) == 0
assert iba_parne([]) == 0
assert iba_parne([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 30
assert iba_parne([-1, 2, -3, 4, -5, 6]) == 12

