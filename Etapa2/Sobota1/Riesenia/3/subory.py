

# Subory
# open == otvorenie suboru
# potrebujeme nazov suboru
# ak date subor co neexistuje,
# hodi to chybu
file = open("data.txt", "r")
# r = read mode = iba na citanie
# w = write mode = na zapis (od zaciatku)
# a = append mode = na zapis (od konca suboru)

# Citanie informacii zo suboru
# read(pocet_znakov)
# print(file.read(5))

# readlines()
# precitaj mi vsetky riadky suboru
# pozor na \n na konci riadkov
# \n == symbol noveho riadku
riadky = file.readlines()
# rstrip = odstranenie specialnych
# symbolov
print(riadky[1].rstrip())

pocet = 0
samohlasky = ["a","e","i","o","u","y"]
# Spocitaj pocet samohlasok v riadkoch
# Pre kazdy riadok
for riadok in riadky:
    # Pre kazdy znak v riadku
    for pismeno in riadok:
        # Zisti ci je znak samohlaska
        if pismeno.lower() in samohlasky:
            pocet = pocet + 1
print(pocet)

# Uloha:
# priemer vysok
sucet = 0
# Zisti priemernu vysku vsetkych ludi v subore
for riadok in riadky:
    riadok = riadok.strip()
    # Nejakym sposobom rozdelit riadok
    # pomomcou ciarky na udaje
    udaje = riadok.split(",")
    print(udaje)
    # vytiahni spravny udaj
    sucet = sucet + int(udaje[1])

# Otvorenie na zapis do suboru
file2 = open("output.txt", "w")
print(sucet / len(riadky))

# Zapis do suboru
# f-string
# retazec = "Priemer vysok je " + str(sucet / len(riadky))
# nahradime premenne za ich realne hodnoty
# kod v {} sa berie ako realny kod v Pythone
file2.write(f"Priemer vysok je {sucet / len(riadky)}")

# Zatvorenie suboru
# funkcia close
# ak nezatvorim subor na zapis, neuvidim co som zapisal
file2.close()

# Ako otvorit subor tak, aby sa sam zavrel
# sluzi nam nato slovicko with
with open("vystup.txt", "w") as file3:
    file3.write(f"Priemer vysok je {sucet / len(riadky)}")

# Toto by hodilo chybu, lebo musime byt odsadeni
# file3.write("Zapis znovu")

# Uloha
# Zisti priemernu vahu ludi ktori maju vacsiu vysku
# ako 175cm
sucet = 0
# Pocet = kolko ludi mi splnilo podmienku
pocet = 0
for riadok in riadky:
    riadok = riadok.strip()
    # Nejakym sposobom rozdelit riadok
    # pomomcou ciarky na udaje
    udaje = riadok.split(",")
    print(udaje)

    # Vyska vacsie ako 175
    if int(udaje[1]) > 175:
        sucet = sucet + int(udaje[2])
        pocet = pocet + 1
    # Vyfiltrovat ludi s mensou vyskou ako 175
    # Ostatnym spocitaj priemer vah
print("Priemer vahy ludi vyssich ako 175")
print(sucet / pocet)


# Uloha
# Zorad ludi podla vysky od najmensieho po najvyssieho
# a zapis do suboru zoradene
zoznam_vysok = []
slovnik_vysok = {}
with open("zoradene.txt", "w") as file4:
    for riadok in riadky:
        riadok = riadok.strip()
        # Nejakym sposobom rozdelit riadok
        # pomomcou ciarky na udaje
        udaje = riadok.split(",")
        # Priradte vysku cloveka do zoznamu
        vyska = int(udaje[1])
        zoznam_vysok.append(vyska)
        # Pri vytvarani kluca s vyskou
        # osetrime pripad ze clovek s vyskou uz moze existovat
        if vyska in slovnik_vysok.keys():
            slovnik_vysok[vyska].append(riadok)
        else:
            slovnik_vysok[vyska] = [riadok]

    # ? ako ich zoradit
    # pomoze nam funkcia .sort() ktora vie zoradit cislo v zozname
    zoznam_vysok.sort()
    print(zoznam_vysok)

    print(slovnik_vysok)

    # Zoradenie vysok ludi
    # najlahsie je to mat vysky v zozname a potom ich zoradit
    
    # Prepojenie zoradeneho zoznamu so slovnikom vysok
    for vyska in zoznam_vysok:
        clovek = slovnik_vysok[vyska][0]
        if len(slovnik_vysok[vyska]) > 1:
            # [1:] - odstran zo zoznamu prvy prvok
            slovnik_vysok[vyska] = slovnik_vysok[vyska][1:]

        file4.write(clovek+"\n")




    

