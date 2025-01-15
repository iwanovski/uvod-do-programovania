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

# Vek funkcia
def vek():
    vek = int(input("Zadaj vek: "))
    if vek < 30:
        print("Mas menej ako 30")
    elif vek < 50:
        print("Mas menej ako 50")
    else:
        print("Mas viac ako 50")
vek()

# For cyklus + funkcia s parametrom namiesto vstupu
def vek2(vek):
    if vek < 30:
        print("Mas menej ako 30")
    elif vek < 50:
        print("Mas menej ako 50")
    else:
        print("Mas viac ako 50")

for i in range(45):
    vek2(i)

    
