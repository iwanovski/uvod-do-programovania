# Praca so subormi

# pomocou file = open(<nazov_suboru>) otvarame subor

# pomocou file.close() subor musime zatvorit

# Rovnako ale vieme pouzit with, ktore za nas subor zatvori

# Ukazka

# Subor vieme otvorit v troch rezimoch

# mode="r" - znamena subor na citanie

# mode="w" - znamena subor na zapis - pozor, mozeme si prepisat existujuci subor

# mode="a" - znamena subor na zapis na koniec suboru

# Sucast uloh 3. a 4. - otvorime aj jeden subor na zapis
file1 = open("uprava.txt", mode="w")

with open("hraci.txt", mode="r") as file:
    # Subor musime vzdy raz precitat
    # Najlahsie sa subor precita pomocou funkcie readlines
    riadky = file.readlines()

    # Z riadkov musime odstranit \n co je znak noveho riadku
    # Vyuzijeme prikaz r.strip()

    riadky = [riadok.rstrip() for riadok in riadky]
    print(riadky)

    # Ak riadok obsahuje viac ako jednu informaciu a informacie
    # su rozdelene ciarkou (ako v .csv) subori
    # Pouzivame funkciu split
    for riadok in riadky:
        rozdeleny = riadok.split(',')
        print(rozdeleny)

    # Uloha 1: Spocitajte, kolko golov mali nasi hraci dokopy
    sucet_golov = 0
    for riadok in riadky:
        rozdeleny = riadok.split(',')
        pocet_golov = int(rozdeleny[3])
        sucet_golov += pocet_golov

    print("Sucet golov nasich hracov bol", sucet_golov)

    # Uloha 4: Pridajte na zaciatok ineho suboru legendu
    # Meno,Priezvisko,Zapasy,Goly,Asistencie,Body
    file1.write("Meno,Priezvisko,Zapasy,Goly,Asistencie,Body\n")

    # Uloha 2: Spocitajte pocet bodov = Goly + Asistencie
    # Vypiste v tvare
    # Hrac <priezvisko> mal dokopy <sucet_bodov> bodov
    for riadok in riadky:
        rozdeleny = riadok.split(',')
        pocet_golov = int(rozdeleny[3])
        pocet_asistencii = int(rozdeleny[4])
        sucet_bodov = pocet_golov + pocet_asistencii
        print(f"Hrac {rozdeleny[1]} mal dokopy {sucet_bodov} bodov")

    # Uloha 3: Zapiste pocet bodov ku kazdemu hracovi do noveho suboru
        spravny_riadok = riadok + f",{sucet_bodov}\n"
        file1.write(spravny_riadok)

file1.close()
        

    
