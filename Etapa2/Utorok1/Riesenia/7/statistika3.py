# Legenda: meno,priezvisko,zapasy,goly,asistencie
pomer_ga = []
ga_hodnoty = []

zapis = open("pomer2.txt", mode="w")

with open("hraci.txt", mode="r") as file:
    riadky = file.readlines()
    for riadok in riadky:
        # Odstranit specialny znak noveho
        # riadka na konci kazdeho riadku
        riadok = riadok.rstrip()
        udaje = riadok.split(",")

        goly = int(udaje[3])
        asistencie = int(udaje[4])
        zapasy = int(udaje[2])
        pomer = round((goly + asistencie) / zapasy,2)
        print(pomer)
        ga_hodnoty.append(pomer)


        #vysledny_riadok = udaje[0] + " " + udaje[1]+ " " + str(pomer) + "\n"
        # F-string - viete pouzit realne premenne, ktorym sa nahradia
        # hodnoty do stringu
        vysledny_riadok = f"{udaje[0]} {udaje[1]} {pomer}\n"
        print(vysledny_riadok)

        

        pomer_ga.append(vysledny_riadok)
        zapis.write(vysledny_riadok)
        print(ga_hodnoty)

    # 3. pre kazdeho hraca vyrajte tzv.
    # pomer G/A na zapasy

    # (goly+asitencie) / zapasov = G/A
    # Do novehu suboru pomer
    # napiste pre kazdeho hraca zaznam v tvare
    # "meno priezvko g/a"
    # "Juraj Slafkovsky 0,61"

    # Najprv pripravime zoznam riadkov vystupu
    # a nakonci to vypiseme

    # 4. Tiez ratame G/A
    # Ale vo vystupnom subore chceme mat hracov zoradenych od
    # najvacsieho G/A po najmensie

with open("pomer.txt", mode="w") as file2:
    # file2.writelines(pomer_ga)
    
    zoradeny_pomer_ga = []
    zoradene_riadky = []
    
    for riadok in pomer_ga:
        riadok = riadok.rstrip()
        udaje = riadok.split(" ")
        ga = udaje[2]


zapis.close()
    


