# Opakovanie prikladu na sucin dvoch cisiel
# nemozeme pouzit operaciu *
def moj_sucin(a, b):
    sucin = 0
    for i in range(b):
        sucin += a
    print(sucin)

moj_sucin(4,8)

# K for cyklom, co sa skutocne deje ked zavolam range(5)
for i in range(5):
    print(i)

# je to iste ako
for i in [0,1,2,3,4]:
    print(i)

# takze sa nam vygeneruje nieco, co v Pythone nazyvame ZOZNAM

# Zoznam je prva komplexnejsie datova struktura, ktoru sa naucime
# nie je to jednoduchy typ ako cislo, retazec, ale struktura ktora moze v
# sebe zahrnat viac ako jednu informaciu

# Vytvorime ho pomocou hranatych zatvoriek
zoznam = [1,2,3,4,5]

# Prazdny zoznam
zoznam2 = []

# Ked sme si ukazovali funkcie, ktora Python pozna -> tak som hovoril, ze
# nam ich vysvieti na fialovo
print()
input("Stlac enter")

# Okrem toho ale existuju aj funkcie, ktora sa viazu na konkretny typ
# V takom pripade ich ale Python nevysvieti na fialovo
# Priklad
meno = "Ivan"
print(meno)

print(meno.upper())
# Funkcia upper nam z retazca urobi retazec, kde su vsetky pismena velkym

# Napriklad funkcia upper by ale na CISLE/BOOL zlyhala s errorom

# Datovo struktura zoznam ma takychto funkcii vela, my budeme pouzit hlavne
zoznam = [1,2,3]
zoznam.append(4)
print(zoznam)

# Teda priradenie na koniec zoznamu

# Uzitocne su aj funkcia insert, alebo napr. sort
# Dlzku nasho zoznamu ziskame pomocou len
print(len(zoznam))

# Rovnako vieme pristupit ku konkretnym prvkom zoznam
print(zoznam[1])
# POZOR - ked chceme pristuput k prvku na pozicii 1
# musime pouzit index 0
print(zoznam[0])

# Takto to funguje vo vacsine programovacich jazykoch

# Priklady pouzitia zoznamu vo funkciach
# Vypis sucet cisiel v zozname, ktore su vacsie ako 5
zoznam = [1,2,3,4,5,6,7,8,9,10]
sucet = 0
for cislo in zoznam:
    if cislo > 5:
        sucet += cislo
print("Sucet cisel vacsich ako 5 v zozname", zoznam)
print("Je", sucet)

# Zoznam sa nam hodi pri praci so subormi
# PRED SPUSTENIM TEJTO CASTI SA PROSIM UISTITE, ZE MATE VYTVORENY
# SUBOR subor.txt v takom istom subore ako sa nahadza tento program
# mate ten subor prilozeny v emaily

# Subor vieme otvorit aj pomocou
# file = open('subor.txt', 'r') ale potom ho musime aj rucne zavriet pomocou
# file.close()

# Namiesto toho budeme pouzivat, ktore nam automaticky aj subor zavrie
with open('subor.txt', 'r') as file:
    # Teraz musime zo suboru nieco prepisat
    # pouzili sme druhy parameter 'r', je to sposob otvorenia suboru
    # r = otvorenie na citanie
    # w = otvorenie na citanie a zapis
    # a = otvorenie na citanie a zapis na koniec suboru

    # Zo suboru vieme citat vsetky riadky, ktore sa nam potom ulozia do zoznamu
    # pomocou
    riadky = file.readlines()

    print(riadky)

    # Vsimnime si, ze tam mame \n, co je subor noveho riadku
    # Ked sa ho chceme zbavit, pouzijeme
    riadky = [riadok.rstrip() for riadok in riadky]
    print(riadky)

    # Teraz vieme tieto nacitane hodnoty zratat ako cisla
    sucet = 0
    for cislo in riadky:
        sucet += int(cislo)
    print("Sucet cisel v subore je:", sucet)

