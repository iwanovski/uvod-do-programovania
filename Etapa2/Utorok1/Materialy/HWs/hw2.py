# Uloha 1
# Naprogramuj funkciu delitelne_2, ktora pre 
# cislo (argument) zisti, ci je toto cislo delitelne dvoma
# a vrati True alebo False
# NAPOVEDA
# Mate dve moznosti, bud napisat vhodne podmienku, alebo pouzit for cyklus
# kym cislo nebude 0 alebo -1

# Vas kod piste do tejto casti
def delitelne_2(cislo):
    return True

# Koniec casti na Vas kod

# Testy
assert delitelne_2(31) == False
assert delitelne_2(12434) == True
assert delitelne_2(1) == False
assert delitelne_2(2) == True
assert delitelne_2(3132134) == True
assert delitelne_2(105) == False


# Uloha 2
# Napiste funckiu pozdrav(meno, priezvisko, mesto) ktora pozdravi nas5 v tvare
# Ahoj <meno> <priezvisko>, pochadzas z <mesto>

# Vas kod piste do tejto casti
def pozdrav(meno, priezvisko, mesto):
    return ""

# Koniec casti na Vas kod

# Testy
assert pozdrav("Eva", "Mudra", "Kosice") == "Ahoj Eva Mudra, pochadzas z Kosice"
assert pozdrav("Peter", "Kratky", "Bratislava") == "Ahoj Peter Kratky, pochadzas z Bratislava"
assert pozdrav("Martin", "Biely", "Banska Bystrica") == "Ahoj Martin Biely, pochadzas z Banska Bystrica"
# Koniec casti na Vas kod


print("Vsetky testy uspesne presli")