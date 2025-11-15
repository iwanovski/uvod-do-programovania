# Domaca uloha 3

# Nacitajte data zo suboru statistika, v ktorom sa nachadzaju udaje o studentoch z rocnika.
# Riadky su v tvare
# MENO,VYSKA v CM, VAHA v KG
# Mate tri ulohy

# 1. Do premennej priemer_vysok vypocitat priemer vysky vsetkych ziakov dokopy
# zaokruhlite na 2 desatinne miesta pomocou funkcie round
priemer_vysok = 0.0

# 2. Zistit pocet ziakov, ktorych vaha je viac ako 54 ale menej ako 71
# tuto hodnotu ulozte do premennej pocet_ziakov
pocet_ziakov = 0

# 3. Zistit meno ziaka, ktory ma najvacsiu vahu a vysku ked ich zratame dokopy
# vaha+vyska, meno zapiste do premennej maximum
maximum = ""

with open("statistika.txt") as file:
    riadky = file.readlines()

    for riadok in riadky:
        # Doplnte kod sem
        pass


# TESTY

assert priemer_vysok == 173.5

assert pocet_ziakov == 4

assert maximum == "Karol"