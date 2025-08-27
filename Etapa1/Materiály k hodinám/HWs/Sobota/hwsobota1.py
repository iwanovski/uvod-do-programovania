# 1. Úloha
# Naprogramujte funkciu cena_vstupneho
# ktora na vstupe berie jeden argument VEK
# Na zaklade veku, vratte z funkcie, kolko bude stat
# vstupne do kina
# Pre deti do 10(vratane) je vstupne 5 (staci vratit cislo)
# Pre tinedzerov medzi 11 a 18 rokov je vstupne 7 
# Pre ludi nad 18 a do 65 je cena 9
# Pre ludi nad 65 rokov je cena 8
# Doprogramujte funkciu sem
def cena_vstupneho(vek):
    return 0

# Testy - ak naprogramujete funkciu spravne
# tento kod vam nehodi chybu
assert cena_vstupneho(68) == 8
assert cena_vstupneho(25) == 9
assert cena_vstupneho(15) == 7
assert cena_vstupneho(5) == 5

# 2. Úloha
# Naprogramujte funkciu vypis, ktora zoberie
# na vstup meno, priezvisko, datum
# (vo formate DD.MM.YYYY) a vrati retazec
# v tvare MENO_PRIEZVISKO_DD.MM.YY
def vypis(meno , priezvisko, datum):
    return ""

# Testy - ak naprogramujete funkciu spravne
# tento kod vam nehodi chybu
assert vypis("Ivan", "Kovac", "25.04.1996") == "Ivan_Kovac_25.04.1996"
assert vypis("Elena", "Gonzalez", "13.02.1965") == "Elena_Gonzalez_13.02.1965"

# 3. Úloha
# Naprogramujte funkciu vykonaj_x ktora vypise
# sucet cisiel A a B, ktora dostaneme na vstupe
# tolko krat, kolko je X na vstupe
def vykonaj_x(a, b, x):
    pass

