# Input, print, premenna
# HOTOVO

# Vyraz
# je nieco, o com vieme
# jasne povedat, ci to je
# pravda, alebo nie
# bool/boolean/pravda nepravda


# Podmienky
# if <VYRAZ>:
vek = int(input("Zadaj vek: "))
# Zlozeny vyraz = cez spojku, vyhodnoti
# sa na jedno True/False
# if ((vek > 35) and (vek < 50)):
if vek > 35:
    # Ak plati vyraz
    print("Mam viac >35")
elif vek > 18:
    print("Mam 19-35")
else:
    # Inak urob toto
    print("Mam <= 18")

if vek > 35:
    # Ak plati vyraz
    print("Mam viac >35")
else:
    if vek > 18:
        print("Mam 19-35")
    else:
        print("Mam <= 18")
print("Koniec programu")


# Vlastne funkcie
# Cykly
