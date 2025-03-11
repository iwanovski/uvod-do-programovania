# Komentar je to co citas teraz a napise sa to pomocou mriezky
# Python tuto cast kodu ignoruje a bude nam sluzit na pisanie poznamok do kodu

# Prvy program
# hello world
print("Hello World!")

# Premenna, sluzi nam na ulozenie nejakej informacie
# vytvorenie
# <nazov> = <hodnota>
# Pozname viacero typov
# typ string, co je retazec
meno = "Ivan"
priezvisko = "Havran"

# typ int, co je cele cislo
vek = 26
print(meno, priezvisko, vek)

# funkcia input - nacitanie vstupu od uzivatela
meno = input("Zadaj meno: ")
priezvisko = input("Zadaj priezvisko: ")

# pozor pri praci s cislami, musime si
# cislo aj ulozit ako typ cislo
# posluzi nam funkcia int
vek = int(input("Zadaj vek: "))
print("O 10 rokov budes mat", vek + 10)

# Podmienky
# Umoznuju nam kod vetvit - niektore casti
# sa zavolaju len vtedy, ak plati alebo neplati
# podmienka

# Vyraz = nieco, o com vieme jasne povedat
# ci to je pravda alebo nie
# priklad = dnes je piatok
# vieme jasne povedat, ci to je pravda, alebo nie

# Potrebujeme novy typ, tzv. bool
# ma len dve hodnoty - True alebo False

# Podmienka
if vek > 15:
    print("Mas narok na vodicak")
else:
    # Vetva else znamena, ak neplati vyraz, vykonaj to co je o vetve else
    print("Nemas narok na vodicak")

# Vetva elif - aby sme nemuseli vyrazne zanorovat vetve if else, vznikla
# tretia moznost, elif
# pouzitie

# Namiesto tohto kodu
# if vek > 15:
    #f vek < 17:
        #print("Mozes mat vodicak na motorku")
    #else:
        #print("Mozes mat vodicak na motorku aj auto")
#else:
    #print("Nemozes mat vodicak")

# Vieme pouzit elif
if vek <= 15:
    print("Nemozes mat vodicak")
elif vek < 17:
    print("Mozes mat vodicak na motorku")
else:
    print("Mozes mat vodicak na motorku aj auto")

# Funkcie
# doteraz sme pouzivali funkcie, ktore nam
# Python priamo poskytuje
# ukazeme si, ako vytvorit vlastnu

# Definicia funkcie
def sucet(cislo1, cislo2):
    # Prikaz return nam sluzi nato, ze nam funkcia
    # vrati vystup, ktore potom vieme ulozit do premennej
    return cislo1 + cislo2

# Funkciu musime aj zavolat
vysledok = sucet(5, 9)
print(vysledok)

# Cykly
# For cyklus = cyklus s pevnym poctom opakovani
# sposobom ako vykonat nejake prikazy viackrat v rade
for i in range(5):
    print("hello world")
    print("test")

# Ako napisat sucet pomocou for cyklu
# ked nemozme pouzit cislo1 + cislo2
def sucet2(cislo1, cislo2):
    sucet = cislo1
    for i in range(cislo2):
        sucet = sucet + 1
    return sucet

vysledok = sucet2(5, 9)
print(vysledok)

# Napis funkciu predstavenie a nechaj troch
# ludi sa predstavit

def predstavenie(meno, priezvisko, vek):
    print(meno)
    print(priezvisko)
    print(vek)

for i in range(3):
    meno = input("Zadaj meno: ")
    priezvisko = input("Zadaj priezvisko: ")
    vek = int(input("Zadaj vek: "))
    predstavenie(meno, priezvisko, vek)
