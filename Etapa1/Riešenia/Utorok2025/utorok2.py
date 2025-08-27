# Definicia vlastnej funkcie
def mocnina(cislo):
    # Funkcia moze mat viac vstupnych argumentov
    return cislo * cislo
    # Prikazom return vraciame vystup z funkcie

# Vstup a vystup
meno = input("Zadaj svoje meno: ")
print("Ahoj",meno)

vstup = int(input("Zadaj cislo: "))
print("Vstup", vstup)

# Ulozenie vystupu funkcie do premennej
vystup = mocnina(vstup)
print("Mocnina zadaneho cisla je", vystup)


# Podmienky
vek = int(input("Zadaj svoj vek: "))

# Ak plati vyraz, urob nieco
if vek > 40:
    print("Mas viac ako 40 rokov")
else:
    print("Mas menej alebo rovno 40 rokov")

# Cyklus - for = s pevnym poctom opakovani
for i in range(5):
    print(i)
    print("For cyklus opakovanie")
