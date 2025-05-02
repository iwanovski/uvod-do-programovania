# 1. Uloha
# Naprogramuj funkciu najvacsie, ktora
# vam vrati najvacsie cislo zo zoznamu cisel
def najvacsie(zoznam):
    # == - porovnanie ci sa veci rovnaju
    # != - porovanie ci sa veci nerovnaju
    if zoznam == []:
    # if len(zoznam) == 0:
        print("Dal si prazdny zoznam")
        return
    najvacsie_cislo = zoznam[0]
    for i in range(len(zoznam)):
        cislo = zoznam[i]
        if cislo > najvacsie_cislo:
            najvacsie_cislo = cislo
    return najvacsie_cislo

# For cyklus = zopakuje nejake prikazy
# nejaky pocet krat

print(najvacsie([-1,7,-22,418,48,-18,-8]))
print(najvacsie([10001,7,-22,418,48,-18,-8]))
print(najvacsie([1,7]))
print(najvacsie([1]))
print(najvacsie([]))


