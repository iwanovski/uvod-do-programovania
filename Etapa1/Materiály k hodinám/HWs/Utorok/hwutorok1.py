# 1. Úloha
"""
Naprogramujte funkciu cena_odpadu, ktora
na zaklade poctu kilogramov (vstup) vyrata cenu,
ktoru musi clovek zaplatit aby mohol odpad ulozit

Cennik:
1 kg - 50 kg = 20
50 - 100 kg = 30
100 - 1000 kg = 100
viac ako 1000kg = 1.2 nasobok poctu kilogramov
"""
def cena_odpadu(pocet):
    return 0

# Testy - ak naprogramujete funkciu spravne
# tento kod vam nehodi chybu
assert cena_odpadu(23) == 20
assert cena_odpadu(49) == 20
assert cena_odpadu(78) == 30
assert cena_odpadu(99) == 30
assert cena_odpadu(155) == 100
assert cena_odpadu(266) == 100
assert cena_odpadu(1275) == 1530
assert cena_odpadu(32321) == 38785.2

# 2. Úloha
"""
Naprogramujte funkciu vyskovy_index, ktora na zaklade veku
a vysky (v cm) vypocita index v tvare
Ak je vek menej alebo rovny 25 rokov
index = 1.42 + vek + vyska
INAK
index = 1.8 + vek + vyska
"""
def vyskovy_index(vek, vyska):
    return 0

assert vyskovy_index(31, 183) == 215.8
assert vyskovy_index(12, 153) == 166.42
assert vyskovy_index(57, 192) == 250.8

