# Vlastne funkcie
# 1. definicia funkcie
def sucet(cislo1, cislo2):
    # telo funkcie
    # print(cislo1+cislo2)
    vysledok = cislo1 + cislo2
    # print(vysledok)
    vysledok = vysledok - 10
    return vysledok
    
    # return None

# Funkcie
print("Hello")

# 2. zavolanie funkcie
sucet1 = sucet(4,9)
print(sucet1)


sucet2 = sucet(4,6)
print(sucet(94,6))
print(sucet2 + 100)

# Porovnaj
def porovnaj(cislo1, cislo2):
    # Vratte 1 ak je prve cislo vacsie
    # Vratte 2 ak je druhe cislo vacsie
    # Inak vratte 0
    if cislo1 > cislo2:
        return 1
    elif cislo1 < cislo2:
        return 2
    return 0

print(porovnaj(4,2)) # vypise 1
print(porovnaj(2,3)) # vypise 2
    
