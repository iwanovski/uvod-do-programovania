# Riesenia uloh z prvej hodiny kurzu - sobota

# Vypis hello world, mena + priezviska
print("Hello World")
print("Ivan Havran")

# Pouzitie premennych
meno = "Ivan"
priezvisko = "Havran"
print(meno, priezvisko)
print(meno + " " + priezvisko)
print(type(meno))

# Pridat novy typ premennej - vek
vek = 25
print(type(vek))
print(meno,priezvisko,vek)
print(meno + " " + priezvisko + " " + str(vek))

# Pouzitie input funkcie
meno = input("Zadaj meno: ")
priezvisko = input("Zadaj priezvisko: ")
vek = input("Zadaj vek: ")
print(meno,priezvisko,vek)

# Pretypoanie stringu z inputu na cele cislo
print("O 10 rokov budem mat", int(vek) + 10)

# Pouzitie vlastnych funkcii
# definicia
def sucet():
    cislo1 = int(input("Zadaj cislo1: "))
    cislo2 = int(input("Zadaj cislo2: "))
    print(cislo1 + cislo2)
# volanie
sucet()

# Podmienky
def porovnaj():
    cislo1 = int(input("Zadaj cislo1: "))
    cislo2 = int(input("Zadaj cislo2: "))
    if cislo1 > cislo2:
        print("Cislo1 je vacsie")
    elif cislo2 > cislo1:
        print("Cislo2 je vacsie")
    else:
        print("Cisla su rovnake")
porovnaj()

# Vek + vratenie z funkcie
def vodicak():
    vek = int(input("Zadaj vek: "))
    if vek < 15:
        return ""
    elif vek < 18:
        return "A"
    else:
        return "AB"
print(vodicak())

# For cyklus + parameter vo funkcii
def vodicak2(vek):
    if vek < 15:
        return ""
    elif vek < 18:
        return "A"
    else:
        return "AB"
    
for i in range(25):
    print("Tento vek moze mat vodicak typu: ",vodicak2(i))
    
